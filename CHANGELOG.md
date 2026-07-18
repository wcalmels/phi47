# Changelog

All notable changes to this project are documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.1.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [Unreleased]

### Added
- Papers under `papers/` (in progress).

## [0.1.2] - 2026-07-18

### Changed
- Updated author metadata to Walter Calmels Von Dem Knesebeck (wcalmels@phi47.cl).

## [0.1.1] - 2026-07-18

### Added
- PyPI Trusted Publishing workflow (OIDC, no stored tokens).
- Zenodo metadata (`.zenodo.json`) and `CITATION.cff` for DOI minting.

### Fixed
- Repaired a BOM-corrupted `pyproject.toml` that broke installation.
- Formatted code (black/isort/ruff) and fixed mypy; green CI on Linux/macOS/Windows across Python 3.10-3.12.

## [0.1.0] - 2026-07-18

### Added
- Initial release: core lattice (`Phi47Lattice`) with the exact Re = 1/2 property.
- Modified Ramanujan `tau*` function with an LRU cache.
- `QualiaEngine` (stimulus to quale) and `phi_measure` (integrated information, IIT-phi).
- `phi47-demo` CLI, a runnable example, and a 96-test suite.

[Unreleased]: https://github.com/wcalmels/phi47/compare/v0.1.2...HEAD
[0.1.2]: https://github.com/wcalmels/phi47/compare/v0.1.1...v0.1.2
[0.1.1]: https://github.com/wcalmels/phi47/compare/v0.1.0...v0.1.1
[0.1.0]: https://github.com/wcalmels/phi47/releases/tag/v0.1.0
