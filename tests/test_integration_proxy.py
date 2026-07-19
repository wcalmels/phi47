"""Tests for the canonical information-integration proxy API."""

import numpy as np
import pytest

from phi47 import (
    Phi47Lattice,
    integration_proxy,
    phi_measure,
)


@pytest.fixture
def built_lattice() -> Phi47Lattice:
    return Phi47Lattice(dim=7).build()


def test_historical_name_is_exact_alias() -> None:
    assert phi_measure is integration_proxy


def test_proxy_returns_nonnegative_value(
    built_lattice: Phi47Lattice,
) -> None:
    score = integration_proxy(
        built_lattice,
        method="fast",
        n_samples=20,
        seed=42,
    )

    assert isinstance(score, float)
    assert score >= 0.0


def test_fast_method_is_reproducible(
    built_lattice: Phi47Lattice,
) -> None:
    first = integration_proxy(
        built_lattice,
        method="fast",
        n_samples=20,
        seed=47,
    )
    second = integration_proxy(
        built_lattice,
        method="fast",
        n_samples=20,
        seed=47,
    )

    assert first == second


def test_all_methods_return_finite_values(
    built_lattice: Phi47Lattice,
) -> None:
    for method in ("exact", "fast", "entropy"):
        score = integration_proxy(
            built_lattice,
            method=method,
            n_samples=10,
            subsystem_size=5,
            seed=47,
        )

        assert np.isfinite(score)
        assert score >= 0.0


def test_unbuilt_lattice_is_rejected() -> None:
    lattice = Phi47Lattice(dim=7)

    with pytest.raises(ValueError):
        integration_proxy(lattice)


def test_invalid_method_is_rejected(
    built_lattice: Phi47Lattice,
) -> None:
    with pytest.raises(ValueError):
        integration_proxy(built_lattice, method="invalid")  # type: ignore[arg-type]


def test_nonpositive_sample_count_is_rejected(
    built_lattice: Phi47Lattice,
) -> None:
    with pytest.raises(ValueError):
        integration_proxy(built_lattice, n_samples=0)


def test_nonpositive_subsystem_size_is_rejected(
    built_lattice: Phi47Lattice,
) -> None:
    with pytest.raises(ValueError):
        integration_proxy(built_lattice, subsystem_size=0)
