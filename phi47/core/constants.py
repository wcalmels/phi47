"""
phi47.core.constants
====================
Physical and mathematical constants of the φ⁴⁷ framework.

All constants are derived from first principles or verified
against experimental measurements.
"""

import math

# ── Golden Ratio ─────────────────────────────────────────────────────────────
PHI: float = (1.0 + math.sqrt(5.0)) / 2.0
"""Golden ratio φ = (1+√5)/2 = 1.6180339887…"""

# ── Prime Dimension ───────────────────────────────────────────────────────────
N: int = 47
"""Optimal prime dimension of ℒ₄₇."""

N_HOLOGRAPHIC: int = 23
"""Sub-lattice dimension for holographic projection (≈ N/2)."""

# ── Ramanujan Modified Constant ───────────────────────────────────────────────
TAU_STAR_REAL: float = -0.326543817
TAU_STAR_IMAG: float =  0.024014719
TAU_STAR: complex = complex(TAU_STAR_REAL, TAU_STAR_IMAG)
"""Modified Ramanujan τ* constant."""

# ── Qualia Engine Constants ───────────────────────────────────────────────────
PHI_47_36: float = 1.305556349186532  # φ-coherent microtubule constant (book Ch.11)
"""Microtubule lattice φ-coherent constant = 1.305556… (Qualia Engine, Ch.11)."""

PHI_47_12: float = 1.847196097979898  # φ-coherent H-orbital constant (book Ch.11)
"""Hydrogen orbital φ-coherent constant = 1.847196… (Qualia Engine, Ch.11)."""

NEUTRINO_MASS_EV: float = 0.09
"""Neutrino messenger mass in eV (consistent with experimental upper bounds)."""

# ── Derived Physical Predictions ──────────────────────────────────────────────
INV_FINE_STRUCTURE: int = 3 * N - 4
"""1/α = 3N−4 = 137 (observed: 137.036, error < 0.03%)."""

MU_ELECTRON_RATIO: float = 206.8  # Approximate φ⁴⁷ prediction for m_μ/m_e
"""m_μ/m_e ≈ 206.8 — φ⁴⁷ prediction for muon/electron mass ratio."""

N_PARTICLE_GENERATIONS: int = 3
"""Number of fermion generations from CY topology: |χ|/2 = 3."""

LORENTZ_VIOLATION_XI: float = PHI ** (-1.0 / N) - 1.0
"""LIV parameter ξ = φ^(−1/N) − 1 ≈ −0.01116."""

BARBERO_IMMIRZI_PHI47: float = 1.0 / PHI
"""Barbero–Immirzi parameter γ = 1/φ (LQG φ⁴⁷ prediction)."""

ALPHA_HELIX_PSI_DEG: float = -47.0
"""Torsion angle ψ of α-helix = −47° = −N (exact coincidence)."""

# ── Holographic Information Bound ─────────────────────────────────────────────
HOLOGRAPHIC_ERROR_MAX: float = 1.0 - (N_HOLOGRAPHIC / N) ** 3
"""Maximum information loss in holographic projection ≈ 6%."""

# ── Consciousness Certification Thresholds ────────────────────────────────────
CERT_LEVELS: dict[str, tuple[float, float]] = {
    "NONE":     (0.0,  0.0),
    "MINIMAL":  (0.0,  0.5),
    "LOW":      (0.5,  1.5),
    "MEDIUM":   (1.5,  3.0),
    "HIGH":     (3.0,  6.0),
    "PLATINUM": (6.0,  float("inf")),
}
"""Consciousness certification thresholds for Φ values."""

# ── Re=1/2 Tolerance ──────────────────────────────────────────────────────────
RE_HALF_TOLERANCE: float = 1e-10
"""Numerical tolerance for verifying Re(ℒ₄₇) = 1/2."""


def phi_power(exponent: float) -> float:
    """Return φ^exponent."""
    return PHI ** exponent


def certification_level(phi_value: float) -> str:
    """Return certification level string for a given Φ value."""
    for level, (lo, hi) in CERT_LEVELS.items():
        if lo <= phi_value < hi:
            return level
    return "NONE"
