# HD-SP-003 — Heat-Kernel Expansion and gamma_E Interface

Identifier: `HD-SP-003`  
Distance tier: Framework-foundational  
Status: Active in Heller-Dirac v0.2  
Anti-seed: `A-HD-SP-001`, `A-HD-FND-001`  
Dependencies pinned: `988307215ad38ccb16514311222184a1b757752b`

## Scope

This identifier records heat-kernel asymptotic vocabulary used by spectral-action and regularization surfaces.

For Laplacian-type spectral data in an ordinary elliptic setting, the heat trace has a small-time asymptotic surface of the form:

```text
Tr(exp(-t D^2)) ~ sum_k a_k t^((k - p) / 2)
```

where `p` is the relevant dimension parameter and the coefficients `a_k` are the Seeley-DeWitt heat coefficients in the classical geometric case.

## Spectral-zeta interface

`HD-SP-003` connects `HD-SP-001` spectral-zeta vocabulary with heat-trace data through the Mellin-transform relation used in zeta regularization. The precise analytic continuation and residue structure must be verified for the operator under study.

## Spectral-action interface

`HD-FND-006` records the spectral action. The large-cutoff expansion of a spectral action is controlled by heat-kernel coefficients when the standard hypotheses apply.

## gamma_E interface

Gamma-function normalization appears in zeta regularization and Mellin-transform expansions. This is one reason `HD-SP-003` participates in the method-grade `gamma_E` synthesis recorded in `HD-MTH-001`.

## Provenance

Gilkey, *Invariance Theory, the Heat Equation, and the Atiyah-Singer Index Theorem*. Chamseddine-Connes (1997), "The spectral action principle." Connes-Marcolli (2008), *Noncommutative Geometry, Quantum Fields and Motives*.

## Boundary

This file is a reference surface for standard heat-kernel vocabulary. It does not construct a spectral triple, prove existence of an expansion for arbitrary spectral data, or promote any spectral-action claim into constructive field theory.
