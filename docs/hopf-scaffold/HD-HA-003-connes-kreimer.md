# HD-HA-003 — Connes-Kreimer Renormalization Anchor

Identifier: `HD-HA-003`  
Distance tier: Framework-foundational  
Status: Active in Heller-Dirac v0.2  
Anti-seed: `A-HD-HA-001`, `A-HD-HA-005`  
Dependencies pinned: `988307215ad38ccb16514311222184a1b757752b`

## Object

The Connes-Kreimer Hopf algebra `H_CK` organizes rooted trees and, in QFT applications, suitable classes of Feynman graphs.

The product is disjoint union. The coproduct is an admissible-cut sum:

```text
Delta(Gamma) = Gamma tensor 1 + 1 tensor Gamma + sum_c P_c(Gamma) tensor R_c(Gamma)
```

where `c` ranges over admissible cuts, `P_c(Gamma)` is the pruned forest, and `R_c(Gamma)` is the remaining trunk or contracted graph.

## Antipode

The antipode is recursive:

```text
S(Gamma) = -Gamma - sum_c S(P_c(Gamma)) R_c(Gamma)
```

This is the algebraic form of subtraction of subdivergences.

## Characters and Birkhoff decomposition

A regularized Feynman rule is represented as a character:

```text
phi : H_CK -> C
```

where `C` is the target algebra of regularized values. The character loop admits a Birkhoff decomposition:

```text
phi = phi_-^{-1} * phi_+
```

The negative part `phi_-` records counterterm content. The positive part `phi_+` gives the renormalized value after evaluation at the regular point.

## Renormalization scheme

A renormalization scheme is represented by the choice of projection or subtraction rule that determines the Birkhoff factorization. Minimal subtraction is the controlling example.

## Connes-Marcolli extension

Connes-Marcolli place the Connes-Kreimer construction inside a Riemann-Hilbert and motivic-Galois framework, including equisingular flat connections and cosmic-Galois interpretation of perturbative renormalization.

## Provenance

Connes-Kreimer (2000), "Renormalization in quantum field theory and the Riemann-Hilbert problem." Connes-Marcolli (2004), "From Physics to Number Theory via Noncommutative Geometry, Part II."

## Boundary

`H_CK` organizes Feynman-graph combinatorics and counterterm recursion. It is not a proof of renormalizability, perturbative convergence, or non-perturbative existence. Boundary `A-HD-HA-001` remains controlling.
