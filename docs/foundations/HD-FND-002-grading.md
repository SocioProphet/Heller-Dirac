# HD-FND-002 — Even Spectral Triples and Grading

Identifier: `HD-FND-002`  
Distance tier: Framework-foundational  
Status: Active after this PR

## Definition

A spectral triple `(A, H, D)` is even if there exists a bounded operator `gamma` on `H` such that:

- `gamma^2 = 1`;
- `gamma* = gamma`;
- `gamma pi(a) = pi(a) gamma` for all `a in A`;
- `gamma D = -D gamma`.

The operator `gamma` is the grading. If no such grading exists, the triple is odd.

## Hilbert-space decomposition

An even spectral triple decomposes:

```text
H = H^+ direct-sum H^-
```

where `gamma` acts by `+1` on `H^+` and by `-1` on `H^-`. The Dirac operator exchanges the two subspaces.

## Reading

In the commutative spin-manifold case, the grading is the chirality operator in even dimension. Even/odd spectral triples track parity of the underlying spin geometry.

## Boundary

Reference-surface canonicalization only. No new theorem is claimed.
