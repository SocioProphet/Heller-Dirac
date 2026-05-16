# HD-FND-007 — Tomita-Takesaki Modular Operator and Modular Flow

Identifier: `HD-FND-007`  
Distance tier: Framework-foundational  
Status: Active after this PR  
Anti-seed: `A-HD-FND-001`, `A-HD-TM-001`

## Statement surface

Let `M` be a von Neumann algebra acting on a Hilbert space `H`, with a cyclic and separating vector `Omega`.

Define the antilinear operator `S` on `M Omega` by:

```text
S(a Omega) = a* Omega
```

The closure of `S` has polar decomposition:

```text
S = J Delta^(1/2)
```

where `J` is the modular conjugation and `Delta` is the modular operator.

Tomita-Takesaki theory gives:

```text
Delta^(it) M Delta^(-it) = M
J M J = M'
```

The modular flow is:

```text
sigma_t(a) = Delta^(it) a Delta^(-it)
```

## Reading

The modular flow is a canonical state-dependent one-parameter automorphism group. It is the foundation for Heller-Dirac time-theory content.

## Provenance

Tomita (1967); Takesaki (1970), *Tomita's theory of modular Hilbert algebras and its applications*. Modern reference: Takesaki, *Theory of Operator Algebras II*.

## Boundary

Per `A-HD-TM-001`, modular flow is not automatically physical time. Per `A-HD-FND-001`, citation is not reproof.
