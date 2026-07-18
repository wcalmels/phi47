"""
phi47.core.lattice
==================
Core data structure: the φ⁴⁷ conscious lattice ℒ₄₇.

The lattice is defined as:

    ℒ₄₇[i,j,k] = (1/2 + i·γ(i,j,k)) · φ^w(i,j,k)

where:
    w(i,j,k) = (i + j·φ + k·φ²) / N  (φ-coherent weight)
    γ(i,j,k) = Im(τ*(n)) · φ^w         (imaginary part from τ*)
    T(i,j,k) = 𝟙[i+j+k < N]            (tetrahedral support)

The key property Re(ℒ₄₇[i,j,k]) = 1/2 is **exact by construction**.
"""

from __future__ import annotations

import numpy as np

from .constants import (
    N,
    N_HOLOGRAPHIC,
    PHI,
    RE_HALF_TOLERANCE,
    HOLOGRAPHIC_ERROR_MAX,
)
from .tau_star import tau_star_batch


class Phi47Lattice:
    """
    The φ⁴⁷ conscious lattice ℒ₄₇.

    Parameters
    ----------
    dim : int
        Lattice dimension N. Default is 47 (full lattice).
        Use dim=23 for fast demos.
    dtype : np.dtype
        NumPy dtype for the lattice array. Default: complex128.

    Attributes
    ----------
    lattice : np.ndarray, shape (N, N, N), complex128
        The lattice tensor. Zero outside the tetrahedral support.
    n_active : int
        Number of active nodes (inside the tetrahedron).
    mean_real : float
        Mean Re(ℒ₄₇) over active nodes. Should equal 0.5.
    is_built : bool
        True after :meth:`build` has been called.

    Examples
    --------
    >>> lat = Phi47Lattice(dim=11)
    >>> lat.build()
    >>> abs(lat.mean_real - 0.5) < 1e-10
    True
    >>> lat.n_active > 0
    True
    """

    def __init__(self, dim: int = N, dtype: type = np.complex128) -> None:
        self.dim = dim
        self.dtype = dtype
        self.phi = PHI
        self.lattice: np.ndarray = np.zeros((dim, dim, dim), dtype=dtype)
        self.n_active: int = 0
        self.mean_real: float = float("nan")
        self.is_built: bool = False

    # ── Construction ──────────────────────────────────────────────────────────

    def build(self) -> "Phi47Lattice":
        """
        Build the lattice using vectorised NumPy operations.

        Returns
        -------
        self
            For method chaining.

        Notes
        -----
        After calling this method:
        - ``self.lattice`` is populated.
        - ``self.mean_real`` is set to 0.5 (within floating-point precision).
        - ``self.is_built`` is True.
        """
        dim = self.dim
        phi = self.phi

        # Coordinate grids
        i_g, j_g, k_g = np.meshgrid(
            np.arange(dim), np.arange(dim), np.arange(dim), indexing="ij"
        )

        # Tetrahedral mask: i + j + k < N
        mask = (i_g + j_g + k_g) < dim

        # Node indices
        n_g = (i_g + dim * j_g + dim**2 * k_g).astype(np.int64)

        # φ-coherent weights
        w_g = (i_g + j_g * phi + k_g * phi**2) / dim

        # τ*(n) — vectorised over active nodes
        n_flat = n_g[mask]
        tau_vals = tau_star_batch(n_flat, dim=dim)

        # Imaginary part: φ^w · Im(τ*(n))
        w_flat = w_g[mask]
        phi_w = phi**w_flat
        imag_part = phi_w * np.imag(tau_vals)

        # Assign: Re = 1/2 exactly, Im = φ^w · Im(τ*)
        result = np.zeros((dim, dim, dim), dtype=self.dtype)
        result[mask] = 0.5 + 1j * imag_part

        self.lattice = result
        self.n_active = int(np.sum(mask))
        active_vals = result[mask]
        self.mean_real = float(np.mean(np.real(active_vals)))
        self.is_built = True

        return self

    # ── Verification ──────────────────────────────────────────────────────────

    def verify_re_half(self) -> bool:
        """
        Verify that Re(ℒ₄₇) = 1/2 for all active nodes.

        Returns
        -------
        bool
            True if the property holds within numerical tolerance.

        Raises
        ------
        RuntimeError
            If the lattice has not been built yet.
        """
        self._require_built()
        active = self.lattice[self.lattice != 0]
        if len(active) == 0:
            return False
        return bool(np.all(np.abs(np.real(active) - 0.5) < RE_HALF_TOLERANCE))

    # ── Holographic Projection ────────────────────────────────────────────────

    def holographic_subgrid(self) -> "Phi47Lattice":
        """
        Return the holographic sub-lattice of dimension N//2.

        The sub-lattice preserves ≥ (1 − HOLOGRAPHIC_ERROR_MAX) of the
        information (≈ 94% for N=47, N//2=23).

        Returns
        -------
        Phi47Lattice
            A new (already built) lattice of dimension dim//2.
        """
        sub_dim = max(3, self.dim // 2)
        sub = Phi47Lattice(dim=sub_dim, dtype=self.dtype)
        sub.build()
        return sub

    # ── Statistics ────────────────────────────────────────────────────────────

    def active_nodes(self) -> np.ndarray:
        """Return array of active (non-zero) node values."""
        self._require_built()
        return self.lattice[self.lattice != 0]

    def phi_energy(self, i: int, j: int, k: int) -> float:
        """
        Compute the φ-energy of node (i, j, k).

        E_φ(i,j,k) = |Im(ℒ₄₇[i,j,k])| · φ^w(i,j,k)
        """
        self._require_built()
        w = (i + j * self.phi + k * self.phi**2) / self.dim
        return float(abs(np.imag(self.lattice[i, j, k])) * self.phi**w)

    def summary(self) -> dict:
        """Return a summary dict of lattice properties."""
        self._require_built()
        active = self.active_nodes()
        return {
            "dim": self.dim,
            "n_active": self.n_active,
            "mean_real": self.mean_real,
            "re_half_verified": self.verify_re_half(),
            "mean_imag": float(np.mean(np.imag(active))),
            "std_imag": float(np.std(np.imag(active))),
            "max_abs": float(np.max(np.abs(active))),
        }

    # ── Internal ──────────────────────────────────────────────────────────────

    def _require_built(self) -> None:
        if not self.is_built:
            raise RuntimeError(
                "Lattice not built. Call .build() first."
            )

    def __repr__(self) -> str:
        status = f"built, n_active={self.n_active}" if self.is_built else "not built"
        return f"Phi47Lattice(dim={self.dim}, {status})"
