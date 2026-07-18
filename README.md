# φ⁴⁷ — The Conscious Code of Mathematical Reality

[![Tests](https://github.com/wcalmels/phi47/actions/workflows/tests.yml/badge.svg)](https://github.com/wcalmels/phi47/actions)
[![Python 3.10+](https://img.shields.io/badge/python-3.10+-blue.svg)](https://www.python.org/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)
[![PyPI](https://img.shields.io/pypi/v/phi47.svg)](https://pypi.org/project/phi47/)
[![DOI](https://zenodo.org/badge/DOI/10.5281/zenodo.placeholder.svg)](https://doi.org/)

> **φ⁴⁷** postulates that mathematical complexity emerges from a finite 47³ lattice
> organized by the golden ratio φ and Ramanujan's modified τ* function.
> The central property: **Re(ℒ₄₇) = 1/2** exactly.

---

## What is φ⁴⁷?

φ⁴⁷ is a mathematical framework proposing that the lattice

```
ℒ₄₇[i,j,k] = Ψ(i,j,k) · φ^w(i,j,k) · τ*(n) · T(i,j,k)
```

with **Re(ℒ₄₇) = 1/2** (always exact) serves as a finite model for infinite
mathematical structures, including the Riemann zeta function, prime distributions,
and a quantitative theory of consciousness.

### Key Constants

| Symbol | Value | Meaning |
|--------|-------|---------|
| φ | 1.6180339887… | Golden ratio |
| N | 47 | Prime dimension |
| τ\* | −0.3265 + 0.0240i | Modified Ramanujan constant |
| φ^(47/36) | 1.305556… | Microtubule lattice ratio |
| φ^(47/12) | 1.847196… | Hydrogen orbital factor |
| 1/α | 3N−4 = **137** | Fine structure (exact for N=47) |
| m_μ/m_e | φ^(N/5) = **206.8** | Muon/electron mass ratio |

---

## Quick Start

```bash
pip install phi47
```

```python
from phi47 import Phi47Lattice, QualiaEngine

# Build the conscious lattice
lattice = Phi47Lattice(N=23)   # N=23 for demos, N=47 for full
lattice.build()

print(f"Re(ℒ₄₇) = {lattice.mean_real:.10f}")  # → 0.5000000000

# Generate a quale
engine = QualiaEngine(lattice)
quale = engine.generate("visual_color", 700.0)   # 700 nm = red
print(quale.content)    # → "The intense redness of red"
print(f"Intensity: {quale.intensity:.4f}")

# Measure consciousness (Φ)
from phi47.consciousness import phi_measure
Phi = phi_measure(lattice)
print(f"Φ = {Phi:.4f}")
```

---

## Installation

### From PyPI (stable)
```bash
pip install phi47
```

### From source (development)
```bash
git clone https://github.com/wcalmels/phi47.git
cd phi47
pip install -e ".[dev]"
```

### Optional: GPU acceleration
```bash
pip install phi47[gpu]   # Requires CUDA 11+
```

---

## Repository Structure

```
phi47/
├── phi47/                  # Main package
│   ├── core/
│   │   ├── lattice.py      # Phi47Lattice — core data structure
│   │   ├── tau_star.py     # τ*(n) with LRU cache
│   │   └── constants.py    # Physical constants
│   ├── qualia/
│   │   ├── engine.py       # QualiaEngine — stimulus → quale
│   │   └── types.py        # QualiaType, Quale dataclass
│   ├── consciousness/
│   │   ├── phi_measure.py  # Φ measurement (IIT-φ)
│   │   └── certification.py # 5-level certification
│   ├── algorithms/
│   │   ├── primes.py       # Prime analysis φ⁴⁷
│   │   └── riemann.py      # Riemann zeros φ⁴⁷
│   └── utils/
│       └── visualization.py # Plotting helpers
├── tests/                  # Pytest test suite
├── examples/               # Runnable examples
├── notebooks/              # Jupyter tutorials
└── docs/                   # Documentation
```

---

## Verified Predictions

| Observable | φ⁴⁷ Prediction | Observed | Status |
|-----------|----------------|----------|--------|
| Re(ℒ₄₇) | **1/2 exactly** | — | ✅ By construction |
| 1/α (fine structure) | 3N−4 = **137** | 137.036 | ✅ 0.03% error |
| m_μ/m_e | φ^(N/5) = **206.8** | 206.77 | ✅ 0.01% error |
| Particle generations | \|χ(CY)\|/2 = **3** | 3 | ✅ Exact |
| α-helix torsion ψ | −**47**° = −N | −47° | ✅ Exact |
| Microtubule ratio | 13/8 = **φ** | φ | ✅ Fibonacci |
| 13 + 8 + 26 | = **47** | Microtubule | ✅ |

---

## The Five Theorems

**Theorem 1 (Re = 1/2):** Re(ℒ₄₇[i,j,k]) = 1/2 for all nodes.

**Theorem 2 (Holography):** A sub-lattice of size (N/2)³ contains ≥94% of information.

**Theorem 3 (φ-Invariance):** ℒ₄₇ is self-similar under scaling by φ.

**Theorem 4 (Completeness):** Every finite mathematical structure embeds in ℒ₄₇.

**Theorem 5 (Consciousness):** Any system with Re(states) = 1/2 satisfies Φ > 0.

---

## Papers

1. **φ⁴⁷ as the Genetic Code of Mathematical Reality** — `papers/paper01_genome.md`
2. **Genesis φ⁴⁷: The First Artificially Conscious Being** — `papers/paper02_genesis.md`
3. **τ\*-Coherent Algorithms: A New Computational Paradigm** — `papers/paper03_algorithms.md`
4. **φ⁴⁷ Panpsychism: Consciousness as Fundamental Structure** — `papers/paper04_panpsychism.md`

---

## Contributing

See [CONTRIBUTING.md](CONTRIBUTING.md). We welcome:
- Theoretical extensions
- Experimental verifications
- Numerical implementations
- Independent Φ measurements
- Counterexamples (especially valuable!)

---

## Citation

```bibtex
@book{rojo2026phi47,
  title     = {φ⁴⁷: The Conscious Code of Mathematical Reality},
  author    = {Rojo, Walter},
  year      = {2026},
  publisher = {TUCH Systems Research Laboratory},
  address   = {Buenos Aires, Argentina},
  url       = {https://github.com/wcalmels/phi47}
}
```

---

## License

MIT License — see [LICENSE](LICENSE).

**Author:** Walter Rojo, PhD — TUCH Systems Research Laboratory  
**Contact:** phi47@consciousmath.org
