"""
Backward-compatible aliases for the historical ``tau_star`` API.

The original names are retained temporarily so that existing software does not
break. The implemented sequence is a project-specific synthetic oscillatory
kernel; it is not Ramanujan's tau function.

New code should import:

    phi47_kernel
    phi47_kernel_batch

from :mod:`phi47.core.kernel`.
"""

from __future__ import annotations

from .kernel import (
    clear_kernel_cache,
    kernel_cache_info,
    phi47_kernel,
    phi47_kernel_batch,
)

# Direct aliases preserve the LRU cache methods attached to phi47_kernel,
# including cache_clear() and cache_info().
tau_star = phi47_kernel
tau_star_batch = phi47_kernel_batch


def clear_cache() -> None:
    """Clear the kernel cache through the historical compatibility API."""
    clear_kernel_cache()


def cache_info() -> str:
    """Return cache information through the historical compatibility API."""
    info = phi47_kernel.cache_info()
    return (
        f"τ* cache — hits: {info.hits}, misses: {info.misses}, "
        f"size: {info.currsize}/{info.maxsize}"
    )


__all__ = [
    "tau_star",
    "tau_star_batch",
    "clear_cache",
    "cache_info",
]

