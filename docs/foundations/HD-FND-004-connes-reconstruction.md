# HD-FND-004 — Connes Reconstruction Theorem

Identifier: `HD-FND-004`  
Distance tier: Framework-foundational  
Status: Active after this PR  
Anti-seed: `A-HD-FND-001`

## Statement surface

Connes' reconstruction theorem states, in essence, that a commutative spectral triple satisfying the appropriate first-order, regularity, finiteness, orientability, reality, and Poincare-duality hypotheses is the spectral triple of a compact Riemannian spin manifold.

Under those hypotheses:

```text
A = C^[4m∞[0m(M)
H = L^2(M, S)
D = canonical Dirac operator
```

where `M` is a compact Riemannian spin manifold and `S` its spinor bundle.

## Reading

This theorem is the reference point for treating classical Riemannian spin geometry as a special case of spectral triples. When the algebra `A` is noncommutative, the theorem does not say there is an ordinary manifold underneath.

## Provenance

Connes (2013), "On the spectral characterization of manifolds," Journal of Noncommutative Geometry 7, 1–82.

## Boundary

This file cites Connes' theorem. It does not reprove it, strengthen it, or apply it to arbitrary spectral triples. Downstream consumers may cite `HD-FND-004` only as reference surface.
