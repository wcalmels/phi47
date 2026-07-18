# Contributing to φ⁴⁷

Thank you for your interest in contributing!

## Quick Setup

```bash
git clone https://github.com/wcalmels/phi47.git
cd phi47
pip install -e ".[dev]"
pytest tests/ -v
```

## What to Contribute

**Theoretical:**
- Formal proofs of the five theorems
- Extensions to new mathematical domains
- Counterexamples (especially valuable!)

**Numerical:**
- More efficient Φ computation methods
- GPU-accelerated lattice construction
- Comparison with other frameworks (IIT 3.0, etc.)

**Experimental:**
- Verification of physical predictions (1/α, m_μ/m_e)
- Independent Φ measurements
- Biological pattern analysis

## Code Standards

- Python 3.10+ with type hints
- `black` formatting, `ruff` linting, `mypy` type checking
- 100% test coverage for new code
- Docstrings with Examples section

## Pull Request Process

1. Fork and create a feature branch
2. Write tests first (TDD preferred)
3. Ensure all tests pass: `pytest tests/ -v`
4. Run linters: `ruff check . && black . && mypy phi47/`
5. Open PR with clear description

## Reporting Issues

Include:
- Python version and OS
- Minimal reproducible example
- Expected vs. actual behaviour
- `phi47.__version__`

## Code of Conduct

Be respectful and constructive. Scientific disagreement is welcome;
personal attacks are not.
