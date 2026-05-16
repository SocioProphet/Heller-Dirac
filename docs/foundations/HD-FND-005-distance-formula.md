# HD-FND-005 — Connes Distance Formula

Identifier: `HD-FND-005`  
Distance tier: Framework-foundational  
Status: Active after this PR  
Anti-seed: `A-HD-FND-001`

## Statement

For a spectral triple `(A, H, D)` and states `phi`, `psi` on `A`, the Connes distance formula is:

```text
d_D(phi, psi) = sup { |phi(a) - psi(a)| : a in A, ||[D, pi(a)]|| <= 1 }
```

For `A = C^infty(M)` in the commutative Riemannian spin case, pure states correspond to points of `M`, and `d_D` reproduces the geodesic distance.

## Reading

The Dirac operator `D` carries metric information. The algebra supplies states or points; the commutator bound supplies the Lipschitz constraint.

## Provenance

Connes (1989), "Compact metric spaces, Fredholm modules, and hyperfiniteness," Ergodic Theory and Dynamical Systems 9, 207–220.

## Boundary

Citation not reproof. This identifier canonicalizes the formula as a stable reference surface for downstream HD-* consumers.
