"""
Example 01 — Hello φ⁴⁷
=======================

Minimal working example demonstrating:

1. construction of the finite lattice;
2. verification of the fixed-real-part invariant;
3. generation of deterministic computational descriptors;
4. calculation of the project-defined information-integration proxy.

Run
---
    py examples/01_hello_phi47.py
"""

from phi47 import (
    N,
    PHI,
    PhenomenologicalDescriptorEngine,
    Phi47Lattice,
    integration_proxy,
)


def main() -> None:
    print("=" * 68)
    print("  φ⁴⁷ — FINITE GOLDEN-RATIO LATTICE RESEARCH FRAMEWORK")
    print("=" * 68)
    print(f"  Golden ratio φ      : {PHI:.15f}")
    print(f"  Reference dimension : {N}")
    print()

    # 1. Construct the finite lattice.
    print("[1/3] Constructing lattice (N=23 for demonstration speed) ...")
    lattice = Phi47Lattice(dim=23).build()

    print(f"  Active nodes        : {lattice.n_active:,}")
    print(f"  Mean real component : {lattice.mean_real:.10f}")
    print(
        "  Re = 1/2 invariant : "
        f"{'CONFIRMED' if lattice.verify_re_half() else 'FAILED'}"
    )
    print("  Status              : invariant by construction")
    print()

    # 2. Generate deterministic software descriptors.
    print("[2/3] Generating computational descriptors ...")
    engine = PhenomenologicalDescriptorEngine(lattice)

    stimuli = [
        ("visual_color", 700.0),
        ("auditory_tone", 440.0),
        ("math_prime", 47.0),
        ("math_beauty", 0.95),
    ]

    for stimulus_type, value in stimuli:
        descriptor = engine.generate(stimulus_type, value)

        print(
            f"  [{descriptor.quale_type.value:>14}] "
            f"{descriptor.content}"
        )
        print(
            f"    score={descriptor.intensity:.4f} "
            f"real={descriptor.re_value:.4f}"
        )

    print()

    # 3. Calculate the project-defined integration proxy.
    print("[3/3] Calculating information-integration proxy ...")

    score = integration_proxy(
        lattice,
        method="fast",
        n_samples=200,
        seed=42,
    )

    print(f"  Integration proxy   : {score:.6f}")
    print("  Interpretation      : exploratory numerical observable")
    print()
    print(
        "  This calculation is not a validated measurement of "
        "consciousness and is not a complete implementation of IIT Φ."
    )
    print("=" * 68)


if __name__ == "__main__":
    main()
