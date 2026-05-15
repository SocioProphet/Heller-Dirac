# Heller-Dirac

Purpose: co-foundational scaffold beside Heller-Godel, organizing the framework's extended Hopf algebraic, time-theoretic, and field-theoretic content around the spectral-triple substrate.

Where Heller-Godel hosts the proof-theoretic core, PFK substrate, and claim-grade discipline, Heller-Dirac hosts the spectral / modular / Hopf / field-theoretic apparatus that physics-flavored Clay-program content may sit on.

## Scope: three pillars

1. Extended Hopf scaffold — Hopf algebras, Hopf algebroids, bicrossed products, Connes-Moscovici-type transverse-geometry carriers, Connes-Kreimer-type renormalization carriers, and Hopf-cyclic cohomology.
2. Time theory — Tomita-Takesaki modular flow, KMS structure, thermal time hypothesis, Bisognano-Wichmann correspondence, and type III factor structure of QFT vacuum representations.
3. Field theory — Algebraic QFT (Haag-Kastler), Wightman, constructive field theory, topological field theory (Atiyah-Segal), and factorization-algebra formulations.

The unifying object is the spectral triple `(A, H, D)` with optional grading and real structure, equipped with Hopf-algebra actions and modular structure on the GNS representation.

## Dependency on Heller-Godel

Heller-Dirac consumes Heller-Godel for:

- PFK substrate: schemas, operator catalog, anti-seed;
- framework objects: `HG-FND-*`, `HG-MTH-005`;
- claim-grade discipline.

Heller-Dirac publishes `HD-*` objects for downstream Clay-program consumption when their content is spectral, modular, Hopf-algebraic, or field-theoretic.

## Identifier namespace

| Prefix | Domain |
|---|---|
| `HD-FND-*` | Foundational vocabulary |
| `HD-HA-*` | Hopf algebra scaffold |
| `HD-TM-*` | Time theory |
| `HD-FT-*` | Field theory |
| `HD-SP-*` | Spectral apparatus |
| `HD-EX-*` | Fixtures |
| `HD-MTH-*` | Methodology declarations |
| `A-HD-*` | Anti-seed register |

## Non-claims

This repository does not:

- prove any Clay problem;
- claim that spectral-triple reformulation constitutes proof (`A-HD-NC-001`);
- claim modular flow is physical time outside Bisognano-Wichmann scope (`A-HD-TM-001`);
- claim AQFT axiomatization constructs a theory (`A-HD-FT-001`);
- claim Hopf-scaffold encoding proves renormalizability (`A-HD-HA-001`);
- transfer methodology into proof-grade content in downstream Clay programs.

## Status

Scaffold declaration. No apparatus implemented yet.

Subsequent PRs should:

1. draft `HD-FND-*` foundational vocabulary;
2. specify the spectral-triple base structure;
3. add `HD-EX-*` canonical fixtures such as the circle spectral triple and free Dirac operator examples;
4. specify modular-flow apparatus and Bisognano-Wichmann scope;
5. specify Hopf-scaffold catalog entries with Connes-Moscovici and Connes-Kreimer anchor examples;
6. cross-reference into Heller-Godel `HG-MTH-006..010` as those drafts land.
