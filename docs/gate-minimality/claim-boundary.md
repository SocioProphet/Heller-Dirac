# Gate Minimality Claim Boundary

Status: control document  
Track: structural-sketch track with one A1 amendment set  
Scope: claim discipline for `a1-gate-minimality-v3-amendments.md` and `a2-gate-minimality-structural-sketch.md`

## Boundary summary

This lane is a structural-sketch lane, not a completed theorem lane.

The A1 note has a v3 amendment set. Those amendments are mechanical: citation precision, terminal-object placement, and Spin-c tightening. They do not establish A2.

The A2 note is a convention-gated structural sketch. It identifies the path-alpha/path-beta split and recommends path beta with SU(3) plus a cubic invariant as the default working convention. That recommendation is not a theorem and may change when C-6 through C-9 are resolved.

## What A2 currently is

A2 is currently:

- a structural sketch under an explicitly undeclared framework convention;
- a roadmap for making A2 theorem-track after the convention decision;
- a record that A1-to-An extension is convention-dependent;
- a proposed default: path beta, SU(3), cubic invariant.

A2 is not currently:

- a proved A2 gate-minimality theorem;
- a proof that SU(3) is forced across all admissible conventions;
- a general An theorem;
- a gauge-group theorem beyond the stated convention;
- an independently reproduced symbolic proof artifact.

## Load-bearing convention parameter

The load-bearing parameter is the path-alpha/path-beta convention split.

Path alpha preserves the Spin(3) spatial target and pushes An variation into SU(2) representation theory plus Frobenius-Schur signs.

Path beta promotes the spatial target with n and uses the ADE-Lie correspondence, with SU(n+1) as the default candidate. For A2, this gives SU(3) and requires a replacement for the A1 symplectic invariant.

The current recommendation is path beta plus SU(3) plus cubic invariant. This is a framework recommendation, not a derivation.

## Subclaim status

- C-6 is convention-stable. It remains open under either path because the framework must choose path alpha or path beta before T_n is statable.
- C-7 is convention-dependent. It survives as a subgroup-classification obligation, but the target group changes if the convention changes.
- C-8 is path-beta-specific. It applies to the SU(3) plus cubic-invariant convention and must be rewritten if path alpha or another path-beta subcase is adopted.
- C-9 is path-alpha-specific. It applies to the SU(2) Frobenius-Schur branch and is not the load-bearing invariant under SU(3) plus cubic.

## Non-claims

This lane does not establish gate minimality across all admissible conventions.

This lane does not generalize from SU(3) plus cubic to arbitrary gauge groups without further work.

This lane does not claim an independent symbolic reproduction.

This lane does not claim A2 public theorem readiness.

This lane does not claim a physical Dirac-operator theorem.

This lane does not claim implications for Yang-Mills, Hodge, BSD, or runtime interpretability artifacts.

## Substantive documents

- `a1-gate-minimality-v3-amendments.md`
- `a2-gate-minimality-structural-sketch.md`

This file is the control surface over both. It governs what may be claimed from them until Issue #6 resolves the A2 convention decision.
