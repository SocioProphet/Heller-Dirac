# Heller-Dirac Identifier Reservations

Status: reservation registry.
Claim level: governance / namespace control only.

This document reserves the `HD-*` namespace for Heller-Dirac scaffold objects. Reservation prevents collision; it does not make a reserved object active.

## Foundational vocabulary — HD-FND

| Identifier range | Reserved scope |
|---|---|
| `HD-FND-001..020` | spectral triple, real structure, grading, KO-dimension, reconstruction-theorem vocabulary, modular representation vocabulary |

Initial named reservations:

- `HD-FND-001` — spectral triple base structure `(A, H, D)`
- `HD-FND-002` — real spectral triple and KO-dimension
- `HD-FND-003` — grading and even/odd structure
- `HD-FND-004` — Connes reconstruction-theorem vocabulary
- `HD-FND-005` — GNS representation interface

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

| Identifier range | Reserved scope |
|---|---|
| `HD-EX-001..005` | canonical examples and fixtures |

Initial named reservations:

- `HD-EX-001` — circle spectral triple fixture
- `HD-EX-002` — free Dirac operator fixture
- `HD-EX-003` — finite spectral triple toy fixture

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

## Activation rule

A reserved `HD-*` identifier becomes active only when a PR adds a dedicated specification or fixture file and updates this registry. Downstream consumers must cite only active identifiers unless explicitly citing a reservation as pending work.
