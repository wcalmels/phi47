"""Shared pytest configuration and fixtures for phi47 tests."""

import pytest


@pytest.fixture(autouse=True)
def reset_tau_cache():
    """Clear the τ* cache before each test that uses it."""
    yield
    # Don't clear — allow caching between tests for speed
