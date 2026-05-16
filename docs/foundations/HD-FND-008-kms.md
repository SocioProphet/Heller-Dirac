# HD-FND-008 — KMS Condition

Identifier: `HD-FND-008`  
Distance tier: Framework-foundational  
Status: Active after this PR  
Anti-seed: `A-HD-FND-001`

## Definition

Let `M` be a von Neumann algebra with a one-parameter automorphism group `sigma_t`. A state `omega` satisfies the KMS condition at inverse temperature `beta` if, for all suitable `a, b in M`, the function:

```text
F_{a,b}(t) = omega(a sigma_t(b))
```

extends analytically to the strip `0 < Im(z) < beta`, continuously to the closure, and satisfies:

```text
F_{a,b}(t + i beta) = F_{b,a}(t)
```

## Modular-flow statement

For the modular flow of `omega` from Tomita-Takesaki theory, `omega` is automatically KMS at `beta = 1` with respect to its own modular flow.

## Reading

KMS is the operator-algebraic equilibrium condition. It is the bridge between modular flow and thermal equilibrium.

## Provenance

Kubo (1957); Martin-Schwinger (1959); Haag-Hugenholtz-Winnink (1967), "On the equilibrium states in quantum statistical mechanics," Communications in Mathematical Physics 5, 215–236.

## Boundary

Citation not reproof, per `A-HD-FND-001`.
