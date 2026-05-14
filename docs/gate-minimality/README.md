# Gate Minimality Lane

Status: active research lane  
Owner: Heller-Dirac  
Scope: A-type singularity gate-minimality, spin-frame conventions, active-set representation choices, and polarization-compatibility conditions

## Purpose

This directory captures the gate-minimality branch of the Heller-Dirac program.

The current center is the A1 minimality theorem and the controlled attempt to extend it to A2 and then An. The extension is not automatic. The A2 sketch shows that higher-singularity gate minimality is convention-dependent: the framework must choose what generalizes the spatial spin-frame, the active-set space, and the A1 symplectic invariant.

## Current artifacts

- `a1-gate-minimality-v3-amendments.md` — mechanical amendments for the A1 proof note.
- `a2-gate-minimality-structural-sketch.md` — pre-proof A2 roadmap and convention gate.
- `claim-boundary.md` — repository-level claim boundary for the lane.

## Current theorem status

A1 may be treated as the only theorem-track object, subject to the v3 amendments being incorporated into the main proof note.

A2 is not theorem-track yet. It is a convention-gated sketch.

An is not theorem-track yet. It is a family of possible theorem programs, not a single established extension.

## Blocking convention gate

No A2 theorem should be drafted until the framework decides among:

1. Path alpha: preserve Spin(3) as spatial target and encode An variation through SU(2) representation dimension plus Frobenius-Schur sign.
2. Path beta: promote the spatial target with n and use the ADE-Lie correspondence, with SU(n+1) as the default candidate.
3. A2 invariant choice: Hermitian, doubled-space symplectic, or cubic invariant.

The current recommendation is path beta with SU(3) and a cubic invariant, but that remains a recommendation until adopted as framework convention.

## Non-claims

This lane does not currently prove A2 minimality.

This lane does not currently establish a canonical An theorem family.

This lane does not currently connect the gate program to physical Dirac operators, Yang-Mills, Hodge, BSD, or runtime interpretability artifacts.
