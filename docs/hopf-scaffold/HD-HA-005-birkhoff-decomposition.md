# HD-HA-005 — Birkhoff Decomposition on the Connes-Kreimer Character Group

Identifier: `HD-HA-005`  
Distance tier: Framework-foundational  
Status: Active in Heller-Dirac v0.2  
Anti-seed: `A-HD-HA-005`  
Dependencies pinned: `988307215ad38ccb16514311222184a1b757752b`

## Scope

This identifier records the Birkhoff-decomposition vocabulary attached to the Connes-Kreimer character group. A regularized rule is treated as a character of the Hopf algebra:

```text
phi : H_CK -> C
```

where `C` is the target algebra of regularized values.

## Factorization surface

The character loop is decomposed into a negative and a positive part:

```text
phi = phi_-^{-1} * phi_+
```

The convolution product is induced by the coproduct on `H_CK`.

The negative part `phi_-` records counterterm content. The positive part `phi_+` records the regularized finite part in the chosen scheme. Evaluation of `phi_+` at the regular point gives the renormalized value when the hypotheses of the chosen scheme are satisfied.

## Scheme dependence

A renormalization scheme supplies the projection or subtraction rule that determines the factorization. Minimal subtraction is the controlling reference example.

## Relation to HD-SP-004

`HD-HA-005` is the Hopf-algebraic factorization counterpart to the analytic Borel-Laplace vocabulary in `HD-SP-004`. The two surfaces are methodologically adjacent but logically independent.

## Provenance

Connes-Kreimer (2000), "Renormalization in quantum field theory and the Riemann-Hilbert problem." Connes-Marcolli (2004), "From Physics to Number Theory via Noncommutative Geometry, Part II."

## Boundary

Birkhoff decomposition is apparatus. It does not prove convergence of the underlying perturbative expansion, renormalizability of a target theory, or non-perturbative existence.
