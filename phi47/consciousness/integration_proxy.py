"""
phi47.consciousness.integration_proxy
=====================================

Project-defined information-integration proxy for φ⁴⁷ lattice states.

Scientific status
-----------------
This module computes an exploratory entropy-based score over a finite subset of
active lattice values and selected bipartitions.

The score is not:

- a validated measurement of consciousness;
- a neurological or clinical diagnostic;
- a complete implementation of Integrated Information Theory;
- evidence that a software system has phenomenal experience.

The term ``integration_proxy`` is the canonical public name.
"""

from __future__ import annotations

from typing import Literal

import numpy as np

from phi47.core.constants import PHI
from phi47.core.lattice import Phi47Lattice

Method = Literal["exact", "fast", "entropy"]


def integration_proxy(
    lattice: Phi47Lattice,
    method: Method = "fast",
    n_samples: int = 200,
    subsystem_size: int = 8,
    seed: int | None = None,
) -> float:
    """
    Compute the project-defined information-integration proxy.

    Parameters
    ----------
    lattice:
        A previously built ``Phi47Lattice``.
    method:
        ``"exact"``, ``"fast"``, or ``"entropy"``.
    n_samples:
        Number of sampled contiguous partitions for the ``"fast"`` method.
    subsystem_size:
        Maximum number of active values included in the calculation.
    seed:
        Random seed retained for API reproducibility.

    Returns
    -------
    float
        A non-negative project-defined integration score.

    Notes
    -----
    Despite the historical use of the symbol Φ, this computation is not a
    validated implementation of IIT Φ.

    The ``"exact"`` method enumerates binary masks over the selected values.
    The ``"fast"`` method evaluates sampled contiguous split positions.
    The ``"entropy"`` method returns a weighted Shannon-entropy heuristic.
    """
    if not isinstance(lattice, Phi47Lattice):
        raise TypeError("lattice must be a Phi47Lattice instance")

    if not lattice.is_built:
        raise ValueError(
            "Lattice must be built before calculating the integration proxy."
        )

    if not isinstance(n_samples, (int, np.integer)):
        raise TypeError("n_samples must be an integer")
    if not isinstance(subsystem_size, (int, np.integer)):
        raise TypeError("subsystem_size must be an integer")
    if n_samples <= 0:
        raise ValueError("n_samples must be greater than zero")
    if subsystem_size <= 0:
        raise ValueError("subsystem_size must be greater than zero")

    active = lattice.active_nodes()
    if len(active) == 0:
        return 0.0

    n_use = min(int(subsystem_size), len(active))
    subsystem = active[:n_use]

    probabilities = np.abs(subsystem).astype(float)
    total = probabilities.sum()

    if total < 1e-15:
        return 0.0

    probabilities /= total

    match method:
        case "exact":
            return _integration_exact(probabilities, lattice.dim)
        case "fast":
            rng = np.random.default_rng(seed)
            return _integration_fast(
                probabilities,
                lattice.dim,
                int(n_samples),
                rng,
            )
        case "entropy":
            return _integration_entropy(probabilities, lattice.dim)
        case _:
            raise ValueError(f"Unknown method: {method!r}")


def _integration_exact(probabilities: np.ndarray, dim: int) -> float:
    """Enumerate binary masks over the selected subsystem."""
    n = len(probabilities)
    if n < 2:
        return 0.0

    total_entropy = _entropy(probabilities)
    minimum_score = float("inf")

    for split in range(1, 2 ** (n - 1)):
        mask = np.array(
            [(split >> index) & 1 for index in range(n)],
            dtype=bool,
        )

        left = probabilities[mask]
        right = probabilities[~mask]

        if left.sum() < 1e-15 or right.sum() < 1e-15:
            continue

        left = left / left.sum()
        right = right / right.sum()

        entropy_difference = _entropy(left) + _entropy(right) - total_entropy

        weight = PHI ** (-int(mask.sum()) / dim)
        score = abs(entropy_difference) * weight

        if score < minimum_score:
            minimum_score = score

    if minimum_score == float("inf"):
        return 0.0

    return max(0.0, float(minimum_score))


def _integration_fast(
    probabilities: np.ndarray,
    dim: int,
    n_samples: int,
    rng: np.random.Generator,
) -> float:
    """
    Evaluate sampled contiguous split positions.

    This method does not sample arbitrary bipartitions. It samples split indices
    that divide the selected vector into a left and right contiguous segment.
    """
    n = len(probabilities)
    if n < 2:
        return 0.0

    total_entropy = _entropy(probabilities)
    minimum_score = float("inf")

    for _ in range(n_samples):
        split = int(rng.integers(1, n))

        left = probabilities[:split]
        right = probabilities[split:]

        left_sum = left.sum()
        right_sum = right.sum()

        if left_sum < 1e-15 or right_sum < 1e-15:
            continue

        left = left / left_sum
        right = right / right_sum

        entropy_difference = _entropy(left) + _entropy(right) - total_entropy

        weight = PHI ** (-split / dim)
        score = abs(entropy_difference) * weight

        if score < minimum_score:
            minimum_score = score

    if minimum_score == float("inf"):
        return 0.0

    return max(0.0, float(minimum_score))


def _integration_entropy(
    probabilities: np.ndarray,
    dim: int,
) -> float:
    """Return a golden-ratio-weighted Shannon-entropy heuristic."""
    entropy = _entropy(probabilities)
    weight = PHI ** (-len(probabilities) / (2 * dim))
    return float(entropy * weight)


def _entropy(probabilities: np.ndarray) -> float:
    """Calculate Shannon entropy in bits."""
    mask = probabilities > 1e-15

    if not mask.any():
        return 0.0

    values = probabilities[mask]
    return float(-np.sum(values * np.log2(values)))


__all__ = ["Method", "integration_proxy"]
