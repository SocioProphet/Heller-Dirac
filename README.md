# Heller-Dirac

Purpose: co-foundational scaffold beside Heller-Godel, organizing the framework's extended Hopf algebraic, Borel-side analytic, time-theoretic, and field-theoretic content around the spectral-triple substrate.

Where Heller-Godel hosts the proof-theoretic core, PFK substrate, and claim-grade discipline, Heller-Dirac hosts the spectral / modular / Hopf / Borel-side analytic / field-theoretic apparatus that physics-flavored Clay-program content may sit on.

## Scope: three pillars plus Borel-side apparatus

1. Extended Hopf scaffold — Hopf algebras, Hopf algebroids, bicrossed products, Connes-Moscovici-type transverse-geometry carriers, Connes-Kreimer-type renormalization carriers, Birkhoff decomposition, Riemann-Hilbert correspondence, and Hopf-cyclic cohomology.
2. Time theory — Tomita-Takesaki modular flow, KMS structure, thermal time hypothesis, Bisognano-Wichmann correspondence, and type III factor structure of QFT vacuum representations.
3. Field theory — Algebraic QFT (Haag-Kastler), Wightman, constructive field theory, topological field theory (Atiyah-Segal), and factorization-algebra formulations.
4. Borel-side analytic apparatus — spectral zeta vocabulary, Stieltjes constants, heat-kernel asymptotics, Borel transform, Borel-Laplace resummation, alien-derivative normalization, and renormalon boundary discipline.

The unifying object is the spectral triple `(A, H, D)` with optional grading and real structure, equipped with Hopf-algebra actions, modular structure on the GNS representation, and Borel-side analytic transforms where a perturbative/resurgent expansion is explicitly in scope.

## Dependency on Heller-Godel

Heller-Dirac consumes Heller-Godel for:

- PFK substrate: schemas, operator catalog, anti-seed;
- framework objects: `HG-FND-*`, `HG-MTH-005`;
- claim-grade discipline.

Heller-Dirac publishes `HD-*` objects for downstream Clay-program consumption when their content is spectral, modular, Hopf-algebraic, Borel-side analytic, or field-theoretic.

## Identifier namespace

| Prefix | Domain | v0.2 status |
|---|---|---|
| `HD-FND-*` | Foundational vocabulary | active for `HD-FND-001..010`; reserved beyond |
| `HD-HA-*` | Hopf algebra scaffold | active for `HD-HA-001..006`; reserved beyond |
| `HD-TM-*` | Time theory | reserved |
| `HD-FT-*` | Field theory | reserved |
| `HD-SP-*` | Spectral and Borel-side analytic apparatus | active for `HD-SP-001..006`; reserved beyond |
| `HD-EX-*` | Fixtures | active for `HD-EX-001..002`; reserved beyond |
| `HD-MTH-*` | Methodology declarations | active for `HD-MTH-001..003`; reserved beyond |
| `A-HD-*` | Anti-seed register | active register in `docs/anti-seed-dirac.md` |

## Non-claims

This repository does not:

- prove any Clay problem;
- claim that spectral-triple reformulation constitutes proof (`A-HD-NC-001`);
- claim modular flow is physical time outside Bisognano-Wichmann scope (`A-HD-TM-001`);
- claim AQFT axiomatization constructs a theory (`A-HD-FT-001`);
- claim Hopf-scaffold encoding proves renormalizability (`A-HD-HA-001`);
- claim Birkhoff decomposition proves convergence (`A-HD-HA-005`);
- claim Riemann-Hilbert correspondence constructs a physical theory (`A-HD-HA-006`);
- claim Borel transform proves Borel summability (`A-HD-SP-004`);
- claim alien-derivative calculus derives non-perturbative objects (`A-HD-SP-005`);
- claim renormalon analysis proves non-perturbative Yang-Mills existence (`A-HD-SP-006`);
- claim the `gamma_E` synthesis is theorem-grade (`A-HD-MTH-001`);
- transfer methodology into proof-grade content in downstream Clay programs.

## Status

v0.2 active. Borel-side framework-core apparatus is available for downstream method-grade citation. Hopf-side scaffold remains in Heller-Godel plus Temporal Mechanics v0.24.1+; Heller-Dirac v0.2 supplies the Borel-side parallel apparatus.

Subsequent PRs should:

1. extend `HD-HA-*` with Hopf-cyclic computation interfaces;
2. extend `HD-SP-*` with verified Stieltjes-constant computations for specific spectral zeta functions;
3. specify `HD-TM-*` time-theory pillar content;
4. specify `HD-FT-*` field-theory pillar content;
5. create downstream consumer PRs that cite Heller-Dirac v0.2 at pinned commit and declared method grade.
