"""
Algorithmic descriptor generation.

The package name ``qualia`` is retained for backward compatibility. Outputs are
deterministic computational descriptors and must not be interpreted as
demonstrated subjective experiences.
"""

from phi47.qualia.engine import (
    PhenomenologicalDescriptor,
    PhenomenologicalDescriptorEngine,
    Quale,
    QualiaEngine,
    QualiaType,
)

__all__ = [
    "PhenomenologicalDescriptor",
    "PhenomenologicalDescriptorEngine",
    "Quale",
    "QualiaEngine",
    "QualiaType",
]
