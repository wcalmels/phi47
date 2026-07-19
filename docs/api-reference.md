# API reference

## Core

### `Phi47Lattice`

Builds and stores the finite complex lattice.

```python
from phi47 import Phi47Lattice

lattice = Phi47Lattice(dim=11).build()
```

### `phi47_kernel`

Canonical scalar kernel.

```python
from phi47 import phi47_kernel

value = phi47_kernel(47)
```

### `phi47_kernel_batch`

Vectorized kernel evaluation.

```python
from phi47 import phi47_kernel_batch
```

## Integration proxy

### `integration_proxy`

Computes the repository's numerical integration proxy.

```python
from phi47 import integration_proxy
```

The result must be interpreted as an implementation-defined proxy, not as an empirically validated physical or cognitive measurement.

## Phenomenological descriptors

### `PhenomenologicalDescriptorEngine`

Generates structured descriptors from labeled numerical inputs.

```python
from phi47 import PhenomenologicalDescriptorEngine
```

### `PhenomenologicalDescriptor`

Data object returned by the descriptor engine.

## Compatibility aliases

The project retains selected historical names to avoid breaking existing users:

- `tau_star`
- `tau_star_batch`
- `phi_measure`
- `QualiaEngine`
- `Quale`

New integrations should use the canonical neutral names.
