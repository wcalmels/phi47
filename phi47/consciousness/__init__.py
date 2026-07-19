"""
Experimental information-integration components.

The package name ``consciousness`` is retained for backward compatibility.
Its numerical outputs are exploratory computational proxies and must not be
interpreted as demonstrated measurements of phenomenal consciousness.
"""

from phi47.consciousness.integration_proxy import (
    Method,
    integration_proxy,
)
from phi47.consciousness.phi_measure import phi_measure

__all__ = [
    "Method",
    "integration_proxy",
    "phi_measure",
]
