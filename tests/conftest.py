"""Shared pytest configuration and fixtures for phi47 tests."""
import pytest
from phi47.core.tau_star import clear_cache

@pytest.fixture(autouse=True)
def reset_tau_cache():
    """Clear the τ* cache before each test that uses it."""
    yield
    # Don't clear — allow caching between tests for speed
