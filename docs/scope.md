# Heller-Dirac Scope

Status: purpose scaffold.  
Claim level: methodological / foundational vocabulary; no theorem claim.

## Unifying substrate

The working substrate is the spectral triple:

```text
(A, H, D)
```

where `A` is an involutive algebra represented on a Hilbert space `H`, and `D` is a self-adjoint operator with compact-resolvent-style spectral control and bounded commutators `[D, a]` where defined.

Optional grading and real structure enrich this base:

```text
(A, H, D, gamma, J)
```

By Connes' reconstruction theorem, under the commutative hypotheses and the full first-order, orientability, regularity, finiteness, and Poincare-duality package, the spectral triple recovers a compact Riemannian spin manifold and `D` is the Dirac operator. This repository treats that statement as orientation for vocabulary, not as a theorem newly proved here.

## Pillar 1: extended Hopf scaffold

The Hopf scaffold studies Hopf algebras, Hopf algebroids, bicrossed products, and matched-pair constructions acting on spectral data.

Anchor examples:

- Connes-Moscovici transverse geometry and Hopf-cyclic cohomology.
- Connes-Kreimer renormalization Hopf algebra and Birkhoff-factorization structure.
- Hopf algebroid and bicrossed-product extensions over noncommutative bases.

Non-claim: organizing a calculation by Hopf algebra does not prove renormalizability or non-perturbative existence.

## Pillar 2: time theory

The time-theory pillar studies Tomita-Takesaki modular structure.

For a von Neumann algebra `M` with cyclic separating vector, modular data produce a modular automorphism group. Connes' thermal time hypothesis treats time as state-dependent modular flow. Bisognano-Wichmann supplies a precise physical correspondence in the vacuum wedge setting of Wightman QFT, where modular flow matches Lorentz boosts.

Non-claim: modular flow is not automatically physical time outside the hypotheses that identify it with physical evolution.

## Pillar 3: field theory

The field-theory pillar studies rigorous QFT formalisms:

- Haag-Kastler algebraic QFT local nets.
- Wightman operator-valued distributions.
- Constructive field theory.
- Atiyah-Segal topological field theory.
- Costello-Gwilliam factorization algebras.

The Dirac operator enters these layers through fermionic fields, index-theoretic invariants, spectral action, and local-to-global observables.

Non-claim: axiomatizing a field theory is not constructing it. Constructive existence remains a separate mathematical burden.

## Relation to Heller-Godel

Heller-Godel supplies claim discipline, PFK schema infrastructure, and framework-method constraints such as `HG-MTH-005`. Heller-Dirac supplies the spectral / modular / Hopf / field-theoretic apparatus for downstream use.

No Heller-Dirac object may be cited as proof-transfer into a Clay-program repository. It may be cited only at the declared grade and pinned commit.
