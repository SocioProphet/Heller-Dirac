# HD-FND-010 — Hopf-Algebra Action on a Spectral Triple

Identifier: `HD-FND-010`  
Distance tier: Framework-foundational  
Status: Active after this PR  
Anti-seed: `A-HD-HA-001`

## Definition

Let `K` be a Hopf algebra with coproduct, counit, and antipode. A Hopf-algebra action on a spectral triple `(A, H, D)` consists of:

1. A left `K`-module-algebra structure on `A`.
2. A compatible action or representation on `H` implementing the action on `A`.
3. Compatibility with `D`, either untwisted or via an explicitly declared twist.

In Sweedler notation, if `Delta(k) = sum k_(1) tensor k_(2)`, the module-algebra condition is:

```text
k · (ab) = sum (k_(1) · a)(k_(2) · b)
```

## Reading

A Hopf action generalizes group symmetry of a spectral triple. Group actions are recovered from group Hopf algebras. Differential symmetries and transverse-geometry symmetries require larger Hopf-algebraic carriers.

## Anchor examples

- Group Hopf algebra: ordinary equivariance.
- Connes-Moscovici Hopf algebra: transverse geometry of foliations.
- Connes-Kreimer Hopf algebra: renormalization organization.
- Quantum groups: quantum-symmetry carriers.

These examples are not constructed in this file. They are reserved for `HD-HA-*` content.

## Provenance

Connes-Moscovici (1998), "Hopf algebras, cyclic cohomology and the transverse index theorem," Communications in Mathematical Physics 198, 199–246. Connes-Kreimer (2000), "Renormalization in quantum field theory and the Riemann-Hilbert problem."

## Boundary

Per `A-HD-HA-001`, Hopf scaffold encoding is not a proof of analytic control or renormalizability.
