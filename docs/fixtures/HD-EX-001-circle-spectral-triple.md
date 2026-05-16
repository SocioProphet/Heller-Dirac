# HD-EX-001 — Circle Spectral Triple

Identifier: `HD-EX-001`  
Distance tier: Framework-foundational fixture  
Status: Active after this PR  
Anti-seed: `A-HD-EX-001`

## Construction

The circle spectral triple is:

```text
A = C^infty(S^1)
H = L^2(S^1)
D = -i d/dtheta
```

where `A` acts on `H` by pointwise multiplication.

## Verification of HD-FND-001 axioms

`D` is essentially self-adjoint on smooth periodic functions. The functions `e_n(theta) = exp(i n theta)` form an orthonormal basis and satisfy:

```text
D e_n = n e_n
```

so the spectrum is `Z`. Since `|n| -> infinity`, the resolvent is compact.

For `a in C^infty(S^1)`:

```text
[D, pi(a)] f = -i a' f
```

so the commutator is multiplication by the smooth bounded function `-i a'`.

## KO-dimension

The circle is odd-dimensional. With `J` given by complex conjugation, the signs are:

```text
epsilon = +1
epsilon-prime = -1
epsilon-double-prime = n/a
```

so this fixture has KO-dimension 1, matching `HD-FND-003`.

## Distance formula

For point-evaluation states at `theta_1` and `theta_2`, `HD-FND-005` gives:

```text
d_D(theta_1, theta_2) = sup {|a(theta_1) - a(theta_2)| : ||a'||_infty <= 1}
```

This reproduces the round geodesic metric on the circle:

```text
d_D(theta_1, theta_2) = min(|theta_1 - theta_2|, 2pi - |theta_1 - theta_2|)
```

## Spectral action

Since the spectrum of `D` is `Z`:

```text
Tr f(D / Lambda) = sum_{n in Z} f(n / Lambda)
```

For rapidly decaying cutoff `f`, Poisson summation gives a leading term proportional to `Lambda * integral f`, with normalization recovering the circle perimeter scale.

## Role

`HD-EX-001` is the first canonical Heller-Dirac fixture. It validates the core apparatus:

- HD-FND-001: spectral triple axioms;
- HD-FND-003: KO-dimension sign data;
- HD-FND-005: metric recovery;
- HD-FND-006: spectral action sanity check.

## Boundary

Correct computation on this fixture is apparatus validation only. It is not Clay progress and does not imply anything about Yang-Mills, BSD, RH, Hodge, P vs NP, or Navier-Stokes.

## Reservation note

`HD-EX-002` is reserved for a future free-Dirac fixture. `HD-EX-003` is reserved for a Hopf-equivariant spectral triple fixture.
