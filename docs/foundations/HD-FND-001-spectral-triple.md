# HD-FND-001 — Spectral Triple

Identifier: `HD-FND-001`  
Distance tier: Framework-foundational  
Status: Active after this PR  
Anti-seed: `A-HD-NC-001`, `A-HD-FND-001`

## Definition

A spectral triple `(A, H, D)` consists of:

1. An involutive associative algebra `A` over `C`.
2. A Hilbert space `H` equipped with a faithful star-representation `pi : A -> B(H)`.
3. A self-adjoint operator `D` with dense domain in `H`, satisfying:
   - compact resolvent: `(D - lambda)^(-1)` is compact for `lambda` in the resolvent set;
   - bounded commutators: `[D, pi(a)]` extends to a bounded operator for every `a in A`.

## Reading

`A` encodes algebraic or coordinate content. `H` is the Hilbert space representation. `D` is the generalized Dirac operator that carries differential, metric, and dimensional information.

The compact-resolvent condition encodes finite-dimensional spectral behavior. The bounded-commutator condition says elements of `A` behave like smooth functions relative to `D`.

## Summability and dimension

A spectral triple is `p`-summable if `(1 + D^2)^(-p/2)` is trace class. The infimum of such `p` is the spectral dimension. For compact Riemannian spin manifolds, this matches the topological dimension.

## Provenance

Standard references: Connes, *Noncommutative Geometry* (1994); Connes-Marcolli, *Noncommutative Geometry, Quantum Fields and Motives* (2008).

## Boundary

This identifier canonicalizes the standard definition. It does not construct a new spectral triple, prove properties of a specific spectral triple, or claim that spectral-triple reformulation constitutes progress on any Clay problem.
