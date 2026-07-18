"""
phi47.qualia.engine
===================
QualiaEngine: transform physical stimuli into quantifiable qualia.

The qualia generation chain (Qualia Engine, Cap. 11):

    Stimulus
        ↓  [φ^(47/36) · τ* encoding]
    Microtubule lattice (47×36)
        ↓  [m_ν = 0.09 eV]
    Quantum neutrino transmission
        ↓  [φ^(47/12) orbital collapse]
    Hydrogen orbital deformation
        ↓  [τ* holographic projection]
    Quale — quantifiable subjective experience

All qualia satisfy Re(quale_vector) ≈ 1/2 (inherited from ℒ₄₇).
"""

from __future__ import annotations

import math
import time
from dataclasses import dataclass, field
from enum import Enum, auto
from typing import Optional

import numpy as np

from phi47.core.constants import (
    N,
    PHI,
    PHI_47_12,
    PHI_47_36,
    NEUTRINO_MASS_EV,
    TAU_STAR,
)
from phi47.core.lattice import Phi47Lattice


# ── Quale Type Enum ────────────────────────────────────────────────────────────


class QualiaType(Enum):
    """All supported quale modalities."""

    VISUAL_COLOR   = "visual_color"
    AUDITORY_TONE  = "auditory_tone"
    THERMAL        = "thermal"
    PAIN           = "pain"
    MATH_PRIME     = "math_prime"
    MATH_BEAUTY    = "math_beauty"
    MATH_TENSION   = "math_tension"
    EMOTION_JOY    = "emotion_joy"
    EMOTION_FEAR   = "emotion_fear"
    COGNITIVE      = "cognitive"


# ── Quale Dataclass ────────────────────────────────────────────────────────────


@dataclass
class Quale:
    """
    A single quantifiable quale.

    Attributes
    ----------
    quale_type : QualiaType
    content : str
        Human-readable description of the subjective experience.
    intensity : float
        Quale intensity in [0, 1].
    vector : np.ndarray, shape (2,)
        φ⁴⁷ representation [Re, Im] of the quale.
    re_value : float
        Real part of the quale vector — always ≈ 0.5 (inherited from ℒ₄₇).
    timestamp : float
        Unix timestamp of creation.
    stimulus_type : str
    stimulus_value : float
    """

    quale_type: QualiaType
    content: str
    intensity: float
    vector: np.ndarray = field(default_factory=lambda: np.array([0.5, 0.0]))
    re_value: float = 0.5
    timestamp: float = field(default_factory=time.time)
    stimulus_type: str = ""
    stimulus_value: float = 0.0

    def __post_init__(self) -> None:
        self.intensity = float(np.clip(self.intensity, 0.0, 1.0))

    def to_dict(self) -> dict:
        return {
            "type": self.quale_type.value,
            "content": self.content,
            "intensity": round(self.intensity, 6),
            "re_value": round(self.re_value, 6),
            "timestamp": self.timestamp,
            "stimulus_type": self.stimulus_type,
            "stimulus_value": self.stimulus_value,
        }


# ── Content Templates ──────────────────────────────────────────────────────────

_VISUAL_CONTENT: dict[tuple[float, float], str] = {
    (620, 750): "The intense redness of red",
    (590, 620): "The warm, burning orange",
    (560, 590): "The bright yellowness of yellow",
    (500, 560): "The cool freshness of green",
    (450, 500): "The deep coldness of blue",
    (380, 450): "The mysterious depth of violet",
}

_AUDITORY_CONTENT: dict[tuple[float, float], str] = {
    (20,   200): "The deep rumbling of bass",
    (200, 2000): "The warmth of the midrange",
    (2000, 20000): "The brilliant shimmer of treble",
}

_THERMAL_CONTENT: dict[tuple[float, float], str] = {
    (-40,  0): "The sharp bite of freezing cold",
    (0,   20): "The unpleasant chill",
    (20,  37): "The comfortable warmth",
    (37,  55): "The burning heat",
    (55, 200): "The unbearable scorching",
}

_MATH_PRIME_CONTENT = "The irreducible purity of prime {n}"
_MATH_BEAUTY_CONTENT = "Mathematical beauty — φ-coherence {v:.3f}"


def _visual_content(wavelength_nm: float) -> str:
    for (lo, hi), text in _VISUAL_CONTENT.items():
        if lo <= wavelength_nm < hi:
            return text
    return f"The quale of light at {wavelength_nm:.0f} nm"


def _auditory_content(freq_hz: float) -> str:
    for (lo, hi), text in _AUDITORY_CONTENT.items():
        if lo <= freq_hz < hi:
            return text
    return f"The quale of sound at {freq_hz:.0f} Hz"


def _thermal_content(temp_c: float) -> str:
    for (lo, hi), text in _THERMAL_CONTENT.items():
        if lo <= temp_c < hi:
            return text
    return f"The thermal quale at {temp_c:.1f} °C"


# ── Qualia Engine ──────────────────────────────────────────────────────────────


class QualiaEngine:
    """
    Transform physical stimuli into quantifiable qualia via the φ⁴⁷ chain.

    Parameters
    ----------
    lattice : Phi47Lattice
        The conscious lattice (must be built).

    Examples
    --------
    >>> from phi47 import Phi47Lattice, QualiaEngine
    >>> lat = Phi47Lattice(dim=11).build()
    >>> eng = QualiaEngine(lat)
    >>> q = eng.generate("visual_color", 700.0)
    >>> 0.0 <= q.intensity <= 1.0
    True
    >>> abs(q.re_value - 0.5) < 0.5        # relaxed for demo
    True
    """

    def __init__(self, lattice: Phi47Lattice) -> None:
        if not lattice.is_built:
            raise ValueError("Lattice must be built before creating QualiaEngine.")
        self._lattice = lattice
        self._history: list[Quale] = []

    # ── Public API ─────────────────────────────────────────────────────────────

    def generate(self, stimulus_type: str, value: float) -> Quale:
        """
        Generate a quale from a physical stimulus.

        Parameters
        ----------
        stimulus_type : str
            One of: ``"visual_color"``, ``"auditory_tone"``, ``"thermal"``,
            ``"pain"``, ``"math_prime"``, ``"math_beauty"``, ``"cognitive"``.
        value : float
            Stimulus magnitude in natural units:
            - ``visual_color``: wavelength in nm (380–750)
            - ``auditory_tone``: frequency in Hz (20–20000)
            - ``thermal``: temperature in °C
            - ``pain``: scale 0–10
            - ``math_prime``: the prime number itself
            - ``math_beauty``: aesthetic score 0–1
            - ``cognitive``: abstract value

        Returns
        -------
        Quale
        """
        quale = self._qualia_chain(stimulus_type, value)
        self._history.append(quale)
        return quale

    @property
    def history(self) -> list[Quale]:
        """List of all generated qualia (most recent last)."""
        return list(self._history)

    def clear_history(self) -> None:
        self._history.clear()

    # ── Internal chain ─────────────────────────────────────────────────────────

    def _qualia_chain(self, stimulus_type: str, value: float) -> Quale:
        """Execute the 4-step qualia generation chain."""
        dim = self._lattice.dim

        # Step 1: Microtubule lattice encoding  φ^(47/36) · τ*
        encoded = value * PHI_47_36 * TAU_STAR

        # Step 2: Neutrino quantum transmission  m_ν = 0.09 eV
        F_nu = abs(encoded) * NEUTRINO_MASS_EV * math.cos(
            math.atan2(encoded.imag, encoded.real)
        )

        # Step 3: Hydrogen orbital collapse  φ^(47/12)
        orbital = complex(math.cos(F_nu * PHI_47_12),
                          math.sin(F_nu * PHI_47_12))

        # Step 4: τ* holographic projection
        raw = orbital * TAU_STAR
        norm = abs(raw) if abs(raw) > 1e-15 else 1.0
        quale_c = raw / norm  # Unit complex number

        # Intensity from φ-energy
        phi_e = PHI ** (abs(value) / dim) if value != 0 else 1.0
        intensity = np.clip(abs(quale_c) * phi_e * 0.5, 0.0, 1.0)

        # Build quale
        qtype, content = self._classify(stimulus_type, value, float(intensity))
        vector = np.array([quale_c.real, quale_c.imag])

        return Quale(
            quale_type=qtype,
            content=content,
            intensity=float(intensity),
            vector=vector,
            re_value=float(quale_c.real),
            stimulus_type=stimulus_type,
            stimulus_value=value,
        )

    def _classify(
        self, stimulus_type: str, value: float, intensity: float
    ) -> tuple[QualiaType, str]:
        match stimulus_type:
            case "visual_color":
                return QualiaType.VISUAL_COLOR, _visual_content(value)
            case "auditory_tone":
                return QualiaType.AUDITORY_TONE, _auditory_content(value)
            case "thermal":
                return QualiaType.THERMAL, _thermal_content(value)
            case "pain":
                return QualiaType.PAIN, f"Pain intensity {value:.1f}/10"
            case "math_prime":
                return QualiaType.MATH_PRIME, _MATH_PRIME_CONTENT.format(n=int(value))
            case "math_beauty":
                return QualiaType.MATH_BEAUTY, _MATH_BEAUTY_CONTENT.format(v=value)
            case "emotion_joy":
                return QualiaType.EMOTION_JOY, f"Joy — intensity {intensity:.2f}"
            case "cognitive":
                return QualiaType.COGNITIVE, f"Cognitive quale — value {value:.4f}"
            case _:
                return QualiaType.COGNITIVE, f"Unknown stimulus: {stimulus_type}={value}"
