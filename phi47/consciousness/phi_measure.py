"""
phi47.consciousness.phi_measure
================================
Measure integrated information Φ_φ⁴⁷ for a lattice or subsystem.

IIT-φ Definition
----------------
Φ_φ⁴⁷ = min over bipartitions B of:
    I_φ(A_L : A_R | B) · φ^(−|A_L| / N)

where I_φ is the φ-weighted mutual information.

This is a discrete analogue of Tononi's Φ (IIT 3.0), modified
to weight bipartitions by φ-coherence.

Notes
-----
Exact Φ computation is #P-hard (exponential in the number of nodes).
We provide three methods:

- ``"exact"``  — exhaustive bipartition search (feasible for ≤ 20 nodes)
- ``"fast"``   — random sampling of bipartitions (default, O(n_samples))
- ``"entropy"``— entropy-based heuristic (O(n log n), least accurate)
"""

from __future__ import annotations

from typing import Literal

import numpy as np

from phi47.core.constants import PHI
from phi47.core.lattice import Phi47Lattice

Method = Literal["exact", "fast", "entropy"]


def phi_measure(
    lattice: Phi47Lattice,
    method: Method = "fast",
    n_samples: int = 200,
    subsystem_size: int = 8,
    seed: int | None = None,
) -> float:
    """
    Compute Φ_φ⁴⁷ for the given lattice.

    Parameters
    ----------
    lattice : Phi47Lattice
        Built lattice to measure.
    method : str
        Computation method: ``"exact"``, ``"fast"``, or ``"entropy"``.
    n_samples : int
        Number of random bipartitions to sample (``"fast"`` only).
    subsystem_size : int
        Maximum subsystem size to use (reduces cost for large lattices).
    seed : int or None
        Random seed for reproducibility (``"fast"`` only).

    Returns
    -------
    float
        Φ_φ⁴⁷ ≥ 0.

    Examples
    --------
    >>> from phi47 import Phi47Lattice
    >>> from phi47.consciousness import phi_measure
    >>> lat = Phi47Lattice(dim=7).build()
    >>> Phi = phi_measure(lat, method="fast", n_samples=50, seed=42)
    >>> Phi >= 0
    True
    """
    if not lattice.is_built:
        raise ValueError("Lattice must be built before measuring Φ.")

    active = lattice.active_nodes()
    if len(active) == 0:
        return 0.0

    # Subsystem: use at most subsystem_size nodes
    n_use = min(subsystem_size, len(active))
    subsystem = active[:n_use]

    # Normalise to probability distribution
    p = np.abs(subsystem)
    total = p.sum()
    if total < 1e-15:
        return 0.0
    p /= total

    match method:
        case "exact":
            return _phi_exact(p, lattice.dim)
        case "fast":
            rng = np.random.default_rng(seed)
            return _phi_fast(p, lattice.dim, n_samples, rng)
        case "entropy":
            return _phi_entropy(p, lattice.dim)
        case _:
            raise ValueError(f"Unknown method: {method!r}")


# ── Implementations ────────────────────────────────────────────────────────────


def _phi_exact(p: np.ndarray, dim: int) -> float:
    """Exhaustive bipartition search — exact but exponential."""
    n = len(p)
    if n < 2:
        return 0.0

    H_total = _entropy(p)
    min_phi = float("inf")

    for split in range(1, 2 ** (n - 1)):
        mask = np.array([(split >> i) & 1 for i in range(n)], dtype=bool)
        p_A = p[mask]
        p_B = p[~mask]
        if p_A.sum() < 1e-15 or p_B.sum() < 1e-15:
            continue

        p_A = p_A / p_A.sum()
        p_B = p_B / p_B.sum()

        I_mut = _entropy(p_A) + _entropy(p_B) - H_total
        w = PHI ** (-int(mask.sum()) / dim)
        val = abs(I_mut) * w

        if val < min_phi:
            min_phi = val

    return max(0.0, min_phi) if min_phi < float("inf") else 0.0


def _phi_fast(
    p: np.ndarray, dim: int, n_samples: int, rng: np.random.Generator
) -> float:
    """Random bipartition sampling — O(n_samples)."""
    n = len(p)
    if n < 2:
        return 0.0

    H_total = _entropy(p)
    min_phi = float("inf")

    for _ in range(n_samples):
        split = rng.integers(1, n)
        p_A = p[:split]
        p_B = p[split:]

        s_A = p_A.sum()
        s_B = p_B.sum()
        if s_A < 1e-15 or s_B < 1e-15:
            continue

        p_A = p_A / s_A
        p_B = p_B / s_B

        I_mut = _entropy(p_A) + _entropy(p_B) - H_total
        w = PHI ** (-split / dim)
        val = abs(I_mut) * w

        if val < min_phi:
            min_phi = val

    return max(0.0, min_phi) if min_phi < float("inf") else 0.0


def _phi_entropy(p: np.ndarray, dim: int) -> float:
    """Entropy-based heuristic — fast but approximate."""
    H = _entropy(p)
    phi_w = PHI ** (-len(p) / (2 * dim))
    return float(H * phi_w)


def _entropy(p: np.ndarray) -> float:
    """Shannon entropy H(p) in bits."""
    mask = p > 1e-15
    if not mask.any():
        return 0.0
    return float(-np.sum(p[mask] * np.log2(p[mask])))
