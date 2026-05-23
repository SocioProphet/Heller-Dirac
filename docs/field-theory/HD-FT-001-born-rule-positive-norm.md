# HD-FT-001 — Born Rule Positive-Norm Bridge

Status: field-theory methodology surface.  
Owner: `SocioProphet/Heller-Dirac`.  
Identifier: `HD-FT-001`.  
Claim level: methodology / boundary vocabulary only; no theorem promotion.

## Purpose

This note records the Heller-Dirac portion of the Born-rule lineage.

The relevant problem is not that Heller-Dirac derives the Born rule. It does not. The relevant problem is that relativistic quantum theory must provide a positive probability-bearing state space before measurement probabilities can be interpreted.

The Born-rule chain therefore enters Heller-Dirac through:

1. positive inner product and norm discipline;
2. conserved probability current;
3. the Dirac equation as the first-order relativistic equation whose density `psi^dagger psi` is positive;
4. field-theoretic reinterpretation of negative-frequency solutions through particles and antiparticles;
5. the distinction between field-theory apparatus and proof-grade claims in downstream repositories.

## Core lineage

The nonrelativistic Born rule assigns probabilities by:

```text
P(x) dx = |psi(x)|^2 dx
```

This requires a nonnegative density.

The Klein-Gordon conserved current has an indefinite time component, so its conserved charge is not a probability density for a one-particle wavefunction in the same direct sense.

The Dirac equation repairs the positive-density problem at the one-particle level by using a first-order equation with spinor-valued states:

```text
rho = psi^dagger psi >= 0
```

and a conserved current:

```text
j^mu = bar(psi) gamma^mu psi.
```

This is the Heller-Dirac-relevant point: the Dirac-side apparatus is a positive-norm and current-conservation bridge into field-theoretic measurement vocabulary.

## Repository routing

The Born-rule material splits across repositories.

### Heller-Dirac

Heller-Dirac owns the field-theory and positive-norm side:

- Dirac spinors and gamma-matrix field-theory vocabulary;
- positive state-space discipline;
- probability-current lineage;
- QFT/Fock-space reinterpretation of particle and antiparticle modes;
- spectral, modular, Hopf, Borel-side, and field-theoretic apparatus as method-grade support.

### Heller-Einstein

Heller-Einstein owns typed-interface and projection-induced stochasticity vocabulary. Its `HE-PROJ-001` theorem produces Markov kernels from deterministic latent dynamics under many-to-one trace maps. That theorem does not derive the Born rule. Heller-Dirac may cite Heller-Einstein only as interface vocabulary when comparing projection-induced stochasticity with Hilbert-space measurement.

### Yang-Mills

Yang-Mills owns gauge-invariant physical Hilbert-space discipline and mass-gap claim boundaries. Heller-Dirac may supply field-theory apparatus vocabulary, but Yang-Mills owns any statement about gauge-invariant observable algebras, reflection-positive Hilbert spaces, transfer gaps, or mass gaps.

## Bridge obligations

A future artifact comparing Heller-Dirac field theory to Born-rule measurement must supply at least:

1. a positive state space or algebraic state space;
2. a conserved current or state/effect pairing;
3. a clear measurement event/effect vocabulary;
4. an account of how gauge or field redundancies are removed before probability interpretation;
5. a non-claim boundary preventing field-theory vocabulary from becoming a proof of quantum mechanics or a Clay-program result.

## Relationship to QFT

In modern quantum field theory, the one-particle Dirac-sea heuristic is replaced by field operators on Fock space. Negative-frequency spinor solutions are reinterpreted through antiparticle creation operators.

That modern QFT picture is the safer Heller-Dirac vocabulary:

```text
field modes + positive Hilbert/Fock structure + observable algebra + state/effect pairing.
```

The Dirac sea can remain historical motivation, but it should not be used as the authoritative formal vacuum structure for downstream Yang-Mills claims.

## Non-claims

This document does not prove the Born rule.

This document does not derive quantum mechanics.

This document does not prove that the Dirac equation uniquely forces the Born rule.

This document does not claim that Klein-Gordon theory is invalid as quantum field theory.

This document does not claim a Yang-Mills mass gap.

This document does not import Heller-Einstein projection-induced stochasticity as a quantum-measurement derivation.

This document does not import Yang-Mills theorem-track content into Heller-Dirac.

This document does not transfer proof content into any Clay-program repository.

## Decision record

Heller-Dirac should host the Born-rule positive-norm / Dirac-current bridge.

Heller-Einstein should host the typed-interface routing note.

Yang-Mills should host the physical-Hilbert-space / gauge-invariant observable bridge.

Any future cross-repo theorem attempt must be explicit about what is preserved, what is projected away, and what claim grade is being asserted.
