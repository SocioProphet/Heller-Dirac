# A1 Gate Minimality - v3 Amendments

Status: v3 amendment set
Scope: mechanical refinements to the A1 gate-minimality note
Substantive theorem content: unchanged for T1 and T2

## Purpose

This note records the v3 amendments required after review of the A1 gate-minimality proof note.

The amendments are mechanical. They do not change the theorem target. They repair citation precision, move the terminal-object point from an open subclaim to a corollary, and tighten the Spin-c extension note.

## Amendment 1: Step 1 citation

Section 3, Step 1 should replace the original sentence:

> Since G is compact and rho_spatial is continuous and injective, rho_spatial is a closed embedding...

with:

> By Cartan's theorem on closed subgroups, or equivalently by the fact that a continuous injective map from a compact space to a Hausdorff space is a homeomorphism onto its image, the continuous faithful homomorphism rho_spatial: G -> SU(2) is a closed embedding. Hence G is identified with a closed connected Lie subgroup of SU(2).

## Amendment 2: C-1 from open subclaim to corollary

Move C-1 from the open-subclaims section into Section 3, immediately after Step 5.

Replacement corollary:

> Corollary: terminal-object structure of A.
>
> A morphism (G, rho) -> (G_prime, rho_prime) in A intertwines the spatial representations: rho_prime_spatial composed with phi equals rho_spatial.
>
> When source and target are both (SU(2), rho_def), with rho_spatial and rho_prime_spatial both equal to id_SU(2), this forces phi = id_SU(2). Hence A is a one-object category up to canonical isomorphism with trivial automorphism group. The object (SU(2), rho_def) is terminal, equivalently initial, equivalently the unique object up to canonical isomorphism.

Remove C-1 from the open-subclaims section.

## Amendment 3: Spin-c note tightened

Replace the C-4 entry with:

> C-4: Spin-c extension.
>
> The complexified extension replaces Spin(3) with Spin-c(3), isomorphic to U(2), where U(2) is the quotient of SU(2) x U(1) by the diagonal Z/2. The central order-2 element zeta = -I of T2 generalizes to a U(1)-family of central elements, namely the U(1) factor, parameterized by the Spin-c connection.
>
> The target group for the minimal-G theorem under condition (ii) replaced by faithful into Spin-c(3) is U(2), and the conjectured minimal candidate is U(2) with the defining representation tensored by an appropriate character.
>
> The proof requires extending condition (iv) to a central one-parameter U(1) subgroup containing the Z/2, and reformulating condition (v) to track the Spin-c connection curvature against the symplectic Q_A.
>
> Statement and proof remain open.

## Non-claims

This amendment set does not prove the Spin-c extension.

This amendment set does not alter the A1 theorem statement except for proof hygiene and placement of the terminal-object corollary.

This amendment set does not establish A2 or An minimality.
