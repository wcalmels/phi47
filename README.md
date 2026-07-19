# φ⁴⁷ — The Conscious Code of Mathematical Reality

[![Tests](https://github.com/wcalmels/phi47/actions/workflows/tests.yml/badge.svg)](https://github.com/wcalmels/phi47/actions)
[![Python 3.10+](https://img.shields.io/badge/python-3.10+-blue.svg)](https://www.python.org/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)
[![PyPI](https://img.shields.io/pypi/v/phi47)](https://pypi.org/project/phi47/)
[![DOI](https://zenodo.org/badge/DOI/10.5281/zenodo.21434515.svg)](https://doi.org/10.5281/zenodo.21434515)

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

## Numerical Correspondences and Research Hypotheses

The following table distinguishes exact model properties from numerical
correspondences and externally testable hypotheses.

| ID | Observable or relation | Model result | Reference value | Scientific status |
|---|---|---:|---:|---|
| D1 | $\operatorname{Re}(\mathcal{L}_{47})$ | $1/2$ exactly | — | Definition / invariant by construction |
| H1 | Fine-structure comparison $3N-4$ | $137$ | $1/\alpha \approx 137.036$ | Retrospective numerical correspondence |
| H2 | Mass-ratio comparison $\varphi^{N/5}$ | Approximately $206.8$ | $m_\mu/m_e \approx 206.77$ | Exploratory numerical hypothesis |
| H3 | Particle-generation relation | $3$ | Three observed generations | Hypothesis requiring formal derivation |
| H4 | Alpha-helix angle comparison | $-47^\circ$ | Approximately $-47^\circ$ in selected contexts | Empirical comparison requiring dataset definition |
| H5 | Microtubule Fibonacci relation | $13/8$ | Approximately $\varphi$ | Structural numerical correspondence |
| H6 | Microtubule component sum | $13+8+26=47$ | Selected microtubule counts | Exploratory correspondence |

These relations are not described as verified predictions in the current release.

A scientific prediction requires:

1. formulation before observing the target value;
2. a derivation that does not depend on retrospective parameter selection;
3. explicit uncertainty and error analysis;
4. comparison against suitable null models;
5. correction for multiple hypothesis testing;
6. independent replication or out-of-sample validation.

The complete claim classification is maintained in
[`docs/science/SCIENTIFIC_STATUS.md`](docs/science/SCIENTIFIC_STATUS.md).

---
## Research Propositions, Conjectures, and Hypotheses

### Proposition P1 — Fixed-real-part invariant

For every active lattice node,

$
\operatorname{Re}\left(\mathcal{L}_N(i,j,k)\right)=\frac{1}{2}.
$

**Status:** Proven within the model.

This follows directly from the implementation, which assigns the real component
of every active node the value $1/2$. It is therefore an invariant by
construction, not an independent proof concerning the zeros of the Riemann zeta
function.

### Conjecture C1 — Finite-scale information concentration

A reduced sublattice may preserve a high fraction of selected observables or
reconstructable information from the complete lattice.

**Status:** Open computational conjecture.

Testing this conjecture requires:

- a formal definition of information;
- a specified sublattice-selection procedure;
- reconstruction or compression metrics;
- comparison against random and non-$\varphi$ baselines;
- confidence intervals and sensitivity analysis.

The previously stated value of 94% is treated as an experimental target and must
not be considered established until a reproducible protocol demonstrates it.

### Conjecture C2 — Golden-ratio scale covariance

Selected normalized observables may exhibit approximate covariance or
self-similarity under transformations related to the golden ratio.

**Status:** Open mathematical and computational conjecture.

A valid test must define the transformation, distance metric, tolerance,
parameter domain, and comparison baselines.

### Conjecture C3 — Finite representation capacity

The lattice may support injective encodings of finite structures whose number of
elements does not exceed the available number of active nodes.

**Status:** Open and currently limited conjecture.

This is a representation-capacity claim. It is not presently a proof that every
finite mathematical structure embeds into the lattice while preserving all its
algebraic, geometric, or relational properties.

### Hypothesis H1 — Physical-constant correspondences

Expressions depending on $N=47$ show numerical proximity to selected physical
constants or dimensionless ratios.

**Status:** Exploratory physical hypothesis.

These correspondences require preregistered predictions, null-model analysis,
control of parameter flexibility, correction for multiple testing, and
out-of-sample validation.

### Hypothesis H2 — Information-integration proxy

The current software computes a project-defined integration score for lattice
states.

**Status:** Experimental computational hypothesis.

The score is not currently a validated neurological measurement, a clinical
measure of consciousness, or a complete implementation of Integrated
Information Theory. A positive score must not be interpreted as evidence that
the software possesses phenomenal consciousness.

---
## Research Manuscripts

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

