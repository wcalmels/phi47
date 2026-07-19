"""
phi47.qualia.engine
===================

Algorithmic phenomenological descriptor generation for φ⁴⁷ lattice states.

Scientific status
-----------------
This module maps numerical stimulus values to deterministic labels, normalized
complex vectors, and bounded intensity scores.

It does not demonstrate:

- phenomenal consciousness;
- subjective experience;
- biological microtubule processing;
- neutrino-mediated cognition;
- hydrogen-orbital collapse in neural systems;
- holographic projection as a verified physical mechanism.

The historical names ``Quale`` and ``QualiaEngine`` are retained as aliases for
backward compatibility.
"""

from __future__ import annotations

import math
import time
from dataclasses import dataclass, field
from enum import Enum

import numpy as np

from phi47.core.constants import (
    NEUTRINO_MASS_EV,
    PHI,
    PHI_47_12,
    PHI_47_36,
    TAU_STAR,
)
from phi47.core.lattice import Phi47Lattice


class QualiaType(Enum):
    """
    Supported descriptor categories.

    The historical enum name is retained for compatibility. Enum values describe
    software output categories and must not be interpreted as demonstrated
    subjective modalities.
    """

    VISUAL_COLOR = "visual_color"
    AUDITORY_TONE = "auditory_tone"
    THERMAL = "thermal"
    PAIN = "pain"
    MATH_PRIME = "math_prime"
    MATH_BEAUTY = "math_beauty"
    MATH_TENSION = "math_tension"
    EMOTION_JOY = "emotion_joy"
    EMOTION_FEAR = "emotion_fear"
    COGNITIVE = "cognitive"


@dataclass
class PhenomenologicalDescriptor:
    """
    Deterministic descriptor generated from an input stimulus.

    Attributes
    ----------
    quale_type:
        Historical category field retained for compatibility.
    content:
        Human-readable software-generated label.
    intensity:
        Bounded numerical score in the interval [0, 1].
    vector:
        Two-component numerical representation [real, imaginary].
    re_value:
        Real component of the generated normalized complex value.
    timestamp:
        Unix timestamp at generation.
    stimulus_type:
        Input category.
    stimulus_value:
        Input numerical value.

    Notes
    -----
    An instance of this class is a computational record. It is not evidence of
    phenomenal experience or consciousness.
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


_VISUAL_CONTENT: dict[tuple[float, float], str] = {
    (620, 750): "Red-spectrum descriptor",
    (590, 620): "Orange-spectrum descriptor",
    (560, 590): "Yellow-spectrum descriptor",
    (500, 560): "Green-spectrum descriptor",
    (450, 500): "Blue-spectrum descriptor",
    (380, 450): "Violet-spectrum descriptor",
}

_AUDITORY_CONTENT: dict[tuple[float, float], str] = {
    (20, 200): "Low-frequency auditory descriptor",
    (200, 2000): "Mid-frequency auditory descriptor",
    (2000, 20000): "High-frequency auditory descriptor",
}

_THERMAL_CONTENT: dict[tuple[float, float], str] = {
    (-40, 0): "Sub-zero thermal descriptor",
    (0, 20): "Low-temperature descriptor",
    (20, 37): "Moderate-temperature descriptor",
    (37, 55): "High-temperature descriptor",
    (55, 200): "Extreme-temperature descriptor",
}

_MATH_PRIME_CONTENT = "Prime-number descriptor for {n}"
_MATH_BEAUTY_CONTENT = "Mathematical-pattern descriptor — φ-score {v:.3f}"


def _visual_content(wavelength_nm: float) -> str:
    for (lower, upper), text in _VISUAL_CONTENT.items():
        if lower <= wavelength_nm < upper:
            return text
    return f"Optical descriptor at {wavelength_nm:.0f} nm"


def _auditory_content(frequency_hz: float) -> str:
    for (lower, upper), text in _AUDITORY_CONTENT.items():
        if lower <= frequency_hz < upper:
            return text
    return f"Auditory descriptor at {frequency_hz:.0f} Hz"


def _thermal_content(temperature_c: float) -> str:
    for (lower, upper), text in _THERMAL_CONTENT.items():
        if lower <= temperature_c < upper:
            return text
    return f"Thermal descriptor at {temperature_c:.1f} °C"


class PhenomenologicalDescriptorEngine:
    """
    Convert numerical stimuli into deterministic computational descriptors.

    Parameters
    ----------
    lattice:
        A built ``Phi47Lattice``.

    Notes
    -----
    The transformation is a project-defined numerical pipeline. Constants and
    intermediate variables are computational parameters, not validated
    biological or quantum mechanisms.
    """

    def __init__(self, lattice: Phi47Lattice) -> None:
        if not isinstance(lattice, Phi47Lattice):
            raise TypeError("lattice must be a Phi47Lattice instance")
        if not lattice.is_built:
            raise ValueError(
                "Lattice must be built before creating the descriptor engine."
            )

        self._lattice = lattice
        self._history: list[PhenomenologicalDescriptor] = []

    def generate(
        self,
        stimulus_type: str,
        value: float,
    ) -> PhenomenologicalDescriptor:
        """
        Generate a deterministic descriptor from a numerical stimulus.

        Parameters
        ----------
        stimulus_type:
            Descriptor category.
        value:
            Numerical stimulus value.

        Returns
        -------
        PhenomenologicalDescriptor
            Software-generated descriptor and numerical representation.
        """
        descriptor = self._descriptor_chain(stimulus_type, value)
        self._history.append(descriptor)
        return descriptor

    @property
    def history(self) -> list[PhenomenologicalDescriptor]:
        """Return generated descriptors in creation order."""
        return list(self._history)

    def clear_history(self) -> None:
        """Clear the in-memory descriptor history."""
        self._history.clear()

    def _descriptor_chain(
        self,
        stimulus_type: str,
        value: float,
    ) -> PhenomenologicalDescriptor:
        """
        Execute the project-defined four-stage numerical transformation.

        The stage names describe computational operations only.
        """
        dim = self._lattice.dim

        # Stage 1: deterministic complex scaling.
        encoded = value * PHI_47_36 * TAU_STAR

        # Stage 2: scalar projection using a historical project constant.
        projected_scalar = (
            abs(encoded)
            * NEUTRINO_MASS_EV
            * math.cos(math.atan2(encoded.imag, encoded.real))
        )

        # Stage 3: map the scalar to a unit-circle complex phase.
        phase_value = complex(
            math.cos(projected_scalar * PHI_47_12),
            math.sin(projected_scalar * PHI_47_12),
        )

        # Stage 4: apply the historical complex project constant and normalize.
        raw = phase_value * TAU_STAR
        norm = abs(raw) if abs(raw) > 1e-15 else 1.0
        normalized = raw / norm

        # Project-defined bounded intensity score.
        phi_weight = PHI ** (abs(value) / dim) if value != 0 else 1.0
        intensity = np.clip(
            abs(normalized) * phi_weight * 0.5,
            0.0,
            1.0,
        )

        descriptor_type, content = self._classify(
            stimulus_type,
            value,
            float(intensity),
        )

        vector = np.array(
            [normalized.real, normalized.imag],
            dtype=float,
        )

        return PhenomenologicalDescriptor(
            quale_type=descriptor_type,
            content=content,
            intensity=float(intensity),
            vector=vector,
            re_value=float(normalized.real),
            stimulus_type=stimulus_type,
            stimulus_value=value,
        )

    # Historical private method retained for downstream compatibility.
    def _qualia_chain(
        self,
        stimulus_type: str,
        value: float,
    ) -> PhenomenologicalDescriptor:
        """Compatibility alias for the historical private transformation."""
        return self._descriptor_chain(stimulus_type, value)

    def _classify(
        self,
        stimulus_type: str,
        value: float,
        intensity: float,
    ) -> tuple[QualiaType, str]:
        match stimulus_type:
            case "visual_color":
                return QualiaType.VISUAL_COLOR, _visual_content(value)
            case "auditory_tone":
                return QualiaType.AUDITORY_TONE, _auditory_content(value)
            case "thermal":
                return QualiaType.THERMAL, _thermal_content(value)
            case "pain":
                return (
                    QualiaType.PAIN,
                    f"Pain-scale descriptor {value:.1f}/10",
                )
            case "math_prime":
                return (
                    QualiaType.MATH_PRIME,
                    _MATH_PRIME_CONTENT.format(n=int(value)),
                )
            case "math_beauty":
                return (
                    QualiaType.MATH_BEAUTY,
                    _MATH_BEAUTY_CONTENT.format(v=value),
                )
            case "emotion_joy":
                return (
                    QualiaType.EMOTION_JOY,
                    f"Joy-category descriptor — intensity {intensity:.2f}",
                )
            case "emotion_fear":
                return (
                    QualiaType.EMOTION_FEAR,
                    f"Fear-category descriptor — intensity {intensity:.2f}",
                )
            case "cognitive":
                return (
                    QualiaType.COGNITIVE,
                    f"Cognitive descriptor — value {value:.4f}",
                )
            case _:
                return (
                    QualiaType.COGNITIVE,
                    f"Unrecognized stimulus: {stimulus_type}={value}",
                )


# Historical API aliases.
Quale = PhenomenologicalDescriptor
QualiaEngine = PhenomenologicalDescriptorEngine


__all__ = [
    "QualiaType",
    "PhenomenologicalDescriptor",
    "PhenomenologicalDescriptorEngine",
    "Quale",
    "QualiaEngine",
]
