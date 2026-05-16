# HD-FND-003 — Real Structure and KO-Dimension

Identifier: `HD-FND-003`  
Distance tier: Framework-foundational  
Status: Active after this PR

## Definition

A real structure on a spectral triple `(A, H, D)` is an antilinear isometry `J : H -> H` satisfying sign relations:

```text
J^2 = epsilon
JD = epsilon' DJ
J gamma = epsilon'' gamma J    (even triples only)
```

where `epsilon`, `epsilon'`, and `epsilon''` are signs. The commutant and first-order conditions are:

```text
[pi(a), J pi(b) J^{-1}] = 0
[[D, pi(a)], J pi(b) J^{-1}] = 0
```

for all `a, b in A`.

## KO-dimension table

| KO-dim | epsilon | epsilon-prime | epsilon-double-prime | Example |
|---|---|---|---|---|
| 0 | +1 | +1 | +1 | point |
| 1 | +1 | -1 | n/a | circle |
| 2 | -1 | +1 | -1 | two-dimensional spin geometry |
| 3 | -1 | +1 | n/a | three-dimensional spin geometry |
| 4 | -1 | +1 | +1 | spin four-manifold |
| 5 | -1 | -1 | n/a | five-dimensional spin geometry |
| 6 | +1 | +1 | -1 | Standard Model finite triple convention |
| 7 | +1 | -1 | n/a | seven-dimensional spin geometry |

## Reading

KO-dimension is the mod-8 dimension carried by the real-structure signs. For commutative Riemannian spin manifolds it agrees with topological dimension modulo 8. For noncommutative triples it is sign data, not necessarily a literal topological dimension.

## Provenance

Connes, "Noncommutative geometry and reality" (1995); Connes-Marcolli (2008), Chapter 1.

## Boundary

This is standard reference surface. It is not a new theorem or new model.
