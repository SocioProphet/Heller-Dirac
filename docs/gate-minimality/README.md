# Gate Minimality Lane

Status: active research lane  
Owner: Heller-Dirac  
Scope: A-type singularity gate-minimality, spin-frame conventions, active-set representation choices, and polarization-compatibility conditions

## Purpose

This directory captures the gate-minimality branch of the Heller-Dirac program.

The current center is the A1 minimality theorem and the controlled attempt to extend it to A2 and then An. The extension is not automatic. The A2 sketch shows that higher-singularity gate minimality is convention-dependent: the framework must choose what generalizes the spatial spin-frame, the active-set space, and the A1 symplectic invariant.

## Current artifacts

- `a1-gate-minimality-v3-amendments.md` — mechanical amendments for the A1 proof note.
- `a2-gate-minimality-structural-sketch.md` — A2 roadmap under adopted path-beta convention.
- `claim-boundary.md` — repository-level claim boundary for the lane.

## Convention-status table

| Track | Convention status | Theorem status |
|---|---|---|
| A1 | closed convention: Spin(3) ~= SU(2), degree-2 symplectic invariant | theorem-track subject to v3 amendment hygiene |
| A2 | convention adopted: path beta, SU(3), central Z/3, cubic invariant | structural sketch; not theorem-track until C-7 and C-8 close |
| An | future convention family | not theorem-track |

## Adopted A2 convention

The adopted A2 convention is:

```text
path beta + SU(3) + central Z/3 + cubic invariant
```

This replaces the earlier default recommendation. It is now the Heller-Dirac structural convention for A2.

The cubic-invariant subcase is adopted. Hermitian preservation and doubled-space symplectic preservation remain documented alternatives but are not theorem-track for A2.

## Blocking obligations for A2 theorem-track promotion

A2 remains structural-sketch until both load-bearing obligations close:

1. C-7: SU(3) closed connected subgroup classification obligation under the adopted gate criteria.
2. C-8: cubic-invariant analog of A1 condition (v), including orientation and non-self-duality handling.

C-9 is retained only as path-alpha alternative documentation.

## Non-claims

This lane does not currently prove A2 minimality.

This lane does not currently establish a canonical An theorem family.

This lane does not currently connect the gate program to physical Dirac operators, Yang-Mills, Hodge, BSD, or runtime interpretability artifacts.

This lane does not imply any SU(3) lattice gauge theory result.