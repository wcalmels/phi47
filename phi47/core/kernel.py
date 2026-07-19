"""
phi47.core.kernel
=================

Project-specific synthetic oscillatory kernel used by the φ⁴⁷ lattice.

Scientific status
-----------------
This module implements a deterministic numerical construction defined by

    K_N(n) = a(n) · φ^(-n/N) · exp(2π i n/N),

where

    a(n) = (-1)^(n mod 7) · ((n mod 100) + 1).

The sequence a(n) is a synthetic periodic amplitude rule created for this
project. It is not Ramanujan's tau function and has not been demonstrated to
approximate, derive from, or preserve the arithmetic properties of Ramanujan's
tau function.

The neutral names ``phi47_kernel`` and ``phi47_kernel_batch`` are therefore the
canonical public API.
"""

from __future__ import annotations

import cmath
import math
from functools import lru_cache

import numpy as np

from .constants import PHI, N


@lru_cache(maxsize=65536)
def phi47_kernel(n: int, dim: int = N) -> complex:
    """
    Evaluate the synthetic φ⁴⁷ oscillatory kernel for one integer.

    Parameters
    ----------
    n:
        Non-negative integer argument.
    dim:
        Positive lattice dimension. The default is the project dimension 47.

    Returns
    -------
    complex
        Complex kernel value.

    Raises
    ------
    TypeError
        If ``n`` or ``dim`` is not an integer.
    ValueError
        If ``n`` is negative or ``dim`` is not positive.

    Notes
    -----
    This function is a project-specific numerical construction. It is not
    Ramanujan's tau function.

    Examples
    --------
    >>> phi47_kernel(0)
    (1+0j)
    >>> abs(phi47_kernel(47)) < abs(phi47_kernel(1))
    True
    """
    if not isinstance(n, (int, np.integer)):
        raise TypeError(f"n must be an integer, got {type(n).__name__}")
    if not isinstance(dim, (int, np.integer)):
        raise TypeError(f"dim must be an integer, got {type(dim).__name__}")
    if n < 0:
        raise ValueError(f"n must be >= 0, got {n}")
    if dim <= 0:
        raise ValueError(f"dim must be > 0, got {dim}")
    if n == 0:
        return complex(1, 0)

    amplitude = ((-1) ** (n % 7)) * (n % 100 + 1)
    phi_decay = PHI ** (-n / dim)
    phase = cmath.exp(2j * math.pi * n / dim)

    return complex(amplitude * phi_decay * phase)


def phi47_kernel_batch(
    n_values: np.ndarray,
    dim: int = N,
) -> np.ndarray:
    """
    Evaluate the synthetic φ⁴⁷ kernel for an array of integers.

    Parameters
    ----------
    n_values:
        Array-like collection of non-negative integer arguments.
    dim:
        Positive lattice dimension.

    Returns
    -------
    numpy.ndarray
        One-dimensional or multidimensional array of ``complex128`` values
        preserving the input shape.

    Raises
    ------
    TypeError
        If ``dim`` is not an integer or the input contains non-integer values.
    ValueError
        If any argument is negative or ``dim`` is not positive.
    """
    if not isinstance(dim, (int, np.integer)):
        raise TypeError(f"dim must be an integer, got {type(dim).__name__}")
    if dim <= 0:
        raise ValueError(f"dim must be > 0, got {dim}")

    raw = np.asarray(n_values)

    if not np.issubdtype(raw.dtype, np.integer):
        raise TypeError("n_values must contain integers")

    n = raw.astype(np.int64, copy=False)

    if np.any(n < 0):
        raise ValueError("n_values must contain only values >= 0")

    amplitude = ((-1.0) ** (n % 7)) * (n % 100 + 1).astype(float)
    phi_decay = PHI ** (-n.astype(float) / dim)
    phase = np.exp(2j * np.pi * n / dim)

    result = np.asarray(amplitude * phi_decay * phase, dtype=np.complex128)
    result = np.where(n == 0, complex(1, 0), result)

    return np.asarray(result, dtype=np.complex128)


def clear_kernel_cache() -> None:
    """Clear the scalar kernel's LRU cache."""
    phi47_kernel.cache_clear()


def kernel_cache_info() -> str:
    """Return scalar-kernel cache statistics."""
    info = phi47_kernel.cache_info()
    return (
        f"φ⁴⁷ kernel cache — hits: {info.hits}, misses: {info.misses}, "
        f"size: {info.currsize}/{info.maxsize}"
    )
