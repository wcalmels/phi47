# Validation roadmap

## Current validation

The repository currently supports:

- unit and integration tests;
- cross-platform CI;
- linting and formatting checks;
- static type checking;
- explicit classification of scientific claims;
- reproducible examples.

## Required next steps

### Numerical robustness

- expand dimensional and boundary-condition tests;
- add property-based testing;
- document floating-point tolerances;
- benchmark runtime and memory use;
- test additional Python versions.

### Model comparison

- define baseline kernels and null models;
- add ablation studies;
- compare outputs under controlled parameter changes;
- separate invariants from implementation artifacts.

### External reproducibility

- publish frozen releases;
- archive releases with DOI metadata;
- provide machine-readable experiment configurations;
- invite independent reproduction and criticism.

### Empirical status

No empirical or physical interpretation should be promoted beyond hypothesis status without independently collected data, a prespecified protocol, uncertainty analysis, and external replication.
