"""Tests for the canonical synthetic φ⁴⁷ kernel API."""

import numpy as np
import pytest

from phi47 import (
    phi47_kernel,
    phi47_kernel_batch,
    tau_star,
    tau_star_batch,
)


def test_kernel_identity_at_zero() -> None:
    assert phi47_kernel(0) == complex(1, 0)


def test_kernel_rejects_negative_integer() -> None:
    with pytest.raises(ValueError):
        phi47_kernel(-1)


def test_kernel_rejects_nonpositive_dimension() -> None:
    with pytest.raises(ValueError):
        phi47_kernel(1, dim=0)


def test_kernel_rejects_noninteger_scalar() -> None:
    with pytest.raises(TypeError):
        phi47_kernel(1.5)


def test_batch_matches_scalar_evaluation() -> None:
    arguments = np.arange(0, 100, dtype=np.int64)
    batch = phi47_kernel_batch(arguments)

    expected = np.array(
        [phi47_kernel(int(n)) for n in arguments],
        dtype=np.complex128,
    )

    np.testing.assert_allclose(batch, expected)


def test_batch_preserves_shape() -> None:
    arguments = np.arange(12, dtype=np.int64).reshape(3, 4)
    result = phi47_kernel_batch(arguments)

    assert result.shape == arguments.shape
    assert result.dtype == np.complex128


def test_batch_rejects_negative_values() -> None:
    with pytest.raises(ValueError):
        phi47_kernel_batch(np.array([0, 1, -1], dtype=np.int64))


def test_historical_scalar_alias_is_exact() -> None:
    assert tau_star is phi47_kernel


def test_historical_batch_alias_is_exact() -> None:
    assert tau_star_batch is phi47_kernel_batch


def test_historical_results_are_preserved() -> None:
    arguments = np.arange(50, dtype=np.int64)

    np.testing.assert_allclose(
        tau_star_batch(arguments),
        phi47_kernel_batch(arguments),
    )
