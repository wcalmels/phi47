"""
phi47.cli
=========

Command-line demonstration of the φ⁴⁷ finite-lattice research framework.

The demonstration constructs a lattice, generates deterministic computational
descriptors, and evaluates the project-defined information-integration proxy.
"""

from __future__ import annotations

import argparse

from phi47 import (
    PHI,
    N,
    PhenomenologicalDescriptorEngine,
    Phi47Lattice,
    integration_proxy,
)


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(
        prog="phi47-demo",
        description=("φ⁴⁷ — finite golden-ratio lattice research demonstration."),
    )
    parser.add_argument(
        "-d",
        "--dim",
        type=int,
        default=23,
        help=(
            "Lattice dimension N "
            "(default: 23; use 47 for the project reference dimension)."
        ),
    )
    parser.add_argument(
        "-s",
        "--samples",
        type=int,
        default=200,
        help=(
            "Number of sampled split positions used by the "
            "integration proxy (default: 200)."
        ),
    )
    parser.add_argument(
        "--seed",
        type=int,
        default=42,
        help="Random seed used by the integration proxy (default: 42).",
    )

    args = parser.parse_args(argv)

    if args.dim <= 0:
        parser.error("--dim must be greater than zero")
    if args.samples <= 0:
        parser.error("--samples must be greater than zero")

    print("=" * 68)
    print("  φ⁴⁷ — FINITE GOLDEN-RATIO LATTICE RESEARCH FRAMEWORK")
    print("=" * 68)
    print(f"  Golden ratio φ      : {PHI:.15f}")
    print(f"  Reference dimension : {N}")
    print()

    print(f"[1/3] Constructing finite lattice (N={args.dim}) ...")
    lattice = Phi47Lattice(dim=args.dim).build()

    print(f"  Active nodes        : {lattice.n_active:,}")
    print(f"  Mean real component : {lattice.mean_real:.10f}")
    print(
        "  Re = 1/2 invariant : "
        f"{'CONFIRMED' if lattice.verify_re_half() else 'FAILED'}"
    )
    print("  Status              : invariant by construction")
    print()

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
            f"{descriptor.content} "
            f"(score={descriptor.intensity:.4f})"
        )

    print()

    print("[3/3] Calculating information-integration proxy ...")
    integration_score = integration_proxy(
        lattice,
        method="fast",
        n_samples=args.samples,
        seed=args.seed,
    )

    print(f"  Integration proxy   : {integration_score:.6f}")
    print("  Interpretation      : project-defined numerical observable")
    print()
    print(
        "  Scientific note: this output is not a validated measurement "
        "of consciousness or IIT Φ."
    )
    print("=" * 68)

    return 0


if __name__ == "__main__":
    raise SystemExit(main())
