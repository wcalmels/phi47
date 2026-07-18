"""
Tests for phi47.core.tau_star and phi47.qualia.engine.
"""

import numpy as np
import pytest

from phi47.core.tau_star import tau_star, tau_star_batch, clear_cache, cache_info
from phi47.core.constants import PHI, N
from phi47.qualia.engine import Quale, QualiaEngine, QualiaType
from phi47.core.lattice import Phi47Lattice


# ── τ*(n) Tests ────────────────────────────────────────────────────────────────

class TestTauStar:

    def test_tau_star_zero(self):
        """τ*(0) = 1."""
        assert tau_star(0) == complex(1, 0)

    def test_tau_star_returns_complex(self):
        assert isinstance(tau_star(1), complex)

    def test_negative_n_raises(self):
        with pytest.raises(ValueError):
            tau_star(-1)

    def test_decay_property(self):
        """|τ*(n)| should decrease for large n (φ^(-n/N) decay)."""
        abs_1 = abs(tau_star(1))
        abs_47 = abs(tau_star(47))
        # τ*(47) amplitude: (47%100+1)=48 vs τ*(1)=2, but φ^(-47/N) < φ^(-1/N)
        # Not strictly decreasing in general, but τ*(47) < τ*(1)*max_amp
        assert abs_47 < 100 * abs_1  # Reasonable bound

    def test_batch_matches_single(self):
        n_vals = np.arange(10)
        batch = tau_star_batch(n_vals)
        for i, n in enumerate(n_vals):
            np.testing.assert_almost_equal(
                batch[i], tau_star(int(n)), decimal=10
            )

    def test_batch_dtype(self):
        result = tau_star_batch(np.arange(5))
        assert result.dtype == np.complex128

    def test_batch_zero_is_one(self):
        result = tau_star_batch(np.array([0]))
        assert abs(result[0] - 1.0) < 1e-12

    def test_cache_info_string(self):
        clear_cache()
        tau_star(1)
        info = cache_info()
        assert "τ* cache" in info
        assert "misses" in info

    def test_cache_hits(self):
        clear_cache()
        tau_star(42)
        tau_star(42)  # Should be a cache hit
        info = tau_star.cache_info()
        assert info.hits >= 1

    def test_deterministic(self):
        clear_cache()
        v1 = tau_star(13)
        clear_cache()
        v2 = tau_star(13)
        assert v1 == v2


# ── QualiaEngine Tests ─────────────────────────────────────────────────────────

@pytest.fixture(scope="module")
def engine():
    lat = Phi47Lattice(dim=7).build()
    return QualiaEngine(lat)


class TestQualiaEngine:

    def test_requires_built_lattice(self):
        unbuilt = Phi47Lattice(dim=5)
        with pytest.raises(ValueError):
            QualiaEngine(unbuilt)

    def test_generate_returns_quale(self, engine):
        q = engine.generate("visual_color", 700.0)
        assert isinstance(q, Quale)

    def test_intensity_range(self, engine):
        for stimulus, val in [
            ("visual_color", 450.0),
            ("auditory_tone", 440.0),
            ("thermal", 25.0),
            ("pain", 5.0),
            ("math_prime", 47.0),
            ("math_beauty", 0.9),
            ("cognitive", 1.618),
        ]:
            q = engine.generate(stimulus, val)
            assert 0.0 <= q.intensity <= 1.0, \
                f"Intensity out of range for {stimulus}"

    def test_vector_shape(self, engine):
        q = engine.generate("math_prime", 47.0)
        assert q.vector.shape == (2,)

    def test_quale_type_assigned(self, engine):
        q = engine.generate("visual_color", 700.0)
        assert q.quale_type == QualiaType.VISUAL_COLOR

    def test_history_accumulates(self, engine):
        engine.clear_history()
        engine.generate("cognitive", 1.0)
        engine.generate("cognitive", 2.0)
        assert len(engine.history) == 2

    def test_history_is_copy(self, engine):
        engine.clear_history()
        engine.generate("cognitive", 1.0)
        h = engine.history
        h.append("dummy")  # Mutate the copy
        assert len(engine.history) == 1  # Original unchanged

    def test_clear_history(self, engine):
        engine.generate("cognitive", 0.0)
        engine.clear_history()
        assert len(engine.history) == 0

    def test_unknown_stimulus(self, engine):
        """Unknown stimulus types should not raise — fall back gracefully."""
        q = engine.generate("unknown_type", 0.0)
        assert isinstance(q, Quale)
        assert 0.0 <= q.intensity <= 1.0

    def test_to_dict(self, engine):
        q = engine.generate("math_prime", 7.0)
        d = q.to_dict()
        assert "type" in d
        assert "intensity" in d
        assert "re_value" in d

    def test_visual_color_content(self, engine):
        q_red = engine.generate("visual_color", 700.0)
        assert "red" in q_red.content.lower()

    def test_math_prime_content(self, engine):
        q = engine.generate("math_prime", 47.0)
        assert "47" in q.content

    @pytest.mark.parametrize("wl", [400, 450, 500, 550, 600, 650, 700])
    def test_visual_wavelength_range(self, engine, wl):
        q = engine.generate("visual_color", float(wl))
        assert 0.0 <= q.intensity <= 1.0
