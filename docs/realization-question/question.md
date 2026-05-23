# The Realization Question

Status: open question.  
Owner: `SocioProphet/Heller-Dirac`.  
Claim level: question only; no theorem claim and no cross-repo import.  
Related boundary: `docs/gate-minimality/claim-boundary.md`.

## Statement

The gate-minimality program in `SocioProphet/Heller-Dirac` defines an algebraic structure.

At A1, the minimal single-group realization is:

```text
Spin(3) ~= SU(2)
```

with central element:

```text
zeta = -I
```

active sector the irreducible two-dimensional spinor representation, and condition (v) the symplectic form on `C^2`.

At A2 under the adopted path beta, the structure extends to:

```text
SU(3) with central Z/3 and cubic invariant
Omega(v1,v2,v3) = epsilon_ijk v1^i v2^j v3^k
```

The lattice Yang-Mills work in `SocioProphet/yang-mills` defines an operational structure. Its v0.14.4 anchor is scoped to pure `SU(2)` Wilson lattice gauge theory at fixed spacing `a > 0`, coupling window:

```text
beta < beta* = 0.006296889394074993
```

and a positive transfer gap above the vacuum in the infinite-volume gauge-invariant Osterwalder-Seiler reflection-positive Hilbert space.

The question:

```text
Do the algebraic A1 gate-minimality data have a corresponding operational realization in lattice Yang-Mills structures?
```

This is a question, not a conjecture.

## Candidate realizations

The following are candidate sites where a realization might be found. Listing them does not assert any of them works.

### Candidate 1: lattice Dirac spectral flow

In a lattice formulation that includes a Dirac operator `D[U]` in an `SU(2)` gauge background `U`, the spinor index space at each site carries the fundamental representation of `SU(2)`.

A closed loop `gamma` in the space of gauge configurations induces spectral flow of:

```text
D[U(t)],  t in [0,1],  U(0) = U(1)
```

The mod-2 spectral flow index along `gamma` is a candidate for a Heller-Dirac Lyapunov-cycle object. The central element:

```text
zeta = -I
```

would correspond to a configuration loop that produces odd spectral flow.

Reference lineage for the lattice Dirac formulation:

- Hasenfratz, Laliena, Niedermayer: Ginsparg-Wilson relation.
- Neuberger: overlap operator.
- Luscher: chiral lattice symmetry.

This candidate would live in a fermionic extension. Pure-bosonic Wilson Yang-Mills does not contain a Dirac operator and therefore does not directly host this candidate.

### Candidate 2: transfer-matrix center action

The Yang-Mills transfer matrix `T` on the Osterwalder-Seiler Hilbert space may carry an action of global gauge transformations modulo local ones.

The center:

```text
Z(SU(2)) = Z/2
```

acts on sectors labeled by center charge. The element:

```text
zeta = -I in Spin(3)
```

is the nontrivial center element, and its action on transfer-matrix eigenstates is a candidate realization of the A1 spin-gate witness.

This candidate would not require a Dirac operator. It would require:

1. identifying the action of `Z(SU(2))` on the Osterwalder-Seiler Hilbert space;
2. identifying whether condition (v), symplectic preservation on the `C^2` active sector, has a meaningful translation in transfer-matrix sector pairings or matrix elements;
3. proving that the construction is internal to the Yang-Mills scope before any cross-repo claim can be made.

### Candidate 3: path-beta extension to SU(3)

For A2 under path beta, the analogous question concerns `SU(3)` lattice gauge theory rather than the current `SU(2)` Yang-Mills theorem-track anchor.

`SocioProphet/yang-mills` explicitly non-claims any `SU(N>=3)` lattice mass-gap theorem. Therefore this candidate cannot be hosted by that repository's current theorem scope.

The question of whether the A2 cubic-invariant condition has an `SU(3)` lattice realization is recorded here for completeness, not for immediate theorem work.

## Boundary with Yang-Mills

This document does not alter the local cross-repo boundary recorded in:

```text
docs/gate-minimality/claim-boundary.md
```

and in the Yang-Mills claim-boundary surface.

Heller-Dirac owns this question because it originates from Heller-Dirac gate-minimality data. Yang-Mills owns its own operational lattice claims. A future result must decide its destination repository at that time and must add paired local boundary entries if the result crosses repositories.

## Non-claims

This document does not claim any candidate realization exists.

This document does not assert that Heller-Dirac and Yang-Mills are coherent.

This document does not import any Yang-Mills theorem into Heller-Dirac.

This document does not extend either repository's theorem-track.

This document does not assign any candidate to a destination repository in advance.

This document does not authorize a literature hunt or proof attempt against any candidate without separate scope work.

This document does not weaken the existing cross-repo boundary discipline.

## Disposition

If progress is made on any candidate, the result remains in this directory as a question/scope artifact until it matures enough to justify a destination.

Destination is decided per result, with paired local boundary entries between this repository and the chosen destination repository.

If no progress is made on any candidate, the question remains open. That is an acceptable outcome.
