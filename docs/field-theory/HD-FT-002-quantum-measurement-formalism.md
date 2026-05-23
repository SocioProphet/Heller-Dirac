# HD-FT-002 — Quantum Measurement Formalism Surface

Status: field-theory methodology / reference surface.  
Owner: `SocioProphet/Heller-Dirac`.  
Identifier: `HD-FT-002`.  
Claim level: formalism vocabulary only; no theorem promotion.

## Purpose

This note captures the quantum-measurement formalism left outside `HD-FT-001`.

`HD-FT-001` records the positive-norm / Dirac-current bridge. `HD-FT-002` records the measurement language that sits on top of a positive Hilbert or algebraic state space: density operators, projectors, POVMs, state updates, interference, decoherence, and path-integral amplitude squaring.

This document does not prove or derive the Born rule. It preserves the measurement formalism as reference vocabulary for downstream Heller-Dirac, Heller-Einstein, and Yang-Mills interfaces.

## Core Born-rule forms

For a pure state and an orthonormal eigenbasis, the elementary Born rule is:

```text
P(a_i) = |<a_i | psi>|^2.
```

For a mixed state represented by density operator `rho`, a projective measurement with projector `Pi_i` gives:

```text
P(a_i) = Tr(Pi_i rho).
```

For a general positive operator-valued measure, or POVM, with effects `E_m >= 0` and:

```text
sum_m E_m = I,
```

the probability rule is:

```text
P(m) = Tr(E_m rho).
```

This is the measurement-facing state/effect pairing that Heller-Dirac may cite when field-theory apparatus needs explicit probability vocabulary.

## State-update boundary

The probability assignment and the state-update rule are related but distinct.

For an ideal projective measurement with outcome `i`, the standard selective update is:

```text
rho -> Pi_i rho Pi_i / Tr(Pi_i rho).
```

For more general measurements, an instrument or Kraus decomposition is needed:

```text
rho -> M_m rho M_m^dagger / Tr(M_m^dagger M_m rho),
E_m = M_m^dagger M_m.
```

The effect `E_m` determines the outcome probability. The instrument determines the post-measurement state. They must not be silently conflated.

## Gleason and uniqueness vocabulary

Gleason-style reasoning belongs here only as reference vocabulary.

The relevant use is:

```text
noncontextual probability assignments over closed subspaces of a Hilbert space are represented by density operators under the theorem's hypotheses.
```

This is a mathematical constraint on probability measures over Hilbert-space projection lattices. It is not, by itself, a physical derivation of quantum mechanics, detector physics, or a downstream Clay-program result.

Dimension and hypothesis discipline matters. Any future use of Gleason-style language must state the Hilbert-space dimension and the noncontextuality or effect-algebra assumptions being used.

## Interference and decoherence vocabulary

For a superposed amplitude:

```text
psi = alpha phi_1 + beta phi_2,
```

the probability density contains cross terms:

```text
|psi|^2 = |alpha phi_1|^2 + |beta phi_2|^2
          + 2 Re(alpha beta^* phi_1 phi_2^*).
```

The cross term is the interference contribution. Decoherence suppresses observable interference when the system becomes entangled with environment or apparatus degrees of freedom and the reduced state loses accessible off-diagonal coherence in the measurement basis.

This is formal vocabulary. It does not solve the measurement problem and does not derive collapse.

## Path-integral vocabulary

The path-integral form reinforces the same boundary:

```text
K(x_f, x_i) = integral D[x(t)] exp(i S[x] / hbar).
```

Probabilities are obtained only after summing amplitudes and applying the state/effect probability rule. The discipline is:

```text
sum complex amplitudes before taking probabilities.
```

This is useful for distinguishing quantum interference from classical mixture. It is not a derivation of the Born rule.

## Relationship to Heller-Einstein

Heller-Einstein owns typed-interface and projection-induced stochasticity vocabulary.

A Heller-Einstein Markov kernel has the form:

```text
K(y, y') = mu_y({x in F_y : tau(f(x)) = y'}).
```

A Born probability has the Hilbert-space form:

```text
P(m) = Tr(E_m rho).
```

Both are probability assignments, but they are not identified by default. A future bridge must prove equivalence under explicit typed-interface and Hilbert-space hypotheses before claiming that a projection-induced trace kernel reproduces Born probabilities.

## Relationship to Yang-Mills

Yang-Mills owns the gauge-invariant physical-Hilbert-space and observable-algebra boundary.

Heller-Dirac may supply measurement vocabulary, but Yang-Mills must decide which gauge-invariant states and effects are physical probability-bearing objects. Gauge-fixed variables, ghosts, and raw gauge potentials are representation apparatus unless physical-state reconstruction and positivity are supplied.

## Non-claims

This document does not prove the Born rule.

This document does not derive quantum mechanics.

This document does not solve the measurement problem.

This document does not derive noncommuting observables or entanglement structure.

This document does not claim Gleason's theorem alone derives physical measurement.

This document does not identify Heller-Einstein Markov kernels with Born probabilities.

This document does not import Yang-Mills theorem-track content into Heller-Dirac.

This document does not transfer proof content into any Clay-program repository.

## Decision record

Heller-Dirac owns this measurement-formalism surface because it is the field-theory and positive-state-space repository.

Heller-Einstein owns typed-interface probability kernels.

Yang-Mills owns physical gauge-invariant observable and Hilbert-space discipline.

Cross-repo use must preserve the distinction between probability formalism, interface-induced stochasticity, and gauge-theory physical-state construction.
