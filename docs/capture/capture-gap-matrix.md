# Heller-Dirac v0.2 Capture-Gap Matrix

Status: v0.2 capture ledger.  
Claim level: governance / capture discipline only.

## Upstream authority

Primary synthesis authority: Temporal Mechanics manuscript v0.24.2, Section 12.7.

Heller-Godel dependency remains pinned at:

```text
988307215ad38ccb16514311222184a1b757752b
```

No direct chat tranche is treated as a repository source. Consumer-repo updates are deferred.

## Deliverable mapping

| Deliverable | File surface | Status |
|---|---|---|
| D1 | `docs/identifier-reservations.md` | captured |
| D2-D4 | `docs/hopf-scaffold/HD-HA-003*`, `HD-HA-005*`, `HD-HA-006*` | captured |
| D5-D9 | `docs/spectral/HD-SP-001*` through `HD-SP-006*` | captured |
| D10-D12 | `docs/methodology/HD-MTH-001*` through `HD-MTH-003*`; `docs/fixtures/HD-EX-002*` | captured |
| D13 | `docs/anti-seed-dirac.md` | captured |
| D14 | `README.md`; `docs/scope.md` | captured |
| D15 | `docs/capture/capture-gap-matrix.md` | captured |
| D16 | `docs/scope/v0.2-non-claim-box.md` | captured |
| D17 | `.github/workflows/heller-dirac-pfk-dependency.yml`; `tests/test_pfk_dependency.py` | captured |

## Intentional adjustments

1. Existing `HD-FND-001..010` files were not modified. The foundational-pause condition was not triggered.
2. `HD-EX-002` is activated as the Catalan A1 fixture. The free-Dirac fixture is moved to reserved `HD-EX-003`.
3. `HD-MTH-002` landed at `docs/methodology/HD-MTH-002-framework-parallel.md`.
4. Follow-up polish expanded `HD-HA-005`, `HD-SP-003`, `HD-SP-006`, and `HD-MTH-002` while preserving claim boundaries.
5. No excluded content was copied into the repository.

## Validation surface

The v0.2 validation checks file presence, active identifier registry entries, anti-seed entries, the unchanged Heller-Godel pin, and forbidden token absence.

## Trust-surface declaration

This v0.2 work is document-only. No executable trust-surface authority is introduced.
