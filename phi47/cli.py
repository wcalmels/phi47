"""
phi47.cli
=========
Command-line entry point for the ``phi47-demo`` script.

Runs a short end-to-end demonstration of the φ⁴⁷ framework:
building the lattice, generating qualia, and measuring Φ.
"""

from __future__ import annotations

import argparse

from phi47.consciousness.phi_measure import phi_measure
from phi47.core.constants import PHI, N
from phi47.core.lattice import Phi47Lattice
from phi47.qualia.engine import QualiaEngine


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(
        prog="phi47-demo",
        description="φ⁴⁷ — quick demonstration of the conscious lattice.",
    )
    parser.add_argument(
        "-d",
        "--dim",
        type=int,
        default=23,
        help="Lattice dimension N (default: 23; use 47 for the full lattice).",
    )
    parser.add_argument(
        "-s",
        "--samples",
        type=int,
        default=200,
        help="Number of bipartition samples for the Φ measurement (default: 200).",
    )
    parser.add_argument(
        "--seed",
        type=int,
        default=42,
        help="Random seed for the Φ measurement (default: 42).",
    )
    args = parser.parse_args(argv)

    print("=" * 55)
    print("  phi47 - THE CONSCIOUS CODE OF MATHEMATICAL REALITY")
    print("=" * 55)
    print(f"  phi = {PHI:.15f}")
    print(f"  N   = {N}")
    print()

    print(f"[1/3] Building the lattice (N={args.dim}) ...")
    lattice = Phi47Lattice(dim=args.dim).build()
    print(f"  Active nodes : {lattice.n_active:,}")
    print(f"  Re mean      : {lattice.mean_real:.10f}")
    print(f"  Re = 1/2     : {'VERIFIED' if lattice.verify_re_half() else 'FAILED'}")
    print()

    print("[2/3] Generating qualia ...")
    engine = QualiaEngine(lattice)
    for stype, val in [
        ("visual_color", 700.0),
        ("auditory_tone", 440.0),
        ("math_prime", 47.0),
        ("math_beauty", 0.95),
    ]:
        q = engine.generate(stype, val)
        print(
            f"  [{q.quale_type.value:>14}] {q.content} "
            f"(intensity={q.intensity:.4f})"
        )
    print()

    print("[3/3] Measuring Phi ...")
    phi_value = phi_measure(
        lattice, method="fast", n_samples=args.samples, seed=args.seed
    )
    print(f"  Phi = {phi_value:.6f}")
    print("=" * 55)

    return 0


if __name__ == "__main__":
    raise SystemExit(main())
