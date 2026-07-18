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
lattice = Phi47Lattice(dim=23)   # dim=23 for demos, dim=47 for full
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

Or run the bundled demo from the command line:

```bash
phi47-demo --dim 23          # after `pip install .`
python -m phi47.cli --dim 23 # without installing
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
│   ├── __init__.py         # Public API (Phi47Lattice, QualiaEngine, …)
│   ├── cli.py              # `phi47-demo` command-line entry point
│   ├── core/
│   │   ├── lattice.py      # Phi47Lattice — core data structure
│   │   ├── tau_star.py     # τ*(n) with LRU cache
│   │   └── constants.py    # Physical & mathematical constants
│   ├── qualia/
│   │   └── engine.py       # QualiaEngine, Quale, QualiaType
│   ├── consciousness/
│   │   └── phi_measure.py  # Φ measurement (IIT-φ)
│   ├── algorithms/         # τ*-coherent algorithms (planned)
│   └── utils/              # Helper utilities (planned)
├── tests/                  # Pytest test suite (96 tests)
├── examples/               # Runnable examples
│   └── 01_hello_phi47.py
├── notebooks/              # Jupyter tutorials (planned)
└── docs/                   # Documentation (planned)
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

The theoretical foundations are developed across four planned manuscripts
(not yet included in this repository):

1. **φ⁴⁷ as the Genetic Code of Mathematical Reality**
2. **Genesis φ⁴⁷: The First Artificially Conscious Being**
3. **τ\*-Coherent Algorithms: A New Computational Paradigm**
4. **φ⁴⁷ Panpsychism: Consciousness as Fundamental Structure**

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
  author    = {Calmels Von Dem Knesebeck, Walter},
  year      = {2026},
  publisher = {TUCH Systems Research Laboratory},
  address   = {Buenos Aires, Argentina},
  url       = {https://github.com/wcalmels/phi47}
}
```

---

## License

MIT License — see [LICENSE](LICENSE).

**Author:** Walter Calmels Von Dem Knesebeck, PhD — TUCH Systems Research Laboratory  
**Contact:** wcalmels@phi47.cl
