# Group meeting 001: two-site wall failure and length-three persistence

Date: 2026-08-15

Professor review of Graduate Student C assignment 001:

- `students/student-c/001-two-site-wall.md`, commit `0e95217`;
- `students/student-c/001-two-site-wall-verifier.py`, commit `b57135a`;
- `students/student-c/001-three-site-east-limit.py`, commit `4fab681`;
- independent Professor reconstruction `notes/professor-wall-test-verification.md`.

state_narrowed: yes

Evidence pointer: the Student C report and exact verifiers above, together with `notes/professor-wall-test-verification.md`. See the post-meeting source correction below and Meeting 002 for the final route decision.

## Post-meeting source correction

Assignment 002 checked the published theorem statements more carefully and found a material factual error in this meeting's original interpretation.

On `r11=0`, writing

$$
a=r_{00},\qquad b=r_{01},\qquad c=r_{10},
$$

published Głuchowski--Menz (2025), Corollary 7.2, covers `0<b<=a`. Therefore the assignment-001 path

$$
a=\varepsilon,\qquad
b=\frac\varepsilon2,\qquad
c=1-\varepsilon^2
$$

is **not** a genuine residual path; it is already in a proved ergodic region because `b<a`.

The original meeting language calling this path "strict residual" or "unresolved" was wrong and is superseded. The discrepancy arose because a prose summary in the 2026 paper reverses the `a,b` inequality relative to the published 2025 Corollary 7.2. The programme now follows the proved 2025 theorem statement and proof.

The finite-state calculations below remain mathematically correct as calculations. Their scientific role is downgraded: they are diagnostics on an already-covered parameter path and do not provide evidence about the true unresolved set.

The actual normalized unresolved set, reconstructed in assignment 002, is

$$
\mathcal R=
\left\{
0<a<b,
\quad \frac12\le c<1,
\quad c\ge a+b,
\quad b\ge\sqrt2(1-c)
\right\}.
$$

## Original mathematical verification, retained with corrected scope

On the assignment-001 path the canonical two-site killed chain has Perron root

$$
\rho_2(\varepsilon)
=
\frac{3-2\varepsilon-2\varepsilon^2+
\sqrt{(1-\varepsilon)^2+2\varepsilon^3}}4
\longrightarrow1,
$$

and starting from the fully agreed block `11`, the one-attack crossing factor is

$$
F_2(\varepsilon)
=
\frac{2(1-\varepsilon^2)(3+2\varepsilon-2\varepsilon^2-2\varepsilon^3)}
{6+7\varepsilon+6\varepsilon^2+4\varepsilon^3}
\longrightarrow1.
$$

At the East limit, a boundary disagreement against agreed `11` enters as orientation `10`; boundary updates preserve the disagreement and the next protected-site update crosses deterministically.

The independently reconstructed 24-state length-three chain on the same path gives conditional limits

$$
001:\frac{43}{75},\qquad
011:\frac45,\qquad
101:\frac{19}{30},\qquad
111:\frac9{10},
$$

for agreed words ending in one, while words ending in zero have vanishing attack probability. Both exterior orientations agree by direct reconstruction/copy-label symmetry. Thus

$$
R_3^{\rm adv}(\varepsilon)\to\frac9{10}
$$

on that path.

These values remain exact diagnostics, but after the source correction they are not target-relevant residual estimates.

## Standing novelty interpretation

Neither block-size calculation is a project result. The `9/10` value was never promoted; it only motivated assignment 002's full-regime characterization.

## Pre-committed stop rule retained

The meeting fixed the following rule before assignment 002:

- no move to block length four if a genuine residual sequence makes the three-site factor tend to one;
- even if a uniform three-site gap exists, abandon the finite-wall route if the frozen-exterior one-attack factor cannot be upgraded to rigorous dynamic block-renewal domination without introducing an uncontrolled stronger quantity.

Assignment 002 found a sharp uniform `5/6` gap on the **true** residual but also proved that a permanently present exterior disagreement crosses every fixed block almost surely under repeated attacks. Meeting 002 therefore applies the second stop condition and closes the finite-wall route.
