\# Scientific Status of φ⁴⁷



\## Purpose



This document classifies the principal claims of the φ⁴⁷ research framework

according to their current evidential and mathematical status.



The purpose of this classification is to distinguish clearly between:



\- definitions introduced by the model;

\- propositions derived from those definitions;

\- reproducible numerical observations;

\- empirical comparisons;

\- mathematical conjectures;

\- scientific hypotheses;

\- speculative extensions.



No claim should be interpreted beyond the status assigned in this document.



\## Status categories



| Code | Category | Meaning |

|---|---|---|

| D | Definition | Introduced directly by the mathematical construction or source code |

| P | Model proposition | Derived analytically from the definitions |

| N | Numerical result | Obtained through a reproducible computation |

| E | Empirical comparison | Compared against independently measured or published data |

| C | Conjecture | Mathematically formulated but not formally proved |

| H | Hypothesis | Scientific interpretation requiring external validation |

| S | Speculative extension | Conceptual proposal without sufficient independent evidence |



\## Claim registry



| ID | Claim | Status | Current basis | Requirement for advancement |

|---|---|---|---|---|

| D1 | The active support satisfies \\(i+j+k<N\\) | Definition | Lattice construction | Not applicable |

| D2 | The real component is assigned the value \\(1/2\\) | Definition | Source-code construction | Not applicable |

| P1 | \\(\\operatorname{Re}(\\mathcal{L}\_N)=1/2\\) at every active node | Model proposition | Immediate consequence of D2 | Formal statement and test |

| N1 | The active-node count agrees with the tetrahedral combinatorial formula | Numerical/model result | Computation and combinatorics | Automated property tests |

| C1 | Selected observables exhibit golden-ratio scale covariance | Conjecture | Preliminary numerical behavior | Define transformation, metric and tolerance |

| C2 | A reduced sublattice preserves most relevant information | Conjecture | Preliminary project assertion | Define information measure and null model |

| H1 | Expressions involving \\(N=47\\) correspond to physical constants | Hypothesis | Numerical proximity | Preregistered out-of-sample predictions |

| H2 | The integration proxy has relevance to consciousness research | Hypothesis | Internal computational metric | Independent neurological and theoretical validation |

| S1 | φ⁴⁷ provides a universal code of mathematical reality | Speculative extension | Conceptual interpretation | Formal theory and independent empirical evidence |



\## Critical-line interpretation



The current lattice implementation assigns the real component directly:



\\\[

\\mathcal{L}\_N(i,j,k)

=

\\frac{1}{2}

\+

\\mathrm{i}\\,\\Gamma\_N(i,j,k).

\\]



Therefore,



\\\[

\\operatorname{Re}\\mathcal{L}\_N(i,j,k)=\\frac12

\\]



is an invariant by construction.



This property may be useful for investigating mathematical structures constrained

to critical-line geometry. It does not independently prove that the non-trivial

zeros of the Riemann zeta function have real part \\(1/2\\).



\## Oscillatory kernel



The function historically named `tau\_star` is a project-specific synthetic

oscillatory kernel.



In the current implementation it must not be described as:



\- Ramanujan's tau function;

\- a formally derived modification of Ramanujan's tau function;

\- a demonstrated approximation to Ramanujan's tau function.



Future versions should expose the neutral name `phi47\_kernel`, while temporarily

retaining `tau\_star` only as a deprecated compatibility alias.



\## Consciousness-related components



The current consciousness-related score is a project-defined integration proxy.



It is not currently:



\- a validated neurological measurement;

\- a clinical measure of consciousness;

\- a complete implementation of Integrated Information Theory;

\- evidence that the software experiences phenomenal consciousness.



Outputs produced by the qualitative-description engine are algorithmic

phenomenological labels, not demonstrated subjective experiences.



\## Evidence policy



A claim may be upgraded only when the repository contains, as applicable:



1\. a precise mathematical definition;

2\. a formal derivation or proof;

3\. reproducible source code;

4\. tests and uncertainty analysis;

5\. null-model comparisons;

6\. correction for multiple hypothesis testing;

7\. independently sourced data;

8\. falsification criteria;

9\. independent replication.



\## Version status



The current project should be described as exploratory research software.



Recommended release designation:



```text

v0.2.0 — Scientific clarification and validation framework

