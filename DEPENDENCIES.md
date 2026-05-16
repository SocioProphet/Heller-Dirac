# Dependencies

## Upstream

| Repository | Commit SHA | Cited content |
|---|---|---|
| `SocioProphet/Heller-Godel` | `988307215ad38ccb16514311222184a1b757752b` | Framework objects (`HG-*`); PFK substrate (`PFK-*`); anti-seed discipline |

## Cited objects

### Framework-grade

- `HG-FND-*` — foundational vocabulary.
- `HG-MTH-005` — Universal Bridge formal specification, cited for method-grade transfer constraints.

### PFK operational substrate

- `PFK-SCHEMA-001..004` — claim ledger, Event-IR, proof artifact, and calibration bundle schemas.
- `PFK-OP-001` — Event ingestion for future Heller-Dirac receipt emission.
- `PFK-OP-030` — Calibration for future spectral baseline checks.

### Anti-seed

- `A-MTH-001` — Universal Bridge does not transfer proofs.
- `A-PFK-OP-001` — operator invocation is not evidence.
- `A-PFK-SCHEMA-001` — schema validity is not content validity.
- `A-PFK-VAL-001` — validator green status is not audit completion.

## Forbidden edges

- Heller-Dirac -> any Clay-program repo as a dependency. Heller-Dirac is upstream infrastructure, not a consumer of Clay-program repos.
- Heller-Dirac -> Heller-Godel-other-than-pinned-commit. No floating `main` references.

## Publisher contract

Heller-Dirac publishes `HD-*` identifiers for downstream consumption. Consumers cite Heller-Dirac at a pinned commit, parallel to their Heller-Godel pin:

```text
[HD-FND-001 @ <heller-dirac-pin>]
[HG-MTH-005 @ 988307215ad38ccb16514311222184a1b757752b]
```

Pinned commits are not floating. Version drift discipline from `A-PFK-SCHEMA-002` applies analogously to Heller-Dirac identifier-version drift.
