"""
Tests for phi47.core.lattice — the central Re=1/2 property and core invariants.
"""

import numpy as np
import pytest

from phi47.core.lattice import Phi47Lattice
from phi47.core.constants import PHI, RE_HALF_TOLERANCE


# ── Fixtures ───────────────────────────────────────────────────────────────────

@pytest.fixture(scope="module")
def small_lattice():
    """dim=7 lattice — fast for unit tests."""
    return Phi47Lattice(dim=7).build()


@pytest.fixture(scope="module")
def medium_lattice():
    """dim=11 lattice."""
    return Phi47Lattice(dim=11).build()


# ── Construction ───────────────────────────────────────────────────────────────

class TestConstruction:

    def test_build_returns_self(self):
        lat = Phi47Lattice(dim=5)
        result = lat.build()
        assert result is lat

    def test_is_built_flag(self):
        lat = Phi47Lattice(dim=5)
        assert not lat.is_built
        lat.build()
        assert lat.is_built

    def test_shape(self):
        lat = Phi47Lattice(dim=7).build()
        assert lat.lattice.shape == (7, 7, 7)

    def test_n_active_positive(self, small_lattice):
        assert small_lattice.n_active > 0

    def test_tetrahedral_count(self):
        """Active nodes should be C(N+2, 3) = N(N+1)(N+2)/6."""
        for dim in [5, 7, 11]:
            lat = Phi47Lattice(dim=dim).build()
            expected = dim * (dim + 1) * (dim + 2) // 6
            assert lat.n_active == expected, \
                f"dim={dim}: expected {expected}, got {lat.n_active}"

    def test_inactive_nodes_are_zero(self, small_lattice):
        dim = small_lattice.dim
        for i in range(dim):
            for j in range(dim):
                for k in range(dim):
                    if i + j + k >= dim:
                        assert small_lattice.lattice[i, j, k] == 0.0 + 0.0j


# ── The Central Property: Re = 1/2 ────────────────────────────────────────────

class TestRealPartHalf:
    """
    The most important invariant of the framework.
    Every active node must have Re = 0.5 exactly.
    """

    @pytest.mark.parametrize("dim", [5, 7, 11, 13, 17, 23])
    def test_re_half_for_all_dims(self, dim):
        lat = Phi47Lattice(dim=dim).build()
        active = lat.active_nodes()
        assert len(active) > 0
        re_vals = np.real(active)
        np.testing.assert_allclose(
            re_vals, 0.5,
            atol=RE_HALF_TOLERANCE,
            err_msg=f"Re ≠ 1/2 for dim={dim}"
        )

    def test_mean_real_attribute(self, small_lattice):
        assert abs(small_lattice.mean_real - 0.5) < RE_HALF_TOLERANCE

    def test_verify_re_half_method(self, small_lattice):
        assert small_lattice.verify_re_half() is True

    def test_re_half_after_full_n47(self):
        """Verify the property for the canonical N=47 lattice."""
        lat = Phi47Lattice(dim=47).build()
        assert lat.verify_re_half(), "Re=1/2 failed for N=47"
        assert abs(lat.mean_real - 0.5) < RE_HALF_TOLERANCE


# ── Holographic Sub-grid ───────────────────────────────────────────────────────

class TestHolography:

    def test_subgrid_dim_is_half(self, medium_lattice):
        sub = medium_lattice.holographic_subgrid()
        assert sub.dim == medium_lattice.dim // 2

    def test_subgrid_inherits_re_half(self, medium_lattice):
        sub = medium_lattice.holographic_subgrid()
        assert sub.verify_re_half()

    def test_subgrid_fewer_nodes(self, medium_lattice):
        sub = medium_lattice.holographic_subgrid()
        assert sub.n_active < medium_lattice.n_active


# ── Summary & Energy ──────────────────────────────────────────────────────────

class TestSummaryAndEnergy:

    def test_summary_keys(self, small_lattice):
        s = small_lattice.summary()
        for key in ["dim", "n_active", "mean_real", "re_half_verified"]:
            assert key in s

    def test_phi_energy_non_negative(self, small_lattice):
        dim = small_lattice.dim
        for i in range(dim):
            if i < dim - 2:
                energy = small_lattice.phi_energy(i, 0, 0)
                assert energy >= 0.0

    def test_require_built_raises(self):
        lat = Phi47Lattice(dim=5)
        with pytest.raises(RuntimeError, match="not built"):
            lat.verify_re_half()


# ── Reproducibility ────────────────────────────────────────────────────────────

class TestReproducibility:

    def test_two_builds_identical(self):
        lat1 = Phi47Lattice(dim=7).build()
        lat2 = Phi47Lattice(dim=7).build()
        np.testing.assert_array_equal(lat1.lattice, lat2.lattice)

    def test_complex_dtype(self, small_lattice):
        assert np.iscomplexobj(small_lattice.lattice)
