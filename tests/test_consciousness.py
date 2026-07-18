"""
Tests for phi47.consciousness.phi_measure.
"""

import numpy as np
import pytest

from phi47.core.lattice import Phi47Lattice
from phi47.consciousness.phi_measure import phi_measure, _entropy


# ── Fixtures ───────────────────────────────────────────────────────────────────

@pytest.fixture(scope="module")
def small_lat():
    return Phi47Lattice(dim=7).build()

@pytest.fixture(scope="module")
def medium_lat():
    return Phi47Lattice(dim=11).build()


# ── phi_measure ────────────────────────────────────────────────────────────────

class TestPhiMeasure:

    def test_phi_non_negative_fast(self, small_lat):
        Phi = phi_measure(small_lat, method="fast", n_samples=50, seed=0)
        assert Phi >= 0.0

    def test_phi_non_negative_entropy(self, small_lat):
        Phi = phi_measure(small_lat, method="entropy")
        assert Phi >= 0.0

    def test_phi_non_negative_exact(self, small_lat):
        Phi = phi_measure(small_lat, method="exact")
        assert Phi >= 0.0

    def test_unbuilt_raises(self):
        lat = Phi47Lattice(dim=5)
        with pytest.raises(ValueError):
            phi_measure(lat)

    def test_unknown_method_raises(self, small_lat):
        with pytest.raises(ValueError):
            phi_measure(small_lat, method="unknown")  # type: ignore

    def test_phi_is_float(self, small_lat):
        result = phi_measure(small_lat, method="fast", n_samples=20, seed=1)
        assert isinstance(result, float)

    def test_reproducibility_with_seed(self, small_lat):
        p1 = phi_measure(small_lat, method="fast", n_samples=50, seed=42)
        p2 = phi_measure(small_lat, method="fast", n_samples=50, seed=42)
        assert p1 == p2

    def test_different_seeds_may_differ(self, small_lat):
        p1 = phi_measure(small_lat, method="fast", n_samples=10, seed=0)
        p2 = phi_measure(small_lat, method="fast", n_samples=10, seed=99)
        # Not guaranteed to differ, but usually will
        # We just check both are valid
        assert p1 >= 0.0 and p2 >= 0.0

    def test_larger_lattice_has_phi(self, medium_lat):
        Phi = phi_measure(medium_lat, method="fast", n_samples=50, seed=0)
        assert Phi > 0.0

    def test_subsystem_size_respected(self, medium_lat):
        """Should not crash for various subsystem sizes."""
        for ss in [2, 4, 8, 16]:
            Phi = phi_measure(
                medium_lat, method="fast",
                n_samples=20, subsystem_size=ss, seed=0
            )
            assert Phi >= 0.0

    def test_empty_lattice_returns_zero(self):
        """A lattice with all zeros → Φ = 0."""
        lat = Phi47Lattice(dim=3)
        lat.lattice = np.zeros((3, 3, 3), dtype=complex)
        lat.n_active = 0
        lat.mean_real = float("nan")
        lat.is_built = True
        assert phi_measure(lat, method="fast", n_samples=10) == 0.0


# ── Entropy Helper ─────────────────────────────────────────────────────────────

class TestEntropy:

    def test_uniform_entropy(self):
        p = np.array([0.25, 0.25, 0.25, 0.25])
        assert abs(_entropy(p) - 2.0) < 1e-10   # log2(4) = 2 bits

    def test_zero_entropy(self):
        p = np.array([1.0, 0.0, 0.0])
        assert _entropy(p) == 0.0

    def test_entropy_non_negative(self):
        rng = np.random.default_rng(0)
        for _ in range(10):
            p = rng.random(5)
            p /= p.sum()
            assert _entropy(p) >= 0.0

    def test_empty_returns_zero(self):
        assert _entropy(np.array([])) == 0.0
