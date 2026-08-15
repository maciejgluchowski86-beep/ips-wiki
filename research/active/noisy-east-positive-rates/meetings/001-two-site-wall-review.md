# Group meeting 001: two-site wall failure and length-three persistence

Date: 2026-08-15

Professor review of Graduate Student C assignment 001:

- `students/student-c/001-two-site-wall.md`, commit `0e95217`;
- `students/student-c/001-two-site-wall-verifier.py`, commit `b57135a`;
- `students/student-c/001-three-site-east-limit.py`, commit `4fab681`;
- independent Professor reconstruction `notes/professor-wall-test-verification.md`.

state_narrowed: yes

Evidence pointer: the Student C report and exact verifiers above, together with `notes/professor-wall-test-verification.md`.

## Verification judgment

The two load-bearing calculations survive independent reconstruction.

On the strict residual path

$$
r_{11}=0,\qquad
r_{10}=1-\varepsilon^2,\qquad
r_{01}=\frac\varepsilon2,\qquad
r_{00}=\varepsilon,
$$

I independently rebuilt the canonical two-site killed chain. The full four-state transient kernel has Perron root

$$
\rho_2(\varepsilon)
=
\frac{3-2\varepsilon-2\varepsilon^2+
\sqrt{(1-\varepsilon)^2+2\varepsilon^3}}4
\longrightarrow1.
$$

Starting from the fully agreed block `11`, the one-attack crossing factor is

$$
F_2(\varepsilon)
=
\frac{2(1-\varepsilon^2)(3+2\varepsilon-2\varepsilon^2-2\varepsilon^3)}
{6+7\varepsilon+6\varepsilon^2+4\varepsilon^3}
\longrightarrow1.
$$

The limiting mechanism is genuinely deterministic. At the East rule `r10=1` and the other three transition probabilities zero, a boundary disagreement against an agreed `11` block enters as orientation `10`; right-site updates preserve that disagreement, while the next protected-site update compares environments `11` and `10` and crosses deterministically. Thus a two-site wall has no contraction margin stable along this unresolved approach to East.

I also independently rebuilt the full 24-state length-three killed chain, rather than relying on Student C's verifier. For exterior orientation `01`, conditional crossing limits after a successful boundary attack for the four agreed words ending in `1` are

$$
001:\frac{43}{75},\qquad
011:\frac45,\qquad
101:\frac{19}{30},\qquad
111:\frac9{10}.
$$

For the four agreed words ending in `0`, the boundary attack probability is `epsilon/2`, hence their unconditional factors tend to zero. Rebuilding the operator with exterior orientation `10` gives the same four nonzero limits; equivalently this follows from exact exchange symmetry of the two coupled copies. Therefore the adversary really ranges over all eight fully agreed three-site configurations and both exterior disagreement orientations, and

$$
\lim_{\varepsilon\downarrow0}R_3^{\rm adv}(\varepsilon)=\frac9{10}.
$$

The maximizer is the all-one block.

## What is learned

Length two is rejected as an East-stable wall mechanism.

The stronger inference that the same local cycle kills every fixed finite wall is also rejected: length three already has a qualitatively different limiting excursion and its one-attack factor stays below one on the path above.

The `9/10` value is **not a project result**. It is a diagnostic calculation at one block length and one asymptotic path. The standing novelty standard forbids turning this programme into `length 3, length 4, length 5, ...` with gradually improved regions.

The mathematical question that remains worth one further block is regime-wide and structural:

> Does the exact length-three adversarial crossing/regeneration factor retain a uniform gap below one over every genuine residual approach to the East boundary, and, if so, can such a local gap be converted by a block-renewal theorem into decay of disagreements in the infinite IPS?

The first half is a characterization of the mechanism over a full parameter regime rather than another larger-block instance. The second half is the theorem that would make the mechanism scientifically useful.

## Pre-committed stop rule for finite walls

This is fixed **before** the next calculation.

Let `R` be the exact normalized residual noisy-East parameter set after the reductions in the 2025/2026 papers, and let `partial_E R` be its East boundary. Student C must define both precisely from source before optimizing anything. Let

$$
R_3^{\rm adv}(r)
$$

denote the one-attack length-three factor maximized over every fully agreed three-site word and both exterior disagreement orientations.

The finite-wall route is abandoned in this programme if Student C proves or finds a genuine residual sequence `r_n -> partial_E R` with

$$
R_3^{\rm adv}(r_n)\to1.
$$

There will be **no move to length four** in response. This is an opportunity-cost ruling, not a theorem that every finite block fails: after one-site failure, two-site failure, and then a three-site loss of uniform margin on some residual path, rescuing the line by another block size would be exactly the block-by-block escalation excluded by the standing novelty standard unless a separate structural theorem predicted such a rescue.

Conversely, even if Student C proves a uniform bound

$$
R_3^{\rm adv}(r)\le1-\delta
$$

near the entire residual East boundary for some `delta>0`, that is still only a diagnostic local theorem. Continuation of the finite-wall route then requires a concrete block-renewal/concatenation statement whose hypotheses can actually be checked under the dynamically evolving exterior of the IPS. If the frozen-exterior one-attack factor cannot be upgraded to such a domination without introducing an uncontrolled stronger quantity, the finite-wall route is also abandoned rather than enlarged to a longer block.

## Direction decision

**continue for one bounded structural block.**

The negative two-site result by itself would have justified killing the proposed smallest-block mechanism. The independently checked `9/10` length-three limit supplies enough counterevidence to the proposed all-fixed-length obstruction to justify one further, sharply bounded characterization. It does not justify a sequence of larger-block computations.

The next assignment is `students/student-c/assignment-002.md`.

Graduate Student C remains the active persistent student. Graduate Students A and B remain idle.

No project claim is registered from assignment 001.