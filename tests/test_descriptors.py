"""Tests for the neutral phenomenological descriptor API."""

import numpy as np
import pytest

from phi47 import (
    PhenomenologicalDescriptor,
    PhenomenologicalDescriptorEngine,
    Phi47Lattice,
    Quale,
    QualiaEngine,
)


@pytest.fixture
def built_lattice() -> Phi47Lattice:
    return Phi47Lattice(dim=11).build()


def test_historical_descriptor_alias() -> None:
    assert Quale is PhenomenologicalDescriptor


def test_historical_engine_alias() -> None:
    assert QualiaEngine is PhenomenologicalDescriptorEngine


def test_generate_returns_descriptor(
    built_lattice: Phi47Lattice,
) -> None:
    engine = PhenomenologicalDescriptorEngine(built_lattice)
    descriptor = engine.generate("visual_color", 700.0)

    assert isinstance(descriptor, PhenomenologicalDescriptor)
    assert 0.0 <= descriptor.intensity <= 1.0
    assert descriptor.vector.shape == (2,)
    assert np.isfinite(descriptor.vector).all()


def test_history_returns_copy(
    built_lattice: Phi47Lattice,
) -> None:
    engine = PhenomenologicalDescriptorEngine(built_lattice)
    engine.generate("cognitive", 47.0)

    history = engine.history
    history.clear()

    assert len(engine.history) == 1


def test_clear_history(
    built_lattice: Phi47Lattice,
) -> None:
    engine = PhenomenologicalDescriptorEngine(built_lattice)
    engine.generate("thermal", 25.0)
    engine.clear_history()

    assert engine.history == []


def test_unbuilt_lattice_is_rejected() -> None:
    lattice = Phi47Lattice(dim=7)

    with pytest.raises(ValueError):
        PhenomenologicalDescriptorEngine(lattice)


def test_non_lattice_is_rejected() -> None:
    with pytest.raises(TypeError):
        PhenomenologicalDescriptorEngine(object())  # type: ignore[arg-type]


def test_historical_private_chain_is_preserved(
    built_lattice: Phi47Lattice,
) -> None:
    engine = PhenomenologicalDescriptorEngine(built_lattice)

    first = engine._descriptor_chain("cognitive", 2.0)
    second = engine._qualia_chain("cognitive", 2.0)

    assert first.content == second.content
    assert first.intensity == second.intensity
    np.testing.assert_allclose(first.vector, second.vector)


def test_descriptor_serialization(
    built_lattice: Phi47Lattice,
) -> None:
    engine = PhenomenologicalDescriptorEngine(built_lattice)
    descriptor = engine.generate("math_prime", 47.0)

    serialized = descriptor.to_dict()

    assert serialized["type"] == "math_prime"
    assert serialized["stimulus_value"] == 47.0
