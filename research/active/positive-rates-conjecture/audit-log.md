# Audit log

## Principal reset: fixed positive-rates target

Date: 2026-08-16

The principal fixed the scientific target to the positive rates conjecture for simple IPS and instructed the Professor to prevent circular progress through equivalent reformulations.

Initial durable files:

- `principal-starting-note.md` — verbatim principal note;
- `state.md` — fixed-target and anti-circularity rules;
- `proof-spine.md` — current source reductions, closed finite-wall route, and last-successful-interaction reconstruction edge;
- `literature.md` — primary sources and inherited project work;
- `meetings/000-principal-reset.md` — setup meeting;
- `students/student-f/assignment-001.md`;
- `students/student-g/assignment-001.md`.

No mathematical claim was registered at setup. Equivalent reformulations are explicitly not counted as target narrowing.

## Inherited verified/checked negative knowledge

From branch `research/noisy-east-positive-rates`:

- source-corrected residual chamber on `r11=0`;
- failure of the one-site long-lived-state criterion in that chamber;
- sharp `5/6` East-boundary limit for the three-site frozen-exterior one-attack diagnostic;
- almost-sure eventual crossing of every fixed finite agreed block under a permanently frozen exterior disagreement;
- closure of the fixed-finite-wall route, including a no-length-four rule.

These are inputs and route exclusions, not new claims of the present programme.

## Meeting 001: first student returns

Meeting:

`meetings/001-density-estimates-and-regional-kernel.md`

`state_narrowed: yes`.

Student F:

- commit `db49c30`;
- `students/student-f/001-last-interaction-reduction.md`.

Student G:

- commit `1f41488`;
- `students/student-g/001-independent-structural-attack.md`.

Professor-checked outputs from F:

- corrected local monomial-generator algebra in the surviving barrier--scaffold note;
- exact hidden successful-type average `B eta_i-c`, with `B=b+c-a`, `rho=c/B`;
- exact comparison generators and Duhamel normalization;
- uniform right-conditioned `L^-` lower bound
  $$
  P^-(eta_i(t)=1\mid F^+_{i,t})\ge (1-e^{-(1-c)t})/(1+b-a);
  $$
- explicit burn-in `T_rho` giving nonnegative insertion against nonnegative right-history-measurable companions;
- raw Duhamel left-dependence obstruction;
- patchwise negativity on `a>b(1-c)` for sufficiently long OI patches.

Professor-checked outputs from G:

- exact original-dynamics transport--dissipation identity for the one-density;
- boundary-uniform interval zero-density lower bound;
- Poisson-tail one-sided finite propagation and the resulting high-probability finite-box estimate;
- adjacent-`11` suppression inequality and mesoscopic hard-core regime near `b=0`.

Meeting 001 also checked that the present density estimates do **not** directly compose. F needs a conditional/weighted insertion statement for `L^-`; G gives unweighted density information for `L`. Numerically,

$$
\frac1{1+b+c}<\frac c{b+c-a}
$$

throughout the residual chamber, and the hard-core half-zero guarantee is also below `rho`.

Current bottleneck: the minimal regional companion kernel at a hidden successful interaction must be proved or disproved to satisfy the `rho`-insertion inequality. One-cell success must be followed immediately by a two-cell composition test.

Next assignments:

- `students/student-f/assignment-002.md`;
- `students/student-g/assignment-002.md`.
