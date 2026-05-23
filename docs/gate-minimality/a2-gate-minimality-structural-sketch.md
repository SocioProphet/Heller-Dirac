# A2 Gate Minimality — Structural Sketch

Status: convention adopted; theorem-track not yet promoted  
Track: structural-sketch track, not theorem track  
Tracker: Issue #1  
Convention status: path beta adopted for A2  
A2 invariant subcase: cubic invariant with explicit determinant formula  
Scope: A2 and future An convention gate for the Heller-Dirac gate-minimality program

## Summary

The A1 to An extension is not a single automatic theorem. It is a convention-dependent family of possible theorem programs.

For A2, this repository adopts path beta:

```text
A2 spatial target: SU(3)
central class: Z/3, represented by omega I_3
active space: C^3 defining representation
invariant subcase: cubic invariant Omega(v1,v2,v3) = det[v1 v2 v3] = epsilon_ijk v1^i v2^j v3^k
```

This is a convention adoption. It is not an A2 minimality proof.

## A.1 What changes from A1 to An

The A1 theorem uses structural facts that interlock:

| Fact | A1 value | A2 path-beta convention |
|---|---|---|
| Local monodromy group | Z/2 | Z/3 |
| Spatial target | Spin(3) ~= SU(2) | SU(3) |
| Active-set space | C^2 | C^3 |
| Active invariant | degree-2 symplectic form | degree-3 cubic invariant `Omega(v1,v2,v3) = epsilon_ijk v1^i v2^j v3^k` |

A2 is theorem-track only after the open load-bearing conditions below are closed.

## A.2 Adopted convention: path beta

Path beta promotes the spatial target with the singularity type. Under the ADE-Lie correspondence, A2 uses SU(3), with central Z/3.

The adopted A2 invariant subcase is the cubic invariant, not Hermitian preservation and not doubled-space symplectic preservation.

The defining-representation cubic datum is the SU(3)-invariant volume form:

```text
Omega(v1, v2, v3) = det[v1 v2 v3] = epsilon_ijk v1^i v2^j v3^k
```

Equivalently, if C-8 later formulates the active sector in adjoint coordinates, the expected cubic Casimir datum is:

```text
C3(X) = d_abc x^a x^b x^c
```

where `d_abc` are the symmetric SU(3) structure constants in Gell-Mann normalization. C-8 must choose and type the active-sector realization explicitly.

The cubic invariant is the natural degree-3 analog of A1's degree-2 symplectic invariant. It is also the subcase that distinguishes the A2 center directly, rather than encoding A2 data into a fixed Spin(3) chassis.

## A.3 Non-adopted alternatives

The following alternatives remain documented but are not the A2 theorem-track convention:

1. Hermitian preservation. Natural for SU(3), but too automatic to play the role of A1 condition (v).
2. Doubled-space symplectic preservation. Useful as a representation trick, but it shifts the invariant into a doubled space and does not directly encode the central Z/3 A2 datum.
3. Path alpha. Preserves Spin(3) ~= SU(2) and encodes A_n variation through SU(2) representation dimension and Frobenius-Schur sign. This is retained as C-9 alternative documentation only.

## A.4 Load-bearing conditions

### C-7: SU(3) closed connected subgroup classification obligation

Status: active, load-bearing.

A future A2 theorem statement must use a complete closed connected subgroup classification for SU(3), then show which candidates are admissible under the A2 gate criteria.

This deliverable is not a re-derivation of the classification theorem. It is the admissibility analysis required by the adopted convention.

### C-8: cubic-invariant analog of condition (v)

Status: active, load-bearing.

A future A2 theorem statement must formulate the cubic-invariant analog of A1 condition (v). It must define the preserved cubic datum on C^3, specify the orientation/volume-form choice, and explain how complex conjugation is handled because the defining SU(3) representation is not self-dual.

Failure to express this invariant in the framework's polarization language blocks theorem-track promotion.

## A.5 Non-load-bearing condition

### C-9: path-alpha alternative

Status: demoted to non-load-bearing under the adopted A2 convention.

C-9 remains as documentation of the path-alpha alternative: preserve Spin(3), use SU(2) representation dimension, and track Frobenius-Schur sign. It is not load-bearing for the path-beta A2 theorem track.

## A.6 Convention decision status

C-6 is resolved to path beta for A2.

```text
Selected path: beta
Selected A2 group: SU(3)
Selected A2 center: Z/3
Selected A2 invariant: cubic invariant Omega(v1,v2,v3) = epsilon_ijk v1^i v2^j v3^k
```

A2 remains structural-sketch status until C-7 and C-8 are closed.

## A.7 Proof skeleton under adopted path beta

Under path beta with SU(3) and cubic invariant:

1. Embed G as a closed connected subgroup of SU(3) by the spatial faithfulness condition.
2. Use the closed connected subgroup classification for SU(3).
3. Eliminate candidates that fail the central Z/3 condition or the cubic-invariant condition.
4. Verify SU(3) satisfies the adopted conditions.
5. Conclude minimality inside the adopted convention only.

This is a proof skeleton, not a proof.

## Non-claims

This note does not prove A2 minimality.

This note does not authorize an A_n theorem family.

This note does not claim SU(3) is forced outside the adopted path-beta convention.

This note does not imply any SU(3) lattice gauge theory result.

This note does not transfer content into SocioProphet/yang-mills.
