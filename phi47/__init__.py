"""
φ⁴⁷ — Finite Golden-Ratio Lattice Research Framework
=====================================================

Exploratory research software for constructing and studying finite,
complex-valued tetrahedral lattices parameterized by the golden ratio.

The current implementation includes:

- a finite tetrahedral lattice;
- a project-specific synthetic oscillatory kernel;
- reproducible numerical observables;
- experimental information-integration and phenomenological descriptors.

Scientific status
-----------------
The equality ``Re(L) = 1/2`` is an invariant by construction because the real
component is assigned directly by the lattice definition.

Physical, biological, and consciousness-related interpretations are research
hypotheses. The software does not establish the Riemann hypothesis, derive
physical constants from first principles, or demonstrate phenomenal
consciousness.

The historical names ``tau_star`` and ``tau_star_batch`` remain available for
backward compatibility. They refer to the synthetic φ⁴⁷ kernel and must not be
interpreted as implementations of Ramanujan's tau function.

Quick start
-----------
>>> from phi47 import Phi47Lattice
>>> lattice = Phi47Lattice(dim=23).build()
>>> abs(lattice.mean_real - 0.5) < 1e-10
True
"""

from phi47.consciousness import integration_proxy, phi_measure
from phi47.core.constants import N, PHI, TAU_STAR
from phi47.core.kernel import phi47_kernel, phi47_kernel_batch
from phi47.core.lattice import Phi47Lattice
from phi47.core.tau_star import tau_star, tau_star_batch
from phi47.qualia.engine import Quale, QualiaEngine, QualiaType

__version__ = "0.1.2"
__author__ = "Walter Calmels Von Dem Knesebeck"
__email__ = "wcalmels@phi47.cl"
__license__ = "MIT"

__all__ = [
    "Phi47Lattice",
    "QualiaEngine",
    "Quale",
    "QualiaType",
    "phi47_kernel",
    "phi47_kernel_batch",
    "tau_star",
    "tau_star_batch",
    "integration_proxy",
    "phi_measure",
    "PHI",
    "N",
    "TAU_STAR",
]

