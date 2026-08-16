# Audit log

## Principal reset: fixed positive-rates target

Date: 2026-08-16

The principal fixed the scientific target to the positive rates conjecture for simple IPS and instructed the Professor to prevent circular progress through equivalent reformulations.

## Inherited negative knowledge

From branch `research/noisy-east-positive-rates`:

- source-corrected residual chamber on `r11=0`;
- failure of the one-site long-lived-state criterion there;
- sharp `5/6` three-site frozen-exterior one-attack diagnostic;
- almost-sure eventual crossing of every fixed finite agreed block under a permanently frozen exterior disagreement;
- closure of the fixed-finite-wall route.

## Meeting 001: exact density/sign information

Meeting: `meetings/001-density-estimates-and-regional-kernel.md`.

`state_narrowed: yes`.

Student F, commit `db49c30`, reconstructed the hidden-type algebra and proved the right-conditioned `L^-` insertion estimate after explicit burn-in. Student G, commit `1f41488`, proved direct transient zero-density, finite-box concentration, and adjacent-`11` suppression estimates for the original dynamics.

Meeting 001 checked that the two density estimates do not compose naively and set the finite regional insertion/composition test as the next bottleneck.

## Meeting 002: one-cell insertion works, two-cell composition fails

Meeting: `meetings/002-cellwise-insertion-composition-fails.md`.

`state_narrowed: yes`.

Student F:

- commit `d2c6e92`;
- `students/student-f/002-regional-insertion.md`;
- verifier commit `cfbcaf5`.

Professor-checked conclusion: one-cell regional integration is positive, but the hidden predecessor transfer is negative on sufficiently short cells at every residual parameter point. The cellwise last-exit/scaffold positivity route is closed.

## Meeting 003: true rightmost-source contraction

Meeting: `meetings/003-live-source-contraction.md`.

`state_narrowed: yes`.

Student F:

- commit `d0a508c`;
- `students/student-f/003-live-disagreement-episode.md`;
- verifier commit `f379cd3`.

Professor-checked conclusions: a rightmost live disagreement has an explicit positive childless regeneration probability; there is a finite-slab regeneration event; the coupling drift isolates the weighted high-risk state `J_i`; and residual-uniform first-generation contraction from zero-rich/no-`11` snapshots fails at the East boundary.

## Meeting 004: two-generation regeneration and all-depth obstruction

Meeting: `meetings/004-two-generation-regeneration-and-depth-obstruction.md`.

`state_narrowed: yes`.

Student F:

- commit `893700c`;
- `students/student-f/004-two-generation-episode.md`;
- verifier commit `5e3c4bc`.

Professor-checked conclusions:

1. every disagreement site has predictable coalescence intensity at least
   $$
   q=1-c+a>0;
   $$
2. after a first child is born, the full parent-child episode clears before grandchild creation with conditional probability at least
   $$
   \left(\frac{1-c+a}{2-c+a}\right)^2;
   $$
3. finite-depth ordered clearing is valid with exponent equal to active-span depth;
4. the resulting depth-dependent gaps are summable and do not give arbitrary-depth extinction.

Ruling: stop finite-depth escalation and seek an all-depth structural contraction.

## Meeting 005: principal centered predecessor-trail reduction

Meeting: `meetings/005-principal-trail-reduction-and-all-depth-transfer.md`.

`state_narrowed: yes`.

Durable principal exploration note:

`notes/principal-centered-trail-reduction.md`.

Professor-checked / accepted working conclusions:

1. In the residual centered dual,
   $$
   B=b+c-a,
   \quad p_*=c/B,
   \quad q_*=(b-a)/B,
   \quad \omega=1-c+a,
   $$
   with selected predecessor-trail interactions all births (`beta=B`, `lambda=0`).
2. The canonical predecessor trail has depth `n=r-x+1`; after conditioning on its decorated geometry the left/trail/right Poisson families factor, and the trail contributes the positive scalar
   $$
   e^{-\omega\tau}.
   $$
   The complete Poisson-Mecke identity is accepted as a working lemma and is assigned for independent reconstruction before use in a closing proof.
3. Averaging the final refresh coin before absolute values makes the right-region operator uniformly sup-norm bounded independently of interval length and trail depth.
4. For fixed interval, zero-boundary finite-volume relaxation plus the positive-rate factor `omega>0` reduces the nonempty-trail term to the invariant all-depth condition
   $$
   B(b-a)^{n-1}\int e^{-\omega|u|}|\pi^0_{m,r}(F_{x,u})|\,du\to0.
   $$
5. At exact East, the final trail birth inserts a centered character independent of the preceding factor under the Bernoulli zero-boundary invariant law, so the invariant trail expectation is exactly zero.
6. A sufficient all-depth theorem is a centered signed-measure transfer norm with contraction constant `theta<1` for
   $$
   (b-a)\int_0^\infty e^{-\omega u}\mathcal C_{y,u}\,du.
   $$
   Total variation on all signed measures is excluded because it loses the centering cancellation.
7. Along `a=eps^2,b=eps,c=1-eps^2`, the one-site constant-mode factor is
   $$
   (1-eps)/(2(1+eps))<1/2.
   $$
8. The principal chat reports a two-level scalar sign change as inter-trail time varies, but that latest claim did not come with its exact calculation and is not yet independently verified.

Ruling: pause, but do not close, the all-depth live-disagreement route. The centered predecessor-trail reduction is narrower because the right region and post-exit relaxation are already controlled, leaving one explicit all-depth invariant-transfer target. The common scale

$$
q=\omega=1-c+a
$$

is noted but not treated as an automatic bridge.

Student F Assignment 005 is superseded by

`students/student-f/assignment-006.md` — independently audit the trail reduction, verify the no-exit complement and reported two-level sign change, then prove or kill the all-depth centered-transfer criterion.

Student G remains on Assignment 002 and will be folded in when it returns.
