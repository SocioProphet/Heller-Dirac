# A2 Gate Minimality - Structural Sketch

Status: pre-proof sketch
Track: structural-sketch track, not theorem track
Proposed tracker: Issue #6 (GitHub issue #1 in this repo)
Convention status: unresolved; path alpha versus path beta remains open
Default recommendation: path beta + SU(3) + cubic invariant
Scope: A2 and An convention gate for the Heller-Dirac gate-minimality program

## Summary

The substantive finding is that the A1 to An extension is not a single theorem. It is a convention-dependent family of possible theorems.

The A1 proof structure can be extended only after the framework specifies three load-bearing choices:

1. what replaces the A1 spatial spin-frame target;
2. what dimension and type the active-set space V_A has for An;
3. what invariant replaces or generalizes the A1 symplectic condition.

Until those choices are fixed, A2 is not theorem-track. It is a convention-gated roadmap.

## Numerical anchors and precision

The numerical and structural anchors in this sketch are exact unless explicitly stated otherwise:

- A1 local monodromy group: Z/2, exact.
- An local monodromy group under path beta: Z/(n+1), exact as a convention-level ADE anchor.
- A2 path-beta central class: Z/3, exact.
- A2 path-beta candidate group: SU(3), exact under the recommended convention.
- A2 path-beta active space: C^3 defining representation, exact under the recommended convention.
- Path-alpha active representation: spin n/2 representation of SU(2), exact as representation-theory convention.
- Frobenius-Schur sign branch under path alpha: half-integer spin is symplectic, integer spin is orthogonal, exact as stated.

No numerical approximation is used in this sketch.

## A.1 What changes from A1 to An

The A1 theorem uses four structural facts that interlock:

| Fact | A1 value | An analog |
|---|---|---|
| Local monodromy group | Z/2 | Z/(n+1) |
| Vanishing-cycle dimension | 1 | n, or n+1 depending convention |
| Spatial spin-frame target | Spin(3) is SU(2) | convention-dependent |
| Active-set V_A | C^2 in the current framework | convention-dependent |
| Invariant on V_A | symplectic | must be reformulated |

The convention-dependent entries are the structural obstruction.

## A.2 Two natural extension paths

### Path alpha: preserve Spin(3)

Keep the spatial target as Spin(3), equivalently SU(2), and let the active-set representation change.

Then the same closed-subgroup argument forces the non-abelian connected option to remain SU(2). Higher An distinctions live in the representation of SU(2) on V_A rather than in the group G.

For V_A of dimension n+1, the active representation is the spin n/2 representation. Its Frobenius-Schur sign alternates:

- half-integer spin gives symplectic type;
- integer spin gives orthogonal type.

Under this path, T_n is essentially T_1 paired with a Frobenius-Schur branching condition.

This path is parsimonious, but it means the gate does not see A_n through a changed spatial group.

### Path beta: promote the spatial target with n

Promote the spatial group with the singularity type. The natural ADE candidate for A_n is SU(n+1), with central element of order n+1.

For A2, the default candidate is SU(3), with central element omega times I_3, where omega is a primitive third root of unity.

This path preserves the ADE-Lie correspondence, but it requires replacing the A1 symplectic invariant because the defining representation of SU(3) is not self-dual.

## A.3 Path alpha candidates

If condition (ii) remains faithful into Spin(3), then G is a closed connected subgroup of SU(2). The only non-abelian option is SU(2).

The active representation then determines the A_n variation:

- dim V_A = 2 gives the defining representation again and degenerates to the A1 gate;
- dim V_A = 3 gives the spin-1 representation, whose invariant form is symmetric, not symplectic;
- dim V_A = n+1 gives spin n/2 and the orthogonal/symplectic alternation by Frobenius-Schur sign.

Conjecture under path alpha: T_n is T_1 plus a Frobenius-Schur branch for condition (v). Odd n and even n fall into different invariant-type cases.

## A.4 Path beta candidates

If the spatial target grows with n, then A2 has several natural candidates:

| Candidate | Center | Natural V_A | Invariant issue |
|---|---|---|---|
| SU(3) | Z/3 | C^3 defining | no invariant bilinear form on V_A x V_A |
| Sp(2), also Spin(5) | Z/2 | C^4 defining | symplectic, but wrong center for A2 monodromy |
| Spin(4), also SU(2) x SU(2) | Z/2 x Z/2 | C^4 bispinor | wrong central cyclic class |

The key obstruction is that SU(n+1)'s defining representation is not self-dual for n >= 2. Therefore the A1 condition using a symplectic form on V_A does not apply directly.

For SU(3), condition (v) has three possible replacements:

1. Hermitian preservation: SU(3) preserves a Hermitian form. This is natural but too automatic.
2. Doubled-space symplectic: act on V_A plus V_A dual with the canonical pairing. This embeds SU(3) into a symplectic group but may select a larger group unless extra structure is added.
3. Cubic invariant: preserve a symmetric trilinear invariant. This is the most distinctive A2 analog of the A1 symplectic invariant.

## A.5 Recommended default

If a default convention must be selected, the current recommendation is:

```text
path beta + SU(3) + cubic invariant
```

Reasons:

- It preserves the ADE-Lie correspondence.
- It realizes the Z/3 loop class by a central order-3 element.
- It gives A2 a genuine group-level distinction from A1.
- The cubic invariant is the natural degree-3 analog of the A1 degree-2 invariant.
- It generalizes toward SU(n+1) and higher-degree invariant data.

This is a recommendation, not a derivation.

## A.6 What must be resolved before A2 is theorem-track

The framework must decide:

1. Whether A_n preserves Spin(3) or promotes the spatial target with n.
2. Whether V_A has SU(2)-representation dimension n+1, SU(n+1) defining dimension n+1, a doubled-space dimension, or another convention.
3. Whether the invariant replacing A1's symplectic condition is orthogonal/symplectic branching, Hermitian preservation, doubled-space symplectic pairing, or cubic preservation.

Once those are fixed, an A2 proof can be written using the A1 proof as template, with one additional technical burden: the classification of closed connected subgroups of SU(3) is more complex than the classification in SU(2).

## A.7 SU(3) proof skeleton under path beta

Under path beta with SU(3) and cubic invariant:

1. Embed G as a closed connected subgroup of SU(3) by the spatial faithfulness condition.
2. Use the closed connected subgroup classification for SU(3).
3. Eliminate discrete and abelian candidates by non-abelianity.
4. Eliminate SO(3), SU(2), and U(2) by the cubic-invariant and central-order-3 requirements.
5. Verify SU(3) satisfies the conditions.
6. Conclude minimality inside the chosen convention.

This proof skeleton is conditional on the convention. It must not be presented as an unconditional A2 theorem.

## A.8 Open subclaims

### C-6: path alpha versus path beta convention decision

Status: open.

Convention dependency: survives every convention. It is the parent decision.

Falsifier: any draft that states T_n or A2 minimality without first selecting path alpha or path beta fails this subclaim.

### C-7: closed connected subgroups of SU(n+1)

Status: open.

Convention dependency: target-dependent. Under path beta for A2, the target is SU(3). Under path alpha, this must be rewritten as an SU(2) representation-theory obligation.

Falsifier: a proposed SU(3) proof that does not eliminate SO(3), SU(2), and U(2), or that uses an incomplete subgroup list, fails this subclaim.

### C-8: cubic-invariant formulation of condition (v) for A2

Status: open.

Convention dependency: path-beta-specific. It is load-bearing only if SU(3) plus cubic invariant is adopted.

Falsifier: if the framework adopts path beta but cannot express the cubic invariant in the framework's polarization language, the SU(3)+cubic theorem path fails.

### C-9: Frobenius-Schur sign for spin n/2 representations

Status: open.

Convention dependency: path-alpha-specific. It is load-bearing only if the framework preserves Spin(3) and uses SU(2) representation dimension/sign as the An variation.

Falsifier: if the orthogonal/symplectic alternation does not match the active-set invariant required by the framework, the path-alpha theorem path fails.

## Non-claims

This note does not prove A2 minimality.

This note does not prove SU(3) is forced without a framework convention.

This note does not establish the An theorem family.

This note does not identify the cubic invariant with a fully defined framework polarization datum. That remains C-8.
