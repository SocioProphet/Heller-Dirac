# C-8 — Cubic-Invariant Condition (v) for A2 Gate Minimality

Status: C-8 formulation document; obligation formulated, not closed as theorem.  
Track: A2 gate-minimality, path beta convention.  
Claim level: definition/scope only.  
Depends on: `docs/gate-minimality/claim-boundary.md`, `docs/gate-minimality/a2-gate-minimality-structural-sketch.md`, `docs/gate-minimality/c7-su3-subgroup-classification-scope.md`.

## Purpose

C-8 defines the A2 analog of A1 condition (v).

At A1, condition (v) was the preservation of a degree-2 symplectic pairing on the active-sector representation. Under the adopted A2 path-beta convention, condition (v) becomes preservation of the selected degree-3 cubic invariant under the active-sector action.

This document formulates the condition. It does not prove that any subgroup or active-sector action satisfies it in the final A2 theorem sense.

## A2 condition (v)

Let the A2 active-sector action be represented by:

```text
rho_A2 : G -> SU(3)
```

with active space `V = C^3` unless a later document explicitly selects an adjoint active-sector realization.

A2 condition (v) is:

```text
rho_A2(g) preserves the selected cubic invariant for every g in G.
```

For the defining representation, the selected cubic invariant is the determinant / volume form:

```text
Omega(v1, v2, v3) = det[v1 v2 v3] = epsilon_ijk v1^i v2^j v3^k
```

Thus the defining-representation version of condition (v) is:

```text
Omega(rho_A2(g)v1, rho_A2(g)v2, rho_A2(g)v3) = Omega(v1, v2, v3)
```

for all `g in G` and all `v1, v2, v3 in C^3`.

## Gell-Mann normalization and adjoint cubic datum

If a later proof-stage document expresses the active sector in adjoint Lie-algebra coordinates, use Gell-Mann normalization:

```text
lambda_a = Gell-Mann matrices
T_a = lambda_a / 2
Tr(T_a T_b) = (1/2) delta_ab
{T_a, T_b} = (1/3) delta_ab I_3 + d_abc T_c
```

The adjoint-coordinate cubic Casimir datum is then:

```text
C3(X) = d_abc x^a x^b x^c
```

for:

```text
X = x^a T_a in su(3)_C
```

This is not the same object as the defining-representation volume form `Omega`. They are complementary cubic data:

- `Omega` lives on the fundamental active space `C^3`.
- `C3` lives on adjoint coordinates.

The C-8 default is the defining-representation condition using `Omega`. Adjoint-coordinate use of `C3` requires an explicit active-sector realization statement.

## Why A2 is the first cubic-Casimir case

The adjoint cubic Casimir has no A1/SU(2) analog. For SU(2), the symmetric invariant tensor `d_abc` vanishes because the anticommutator of Pauli generators closes only through the identity term, not through a nonzero symmetric adjoint tensor.

Thus A2/SU(3) is the first A-type case where a nontrivial adjoint cubic Casimir appears. This is one algebraic reason path beta is the correct A2 convention when the framework asks for degree-3 invariant structure.

This observation is explanatory only. It does not prove A2 minimality.

## Orientation and complex conjugation

The defining volume form `Omega` is orientation-sensitive. Choosing `Omega` rather than `conjugate(Omega)` is part of the A2 condition-level convention.

The fundamental and antifundamental representations of SU(3) are inequivalent:

```text
3 != 3bar
```

Complex conjugation interchanges the two representation choices. It should not be silently absorbed into the active-sector action.

Therefore condition (v) at A2 holds for an active-sector action only if:

1. the action preserves the selected `Omega` convention; and
2. the choice of fundamental `3` versus antifundamental `3bar` is made explicitly at the condition level; and
3. any use of the outer automorphism is declared rather than hidden inside the action.

For the adjoint cubic `d_abc`, the tensor is real and totally symmetric in Gell-Mann normalization. Complex conjugation does not supply an inner equivalence between `3` and `3bar` at the fundamental level; that representation-level choice remains part of the condition.

## Comparison with A1

A1 condition (v):

```text
preserve a degree-2 symplectic pairing on C^2
```

A2 condition (v):

```text
preserve a degree-3 cubic invariant on C^3
```

This suggests the natural schematic pattern:

```text
A_n: preserve a degree-(n+1) active-sector invariant
```

but this document does not formulate or prove the A_n condition. The pattern is heuristic until a future A_n convention document is written.

## C-7 dependency

C-7 remains open until its subgroup candidates are tested against this condition.

In particular, `U(2) = S(U(2) x U(1))` cannot be eliminated or admitted by center containment alone. It must be checked against the chosen cubic-invariant condition.

The full `SU(3)` candidate is expected to preserve the defining volume form by construction, but that expectation is still part of a later proof-stage admissibility argument, not a theorem claim in this document.

## Formal C-8 output

C-8 formulates the following rule:

```text
C-8(v): An A2 active-sector action is C-8-admissible only if it preserves the selected defining-representation cubic invariant Omega and explicitly declares the fundamental versus antifundamental orientation convention. If the active sector is moved to adjoint coordinates, the document must separately require preservation of C3(X) = d_abc x^a x^b x^c under the selected adjoint action.
```

## Non-claims

This document does not prove A2 minimality.

This document does not prove that any proper connected subgroup is eliminated by C-8.

This document does not close C-7.

This document does not promote A2 to theorem-track.

This document does not formulate an A_n theorem family.

This document does not imply any SU(3) lattice gauge theory result.

This document does not cross into `SocioProphet/yang-mills` scope.
