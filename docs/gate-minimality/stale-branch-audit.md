# Gate-Minimality Stale Branch Audit

Status: audit report only.  
Audited branch: `work/a1-a2-gate-minimality`  
Audit base: `main` after PR #6 merge (`d9e8620aeec540da05aa524e422e3367cf7c28b6`)  
Claim level: repository hygiene / no mathematical claim.

## Purpose

This audit records the remaining unique content on the stale branch `work/a1-a2-gate-minimality` after PR #6 merged the A2 path-beta convention decision.

The stale branch must not be merged as-is. It is behind current `main` and contains out-of-scope drift relative to PR #6.

## Branch state

Comparison:

```text
base: main
head: work/a1-a2-gate-minimality
status: diverged
ahead_by: 11
behind_by: 39
merge_base: 6cca1be64b953a2b6750ebfe1ad013062c2af7c8
```

## File audit

| File | Stale-branch status | Keeper? | Disposition |
|---|---|---:|---|
| `docs/gate-minimality/README.md` | Older gate-minimality local README. Superseded by PR #6, which adopted path beta and removed recommendation/timeline ambiguity. | No direct harvest | Superseded; do not re-merge. |
| `docs/gate-minimality/a1-gate-minimality-v3-amendments.md` | Older A1 amendment file. Superseded by PR #6, including explicit A1-unaffected note. | No direct harvest | Superseded; do not re-merge. |
| `docs/gate-minimality/a2-gate-minimality-structural-sketch.md` | Older A2 sketch. Superseded by PR #6, which added the explicit cubic invariant formula and post-decision C-6/C-7/C-8/C-9 statuses. | No direct harvest | Superseded; do not re-merge. |
| `docs/gate-minimality/claim-boundary.md` | Older claim boundary. Superseded by PR #6 cross-repo boundary and path-beta adopted-convention language. | No direct harvest | Superseded; do not re-merge. |
| `README.md` | Root README rewrite for gate-minimality lane. It predates Heller-Dirac v0.2 Borel-side apparatus and conflicts with the broader repository purpose now on `main`. | Partial only | Archive as stale context; do not replace root README. Any future root README update must integrate current Heller-Dirac v0.2 apparatus and gate-minimality together. |
| `Makefile` | Adds `make validate` and `make validate-gate-minimality` targets calling `tools/validate_gate_minimality.py`. | Yes, conceptually | Harvest later only if paired with an updated validator that matches post-PR #6 adopted-convention semantics. |
| `tools/validate_gate_minimality.py` | Gate-minimality validator. Useful pattern, but stale: it expects unresolved convention wording, default recommendation wording, and open C-6/C-9 statuses. | Yes, after rewrite | Harvest in a follow-up PR as a new post-PR #6 validator; must validate adopted beta, explicit cubic formula, load-bearing C-7/C-8, non-load-bearing C-9, and cross-repo boundary. |

## Keeper material

Keeper material exists, but only as implementation pattern:

1. `Makefile` target shape for a local validation command.
2. `tools/validate_gate_minimality.py` as a validator skeleton.

The stale semantic checks must not be reused directly. They must be rewritten against the post-PR #6 state.

## Recommended follow-up

Open a new scoped PR:

```text
validation: add post-decision gate-minimality guard
```

Expected changes:

- Add `tools/validate_gate_minimality.py`, rewritten for adopted path beta.
- Add `Makefile` targets only if they do not conflict with existing repository validation patterns.
- Check for explicit formula:
  `Omega(v1,v2,v3) = det[v1 v2 v3] = epsilon_ijk v1^i v2^j v3^k`.
- Check C-7 and C-8 are load-bearing.
- Check C-9 is non-load-bearing path-alpha alternative documentation.
- Check `claim-boundary.md` contains the cross-repo non-claim against `SocioProphet/yang-mills` SU(N>=3) lattice mass-gap scope.
- Check no deadline/target-date obligation language is present.

## Branch disposition

Do not delete `work/a1-a2-gate-minimality` yet.

Recommended disposition after review:

1. Harvest validator concept into a clean follow-up PR if desired.
2. Then delete the stale branch after confirming no additional keeper material remains.

## Non-claims

This audit does not merge stale branch content.

This audit does not add validation tooling.

This audit does not change the gate-minimality convention.

This audit does not prove A2 minimality.
