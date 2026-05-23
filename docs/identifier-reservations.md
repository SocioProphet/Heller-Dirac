# Heller-Dirac Identifier Reservations

Status: reservation and activation registry.
Claim level: governance / namespace control.

This document controls the `HD-*` namespace for Heller-Dirac scaffold objects. Active identifiers have dedicated files and may be cited by downstream consumers at a pinned commit.

## Foundational vocabulary — HD-FND

| Identifier | Scope | Status | Path |
|---|---|---|---|
| `HD-FND-001` | spectral triple base structure `(A, H, D)` | active | `docs/foundations/HD-FND-001-spectral-triple.md` |
| `HD-FND-002` | grading and even spectral triples | active | `docs/foundations/HD-FND-002-grading.md` |
| `HD-FND-003` | real structure and KO-dimension | active | `docs/foundations/HD-FND-003-real-structure.md` |
| `HD-FND-004` | Connes reconstruction theorem reference | active | `docs/foundations/HD-FND-004-connes-reconstruction.md` |
| `HD-FND-005` | Connes distance formula reference | active | `docs/foundations/HD-FND-005-distance-formula.md` |
| `HD-FND-006` | spectral action principle reference | active | `docs/foundations/HD-FND-006-spectral-action.md` |
| `HD-FND-007` | Tomita-Takesaki modular operator and flow | active | `docs/foundations/HD-FND-007-modular-operator.md` |
| `HD-FND-008` | KMS condition | active | `docs/foundations/HD-FND-008-kms.md` |
| `HD-FND-009` | Bisognano-Wichmann correspondence | active | `docs/foundations/HD-FND-009-bisognano-wichmann.md` |
| `HD-FND-010` | Hopf-algebra action on a spectral triple | active | `docs/foundations/HD-FND-010-hopf-action.md` |
| `HD-FND-011..020` | future foundational vocabulary | reserved | future PR |

## Hopf scaffold — HD-HA

| Identifier | Scope | Status | Path |
|---|---|---|---|
| `HD-HA-001` | Hopf action on spectral data | active | `docs/hopf-scaffold/HD-HA-001-hopf-action-on-spectral-data.md` |
| `HD-HA-002` | Connes-Moscovici transverse-geometry anchor | active | `docs/hopf-scaffold/HD-HA-002-connes-moscovici.md` |
| `HD-HA-003` | Connes-Kreimer renormalization anchor | active | `docs/hopf-scaffold/HD-HA-003-connes-kreimer.md` |
| `HD-HA-004` | Hopf-cyclic cohomology interface | active | `docs/hopf-scaffold/HD-HA-004-hopf-cyclic-cohomology.md` |
| `HD-HA-005` | Birkhoff decomposition on Connes-Kreimer Hopf algebra | active | `docs/hopf-scaffold/HD-HA-005-birkhoff-decomposition.md` |
| `HD-HA-006` | Riemann-Hilbert correspondence for perturbative renormalization | active | `docs/hopf-scaffold/HD-HA-006-riemann-hilbert.md` |
| `HD-HA-007..010` | Hopf-cyclic computation interfaces and future Hopf scaffold | reserved | future PR |

## Time theory — HD-TM

| Identifier range | Reserved scope |
|---|---|
| `HD-TM-001..010` | Tomita-Takesaki modular theory, KMS, thermal time, Bisognano-Wichmann scope, type III factor vocabulary |

Initial named reservations:

- `HD-TM-001` — Tomita-Takesaki modular flow
- `HD-TM-002` — KMS condition
- `HD-TM-003` — thermal time hypothesis scope
- `HD-TM-004` — Bisognano-Wichmann correspondence scope

## Field theory — HD-FT

| Identifier range | Reserved scope |
|---|---|
| `HD-FT-001..010` | AQFT, Wightman, constructive field theory, TQFT, factorization algebras |

Initial named reservations:

- `HD-FT-001` — Haag-Kastler local net vocabulary
- `HD-FT-002` — Wightman field-theory vocabulary
- `HD-FT-003` — constructive field-theory boundary
- `HD-FT-004` — Atiyah-Segal TQFT vocabulary
- `HD-FT-005` — factorization-algebra QFT vocabulary

## Spectral apparatus — HD-SP

| Identifier | Scope | Status | Path |
|---|---|---|---|
| `HD-SP-001` | spectral zeta function vocabulary | active | `docs/spectral/HD-SP-001-spectral-zeta.md` |
| `HD-SP-002` | Stieltjes constants of spectral zeta | active | `docs/spectral/HD-SP-002-stieltjes-constants.md` |
| `HD-SP-003` | heat-kernel asymptotic expansion and `gamma_E` | active | `docs/spectral/HD-SP-003-heat-kernel.md` |
| `HD-SP-004` | Borel transform and Borel-Laplace resummation | active | `docs/spectral/HD-SP-004-borel-laplace.md` |
| `HD-SP-005` | Sauzin alien-derivative normalization | active | `docs/spectral/HD-SP-005-alien-derivative.md` |
| `HD-SP-006` | IR-renormalon Borel-plane singularity structure | active | `docs/spectral/HD-SP-006-ir-renormalon.md` |
| `HD-SP-007..010` | future spectral-zeta and Borel-side computations | reserved | future PR |

## Fixtures — HD-EX

| Identifier | Scope | Status | Path |
|---|---|---|---|
| `HD-EX-001` | circle spectral triple fixture | active | `docs/fixtures/HD-EX-001-circle-spectral-triple.md` |
| `HD-EX-002` | Catalan A1 closed-form Borel-plane example | active | `docs/fixtures/HD-EX-002-catalan-a1.md` |
| `HD-EX-003` | free Dirac operator fixture | reserved | future PR |
| `HD-EX-004` | Hopf-equivariant spectral triple fixture | reserved | future PR |
| `HD-EX-005` | future fixture | reserved | future PR |

## Methodology — HD-MTH

| Identifier | Scope | Status | Path |
|---|---|---|---|
| `HD-MTH-001` | `gamma_E` synthesis as universal first-subleading constant across four threads | active | `docs/methodology/HD-MTH-001-gamma-E-synthesis.md` |
| `HD-MTH-002` | Hopf-side / Borel-side framework parallel | active | `docs/methodology/HD-MTH-002-hopf-borel-parallel.md` |
| `HD-MTH-003` | Catalan A1 as Hopf-side / Borel-side bridge fixture | active | `docs/methodology/HD-MTH-003-catalan-bridge.md` |
| `HD-MTH-004..005` | methodology declarations for promotion criteria and downstream citation discipline | reserved | future PR |

## Anti-seed — A-HD

Active anti-seed identifiers are defined in `docs/anti-seed-dirac.md`:

- `A-HD-NC-001`
- `A-HD-TM-001`
- `A-HD-FT-001`
- `A-HD-HA-001`
- `A-HD-HA-005`
- `A-HD-HA-006`
- `A-HD-SP-001`
- `A-HD-SP-004`
- `A-HD-SP-005`
- `A-HD-SP-006`
- `A-HD-MTH-001`
- `A-HD-MTH-002`
- `A-HD-MTH-003`
- `A-HD-EX-001`
- `A-HD-FND-001`

## Activation rule

A reserved `HD-*` identifier becomes active only when a PR adds a dedicated specification or fixture file and updates this registry. Downstream consumers must cite only active identifiers unless explicitly citing a reservation as pending work.
