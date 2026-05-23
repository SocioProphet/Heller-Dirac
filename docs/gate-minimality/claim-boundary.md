# Gate Minimality Claim Boundary

Status: control document  
Track: structural-sketch track with one A1 theorem-track amendment set  
Scope: claim discipline for `a1-gate-minimality-v3-amendments.md` and `a2-gate-minimality-structural-sketch.md`

## Boundary summary

This lane is a structural-sketch lane except for the A1 theorem-track amendment set.

A1 remains governed by the existing Spin(3) ~= SU(2) setting and its degree-2 symplectic condition.

A2 now has an adopted convention:

```text
path beta + SU(3) + central Z/3 + cubic invariant
```

This adoption resolves the A2 convention gate. It does not prove A2 minimality and does not promote A2 to theorem-track.

## Relocation note

The current C-7 and C-8 proof-character obligations have been relocated to `SocioProphet/Heller-Godel`:

```text
SocioProphet/Heller-Godel/docs/gate-minimality/c7-su3-subgroup-classification-scope.md
SocioProphet/Heller-Godel/docs/gate-minimality/c8-cubic-invariant-condition.md
```

This reflects the corrected architecture: the gate-minimality pipeline at `p = 2` and `p = 3` is Heller-Godel content, part of the `chi_p` / `zeta_p` / proof-character framework. Heller-Dirac retains the historical path-beta adoption context, A1 amendment hygiene, redirect stubs, and local non-claim boundaries.

## A2 convention status

A2 is currently:

- an adopted path-beta structural convention;
- a candidate theorem track only after C-7 and C-8 are closed in Heller-Godel;
- a record that A1-to-An extension is convention-dependent;
- historically scoped to structural gate-minimality in this Heller-Dirac adoption record.

A2 is not currently:

- a proved A2 gate-minimality theorem;
- an authorization for a general A_n theorem family;
- a proof that SU(3) is forced outside the path-beta convention;
- a physical or lattice-gauge theorem;
- an independently reproduced symbolic proof artifact.

## Load-bearing convention parameter

The adopted A2 convention is path beta.

Path beta promotes the spatial target with n and uses the ADE-Lie correspondence. For A2 this gives SU(3), central Z/3, and the cubic invariant as the analog of the A1 degree-2 symplectic invariant.

Path alpha is retained only as an alternative documentation path: preserve Spin(3) and encode A_n variation through SU(2) representation dimension and Frobenius-Schur signs.

## Subclaim status

- C-6: resolved to path beta for A2.
- C-7: active and load-bearing in Heller-Godel. It must analyze the closed connected subgroup classification obligation for SU(3) under the adopted gate criteria.
- C-8: active and load-bearing in Heller-Godel. It must formulate and close the cubic-invariant analog of A1 condition (v), including orientation and non-self-duality handling.
- C-9: demoted to non-load-bearing path-alpha alternative documentation.

## Non-claims for this PR

This PR does not prove A2 minimality.

This PR does not authorize an A_n theorem family.

This PR does not imply any SU(3) lattice gauge theory result. That scope belongs to `SocioProphet/yang-mills` and is non-claimed there.

This PR does not transfer content into Yang-Mills, Hodge, BSD, Navier-Stokes, runtime interpretability, or any other downstream program.

## Cross-repo boundaries

### `SocioProphet/yang-mills`

The A2 gate-minimality program in this repository is structurally disjoint from the scope of `SocioProphet/yang-mills`.

This repository's A2 work concerns algebraic gate-minimality structure for:

```text
path beta + SU(3) + central Z/3 + cubic invariant
```

It does not claim, and does not contribute to, any lattice gauge theory result, mass-gap theorem, Borel-summability statement, continuum-limit construction, weak-coupling theorem, or asymptotic-freedom analysis.

`SocioProphet/yang-mills` explicitly non-claims any `SU(N>=3)` lattice mass-gap result. The exact boundary phrase is: SU(N>=3) lattice mass-gap is outside this repository's gate-minimality claim surface. SU(3) gate-minimality content from this repository does not appear in the operational theorem scope of that repository.

`SocioProphet/yang-mills` Lane VIII operates on pure `SU(2)` under Reading Z: the `G2` subscript is the gluon condensate / action-density proxy `G^2`, not the exceptional Lie group and not an A2/SU(3) alignment.

This boundary entry is local to Heller-Dirac. It is a pointer to the paired Yang-Mills boundary entry, not a central authority over the Yang-Mills repository.

Crossing rule: any PR in either repository whose content would import, depend on, or claim coherence with the other repository's scope must add a corresponding local boundary entry in both repositories in the same PR sequence. Such a crossing must not merge in either repository until both local entries are present.

Current Yang-Mills reference surfaces:

- `SocioProphet/yang-mills` `docs/lane-viii-conventions.md` — Reading Z adoption.
- `SocioProphet/yang-mills` `manuscripts/lane-viii-borel-laplace/v0.2.3-FRI/residue-hunt-scope.md` — pure `SU(2)` residue-hunt scope with no value admitted.
- `SocioProphet/yang-mills` `docs/claim-boundary.md` — paired cross-repo boundary surface.

## Substantive documents

- `a1-gate-minimality-v3-amendments.md`
- `a2-gate-minimality-structural-sketch.md`
- `c7-su3-subgroup-classification-scope.md` — redirect stub to Heller-Godel.
- `c8-cubic-invariant-condition.md` — redirect stub to Heller-Godel.
- `README.md`

This file is the control surface over the Heller-Dirac side of the lane. Current C-7/C-8 content is owned by Heller-Godel.