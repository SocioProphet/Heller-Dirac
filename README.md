# Heller-Dirac

Research capture for the Heller-Dirac programme: Deligne-cohomological phase characters from proof-class generating functions, with reproducible tests and CI.

This repository is deliberately structured as both a manuscript archive and a regression harness. The manuscript captures the mathematical construction; the Python package captures the finite arithmetic layer that can be tested automatically.

## Current Paper I

**Paper I — Deligne-Cohomological Phase Characters from Proof-Class Generating Functions**

Core claim boundary:

- We do **not** claim progress on the Hodge conjecture itself.
- We construct a small Hodge-adjacent test object in the Deligne-cohomological corridor.
- The primary analytic object is a Puiseux singular unit on a branch-killing cover.
- The finite phase character is the monodromy / deck shadow of that unit.
- The finite character is multiplicative.
- The carry cocycle appears only after choosing integer representatives of residues modulo `L`.
- The Deligne cup-product symbol is a separate regulator-symbol refinement; it is not the carry cocycle.

## Repository layout

```text
docs/paper-i/                         Manuscript capture and claim ledger
src/heller_dirac/                     Testable arithmetic and monodromy primitives
tests/                                Regression tests for mechanizable claims
scripts/check_claim_boundaries.py     Manuscript claim-boundary lint
.github/workflows/ci.yml              Reproducibility CI
```

## Reproducibility contract

Every mathematical claim that can be reduced to finite arithmetic should have a regression test. Current tests cover:

- normalization of rational local exponents;
- deck / monodromy character indices;
- `p`-primary and prime reductions;
- strict multiplicativity at the finite-character level;
- carry as section-defect cocycle;
- the carry cocycle identity;
- the fact that the tame symbol is not the carry;
- Catalan / Klein-bottle `mu_2` holonomy bookkeeping;
- manuscript claim-boundary guardrails.

## Local run

```bash
python -m pip install -e .[dev]
pytest -q
python scripts/check_claim_boundaries.py
```

## Status

Initial capture is in place. The open technical work is to expand the manuscript from the captured sections into a submission-ready paper and to add symbolic / proof-assistant coverage for Deligne-side sign conventions where feasible.
