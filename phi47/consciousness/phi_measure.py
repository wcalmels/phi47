"""
Backward-compatible interface for the historical ``phi_measure`` module.

The canonical public API is ``integration_proxy``.

The returned value is a project-defined entropy-based integration score. It is
not a validated measurement of consciousness and is not a complete
implementation of Integrated Information Theory.
"""

from __future__ import annotations

from phi47.consciousness.integration_proxy import (
    Method,
    _entropy,
    _integration_entropy,
    _integration_exact,
    _integration_fast,
    integration_proxy,
)

# Historical public alias.
phi_measure = integration_proxy

# Historical internal aliases retained for compatibility with existing tests
# and downstream code.
_phi_exact = _integration_exact
_phi_fast = _integration_fast
_phi_entropy = _integration_entropy

__all__ = [
    "Method",
    "integration_proxy",
    "phi_measure",
]
