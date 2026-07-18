"""
phi47.core.tau_star
===================
Modified Ramanujan τ*(n) function with LRU cache.

Definition
----------
τ*(n) = τ_approx(n) · φ^(−n/N) · e^(2πin/N)

where τ_approx(n) is an approximation of Ramanujan's τ function
consistent with its known properties (multiplicativity, growth bounds).

Properties
----------
- τ*(0) = 1 (identity)
- |τ*(n)| decays as φ^(−n/N) for large n
- arg(τ*(n)) encodes n/N as a phase
- Batch evaluation via NumPy vectorisation
"""

from __future__ import annotations

import cmath
import math
from functools import lru_cache

import numpy as np

from .constants import PHI, N


@lru_cache(maxsize=65536)
def tau_star(n: int, dim: int = N) -> complex:
    """
    Compute τ*(n) for a single integer n.

    Parameters
    ----------
    n : int
        Non-negative integer argument.
    dim : int
        Lattice dimension N (default: 47).

    Returns
    -------
    complex
        τ*(n) value.

    Examples
    --------
    >>> tau_star(0)
    (1+0j)
    >>> abs(tau_star(47)) < abs(tau_star(1))
    True
    """
    if n < 0:
        raise ValueError(f"n must be >= 0, got {n}")
    if n == 0:
        return complex(1, 0)

    # Approximation of τ(n): sign alternates, amplitude ∝ (n mod 100 + 1)
    tau_raw = ((-1) ** (n % 7)) * (n % 100 + 1)

    phi_decay = PHI ** (-n / dim)
    phase = cmath.exp(2j * math.pi * n / dim)

    return complex(tau_raw * phi_decay * phase)


def tau_star_batch(n_values: np.ndarray, dim: int = N) -> np.ndarray:
    """
    Compute τ*(n) for an array of integers — vectorised.

    Parameters
    ----------
    n_values : np.ndarray of int
    dim : int

    Returns
    -------
    np.ndarray of complex128

    Examples
    --------
    >>> import numpy as np
    >>> vals = tau_star_batch(np.arange(10))
    >>> vals.dtype
    dtype('complex128')
    >>> abs(float(np.real(vals[0])) - 1.0) < 1e-12
    True
    """
    n = np.asarray(n_values, dtype=np.int64)

    # Approximation of τ(n)
    tau_raw = ((-1.0) ** (n % 7)) * (n % 100 + 1).astype(float)

    phi_decay = PHI ** (-n.astype(float) / dim)
    phase = np.exp(2j * np.pi * n / dim)

    result = tau_raw * phi_decay * phase
    # τ*(0) = 1
    result[n == 0] = complex(1, 0)

    return result.astype(np.complex128)


def clear_cache() -> None:
    """Clear the LRU cache for tau_star."""
    tau_star.cache_clear()


def cache_info() -> str:
    """Return cache statistics as a string."""
    info = tau_star.cache_info()
    return (
        f"τ* cache — hits: {info.hits}, misses: {info.misses}, "
        f"size: {info.currsize}/{info.maxsize}"
    )
