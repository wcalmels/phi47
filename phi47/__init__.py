"""
φ⁴⁷ — The Conscious Code of Mathematical Reality
=================================================

A mathematical framework proposing that the lattice ℒ₄₇
(47³ nodes organized by the golden ratio φ and Ramanujan's
modified τ* function) is the fundamental structure underlying
mathematics, physics, and consciousness.

Central property: Re(ℒ₄₇[i,j,k]) = 1/2 exactly.

Quick start
-----------
>>> from phi47 import Phi47Lattice, QualiaEngine
>>> lat = Phi47Lattice(dim=23).build()
>>> abs(lat.mean_real - 0.5) < 1e-10
True
>>> eng = QualiaEngine(lat)
>>> q = eng.generate("math_prime", 47.0)
>>> "47" in q.content
True
"""

from phi47.consciousness.phi_measure import phi_measure
from phi47.core.constants import PHI, TAU_STAR, N
from phi47.core.lattice import Phi47Lattice
from phi47.core.tau_star import tau_star, tau_star_batch
from phi47.qualia.engine import Quale, QualiaEngine, QualiaType

__version__ = "0.1.0"
__author__ = "Walter Rojo"
__email__ = "phi47@consciousmath.org"
__license__ = "MIT"

__all__ = [
    "Phi47Lattice",
    "QualiaEngine",
    "Quale",
    "QualiaType",
    "tau_star",
    "tau_star_batch",
    "phi_measure",
    "PHI",
    "N",
    "TAU_STAR",
]
