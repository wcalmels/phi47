# Mathematical model

## Finite lattice

Phi47 constructs a finite complex lattice intended for deterministic numerical study. The implementation exposes lattice state, summary values, and derived numerical quantities through a tested Python API.

## Canonical kernel

The canonical scalar kernel is exposed as:

```python
from phi47 import phi47_kernel
```

Legacy names such as `tau_star` remain available as compatibility aliases. The neutral kernel name is preferred in new code and documentation.

## Integration proxy

The integration proxy is a software-defined numerical summary. It is not presented as a validated measurement of consciousness or any other latent physical property.

```python
from phi47 import integration_proxy
```

Interpretation must remain limited to the implementation and the experiments documented in the repository.

## Phenomenological descriptors

`PhenomenologicalDescriptorEngine` maps an input label and scalar value to a structured descriptor. These descriptors are computational objects used for testing and exploration; they are not direct observations of subjective experience.

## Reproducibility

For every numerical result, the project aims to document:

- input values;
- lattice dimension;
- algorithm version;
- random seed, when applicable;
- expected tolerance;
- test or reproduction command.
