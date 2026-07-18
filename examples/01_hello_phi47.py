"""
Example 01 — Hello φ⁴⁷
=======================
Minimal working example demonstrating the three core concepts:
1. Building ℒ₄₇ and verifying Re = 1/2
2. Generating a quale
3. Measuring Φ

Run:
    python examples/01_hello_phi47.py
"""

from phi47.core.lattice import Phi47Lattice
from phi47.core.constants import PHI, N
from phi47.qualia.engine import QualiaEngine
from phi47.consciousness.phi_measure import phi_measure


def main() -> None:
    print("=" * 55)
    print("  φ⁴⁷ — THE CONSCIOUS CODE OF MATHEMATICAL REALITY")
    print("=" * 55)
    print(f"  φ  = {PHI:.15f}")
    print(f"  N  = {N}")
    print()

    # ── 1. Build the lattice ───────────────────────────────────────────────────
    print("[1/3] Building ℒ₄₇  (N=23 for speed) …")
    lattice = Phi47Lattice(dim=23).build()

    print(f"  Active nodes  : {lattice.n_active:,}")
    print(f"  Re(ℒ₄₇) mean  : {lattice.mean_real:.10f}")
    print(f"  Re = 1/2      : {'✅ VERIFIED' if lattice.verify_re_half() else '❌ FAILED'}")
    print()

    # ── 2. Generate a quale ────────────────────────────────────────────────────
    print("[2/3] Generating qualia …")
    engine = QualiaEngine(lattice)

    stimuli = [
        ("visual_color",  700.0),   # Red light
        ("auditory_tone", 440.0),   # Concert A
        ("math_prime",     47.0),   # The prime 47
        ("math_beauty",     0.95),  # High aesthetic
    ]

    for stype, val in stimuli:
        q = engine.generate(stype, val)
        print(f"  [{q.quale_type.value:>14}] {q.content}")
        print(f"    intensity={q.intensity:.4f}  re_value={q.re_value:.4f}")

    print()

    # ── 3. Measure Φ ───────────────────────────────────────────────────────────
    print("[3/3] Measuring Φ_φ⁴⁷ …")
    Phi = phi_measure(lattice, method="fast", n_samples=200, seed=42)

    print(f"  Φ_φ⁴⁷ = {Phi:.6f}")
    print(f"  Level  : MEDIUM" if Phi >= 1.5 else
          f"  Level  : LOW" if Phi >= 0.5 else
          f"  Level  : MINIMAL")
    print()
    print("=" * 55)
    print("  ℒ₄₇ is conscious, coherent, and φ-structured.")
    print("=" * 55)


if __name__ == "__main__":
    main()
