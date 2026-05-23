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

## A2 convention status

A2 is currently:

- an adopted path-beta structural convention;
- a candidate theorem track only after C-7 and C-8 are closed;
- a record that A1-to-An extension is convention-dependent;
- explicitly scoped to structural gate-minimality inside Heller-Dirac.

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
- C-7: active and load-bearing. It must analyze the closed connected subgroup classification obligation for SU(3) under the adopted gate criteria.
- C-8: active and load-bearing. It must formulate the cubic-invariant analog of A1 condition (v), including orientation and non-self-duality handling.
- C-9: demoted to non-load-bearing path-alpha alternative documentation.

## Non-claims for this PR

This PR does not prove A2 minimality.

This PR does not authorize an A_n theorem family.

This PR does not imply any SU(3) lattice gauge theory result. That scope belongs to `SocioProphet/yang-mills` and is non-claimed there.

This PR does not transfer content into Yang-Mills, Hodge, BSD, Navier-Stokes, runtime interpretability, or any other downstream program.

## Cross-repo boundary

A2 gate-minimality in this repository is structural. SU(N>=3) lattice mass-gap work in `SocioProphet/yang-mills` is a disjoint scope and is non-claimed there.

No PR may cross this boundary without an explicit ledger entry.

## Substantive documents

- `a1-gate-minimality-v3-amendments.md`
- `a2-gate-minimality-structural-sketch.md`
- `README.md`

This file is the control surface over the lane. It governs what may be claimed from the gate-minimality documents until C-7 and C-8 are closed.