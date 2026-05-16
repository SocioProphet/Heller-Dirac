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

| Identifier range | Reserved scope |
|---|---|
| `HD-HA-001..010` | Hopf algebras, Hopf algebroids, bicrossed products, Connes-Moscovici, Connes-Kreimer, Hopf-cyclic cohomology |

Initial named reservations:

- `HD-HA-001` — Hopf action on spectral data
- `HD-HA-002` — Connes-Moscovici transverse-geometry anchor
- `HD-HA-003` — Connes-Kreimer renormalization anchor
- `HD-HA-004` — Hopf-cyclic cohomology interface

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

| Identifier range | Reserved scope |
|---|---|
| `HD-SP-001..010` | Dirac operators, spectral action, distance formula, heat-kernel asymptotics, index-theoretic apparatus |

Initial named reservations:

- `HD-SP-001` — Dirac operator apparatus
- `HD-SP-002` — spectral action vocabulary
- `HD-SP-003` — Connes distance formula vocabulary
- `HD-SP-004` — heat-kernel asymptotic interface

## Fixtures — HD-EX

| Identifier | Scope | Status | Path |
|---|---|---|---|
| `HD-EX-001` | circle spectral triple fixture | active | `docs/fixtures/HD-EX-001-circle-spectral-triple.md` |
| `HD-EX-002` | free Dirac operator fixture | reserved | future PR |
| `HD-EX-003` | Hopf-equivariant spectral triple fixture | reserved | future PR |
| `HD-EX-004..005` | future fixtures | reserved | future PR |

## Methodology — HD-MTH

| Identifier range | Reserved scope |
|---|---|
| `HD-MTH-001..005` | methodology declarations for Heller-Dirac scaffold |

Initial named reservations:

- `HD-MTH-001` — Heller-Dirac purpose declaration
- `HD-MTH-002` — downstream citation discipline
- `HD-MTH-003` — spectral/Hopf/modular non-transfer rule

## Anti-seed — A-HD

Active anti-seed identifiers are defined in `docs/anti-seed-dirac.md`:

- `A-HD-NC-001`
- `A-HD-TM-001`
- `A-HD-FT-001`
- `A-HD-HA-001`
- `A-HD-SP-001`
- `A-HD-MTH-001`
- `A-HD-EX-001`
- `A-HD-FND-001`

## Activation rule

A reserved `HD-*` identifier becomes active only when a PR adds a dedicated specification or fixture file and updates this registry. Downstream consumers must cite only active identifiers unless explicitly citing a reservation as pending work.
