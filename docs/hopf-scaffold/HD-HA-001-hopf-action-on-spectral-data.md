# HD-HA-001 — Hopf Action on Spectral Data

Identifier: `HD-HA-001`  
Distance tier: Framework-foundational  
Status: Active in Heller-Dirac v0.2  
Anti-seed: `A-HD-HA-001`  
Dependencies pinned: `988307215ad38ccb16514311222184a1b757752b`

## Definition surface

`HD-HA-001` names the general situation in which a Hopf algebra `K` acts on spectral data attached to a spectral triple `(A, H, D)`.

The minimal vocabulary is:

```text
Delta(k) = sum k_(1) tensor k_(2)
k · (ab) = sum (k_(1) · a)(k_(2) · b)
```

where `A` is a `K`-module algebra and the action on `H` implements the action on represented algebra elements.

## Relation to HD-FND-010

`HD-FND-010` records the foundational definition of a Hopf-algebra action on a spectral triple. `HD-HA-001` activates that content into the Hopf-scaffold namespace so downstream consumers can cite the Hopf-side action vocabulary directly.

## Use

This identifier is the entry point for group Hopf algebras as ordinary equivariance, Connes-Moscovici transverse-geometry carriers, Connes-Kreimer renormalization carriers, and quantum-group or bicrossed-product symmetry carriers.

## Provenance

Connes-Moscovici (1998), "Hopf algebras, cyclic cohomology and the transverse index theorem"; Connes-Kreimer (2000), "Renormalization in quantum field theory and the Riemann-Hilbert problem."

## Boundary

This identifier is apparatus. It does not prove analytic control, renormalizability, or existence of any field-theoretic object.
