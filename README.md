# Heller-Dirac

Heller-Dirac is the working repository for the gate-minimality branch of the Heller research program: spin-frame, Dirac/ADE, active-set, and polarization-compatibility structures around A-type singularities.

The current repo state is deliberately modest. It captures research notes, convention gates, and proof sketches. It does not claim a completed theorem beyond the explicitly scoped A1 gate-minimality result once its mechanical amendments are incorporated.

## Current canonical lane

The active lane is:

```text
docs/gate-minimality/
```

It currently contains:

- `README.md` — local map and claim discipline.
- `a1-gate-minimality-v3-amendments.md` — mechanical v3 amendments for the A1 gate-minimality note.
- `a2-gate-minimality-structural-sketch.md` — pre-proof A2 structural sketch and convention-gate roadmap.
- `claim-boundary.md` — repository-level claim boundary and non-claims.

## Claim boundary

This repository may currently claim:

- A1 gate minimality has a v3 amendment set that resolves mechanical review issues around the closed-embedding citation, terminal-object phrasing, and Spin^c note.
- The A2 extension is not yet a theorem; it is convention-dependent.
- The A1 to An extension requires an explicit framework choice about the spatial target, active-set dimension/type, and the invariant replacing or generalizing the A1 symplectic condition.

This repository must not currently claim:

- a proved A2 minimality theorem;
- a canonical An theorem family;
- that SU(3) is forced before the framework chooses path beta and the cubic-invariant convention;
- that Neuronpedia, Superconscious, or any runtime harness provides evidence for these mathematical claims;
- that this branch proves anything about physical Dirac operators, Yang-Mills mass gap, Hodge, or BSD.

## Default working recommendation

If a default is needed for the A2 program, the current recommendation is:

```text
path beta + SU(3) + cubic invariant
```

Under that convention, the Z/3 loop class is represented by the central element omega I_3 in SU(3), and the active-set compatibility condition is reformulated using a symmetric cubic invariant rather than the A1 symplectic form.

That recommendation is not a theorem. It is a proposed convention for turning the A2 sketch into a statable theorem.

## Open gate

The first required issue is the A2 convention decision:

1. Does the framework preserve Spin(3) spatial target and push all An variation into SU(2) representation theory and Frobenius-Schur signs?
2. Or does the framework promote the spatial target with n and use the ADE-Lie correspondence, making SU(n+1) the default candidate?
3. What replaces the A1 symplectic condition for A2: Hermitian, doubled-space symplectic, or cubic invariant?

No A2 theorem should be written until this issue is resolved.

## Local validation

```bash
make validate
```

The validator checks that the gate-minimality notes exist and that the A2 sketch remains explicitly pre-proof/convention-gated.
