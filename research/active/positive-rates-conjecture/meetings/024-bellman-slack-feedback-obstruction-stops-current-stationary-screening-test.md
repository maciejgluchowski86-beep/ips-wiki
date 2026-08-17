# Group meeting 024: Bellman-slack feedback obstruction stops the current stationary-screening test

Date: 2026-08-17

Professor review of:

- Meeting 023 and its one-block feasibility/stopping rule;
- Student F commits `1bab5ea`, `students/student-f/015-stationary-boundary-control-screening.md`, and `6776ea9`, the exact verifier;
- the principal stationary-boundary-control note and current `state.md` / `proof-spine.md`;
- Student G checkpoint `2cb0696` and verifier `2a2f66b` only to confirm that G009 remains in flight and logically independent.

`state_narrowed: yes`.

Evidence pointer: F015 equations `(0.1)`--`(0.7)`, especially the exact scale-extension identity, weighted tracking representation, controller-uniform unweighted mismatch theorem, and maximum-principle obstruction to additive block correctors. The finite rational calibration is checked by the committed verifier.

## Ruling in one sentence

F015 materially sharpens the stationary occupation-control architecture but does **not** produce the repeatable multiscale theorem required by Meeting 023. The current Bellman-corrector concatenation implementation therefore stops here: no F016 and no larger-`N` LP continuation is issued. The exact hierarchy remains valid reusable mathematics, and a future stationary-screening theorem is not refuted, but it would require a genuinely new mechanism controlling adaptive **weighted** boundary mismatch by a joint cross-block corrector. Student F becomes idle; G009 remains the sole active block.

## 1. Exact scale-extension identity accepted

Let `F_N^+` and `F_N^-` be optimal upper/lower Bellman correctors and define their nonnegative slacks

$$
s_N^+(x,u)=U_N(h)-h(x)+L_N^uF_N^+(x),
$$

$$
s_N^-(x,u)=h(x)-L_N^uF_N^-(x)-\ell_N(h).
$$

For `M>N`, feed the physical interface spin `X_N` into the old boundary-action slot. Writing an arbitrary `M`-site corrector as the old corrector plus an unrestricted remainder and applying the finite LP dual gives exactly

$$
\boxed{
U_N(h)-U_M(h)
=\inf_{m\in\mathcal K_M}m(s_N^+),
}
$$

$$
\boxed{
\ell_M(h)-\ell_N(h)
=\inf_{m\in\mathcal K_M}m(s_N^-),
}
$$

and hence

$$
\boxed{
D_M(h)=D_N(h)
-\inf_{m\in\mathcal K_M}m(s_N^+)
-\inf_{m\in\mathcal K_M}m(s_N^-).
}
\tag{24.1}
$$

I accept this identity. It converts the proposed dyadic contraction into an exact occupation problem: scale improvement is precisely unavoidable stationary occupation of the old Bellman slacks after the controller is moved farther right.

## 2. Bellman slack is weighted adaptive tracking error

Complementary slackness and irreducibility allow an optimal corrector to be chosen so that for every old block state at least one boundary action is tight. Let `pi_F(x)` be one such action. Since the two boundary actions differ only through the rightmost-site flip rate,

$$
\boxed{
s_F(x,u)
=w_F(x)\,1_{\{u\ne\pi_F(x)\}},
}
\tag{24.2}
$$

where

$$
w_F(x)
=d(x_{N-1})|F(x^{N-1})-F(x)|,
\qquad d(0)=b-a,\quad d(1)=c.
$$

Thus the required scale gain is not merely failure of the next physical spin to track an optimal feedback action. It is that mismatch weighted by the `N`-dependent Bellman boundary gradient.

This is the load-bearing distinction in F015.

## 3. Controller-uniform unweighted mismatch is real but insufficient

Put

$$
r_*:=\min\{a,1-c\}>0.
$$

For every Boolean target `pi` of the old `N` spins and every stationary controlled extension with physical interface spin `V=X_N`, F proves

$$
\boxed{
P(V\ne\pi(X_0,\ldots,X_{N-1}))
\ge \frac{r_*}{N+1+r_*}.
}
\tag{24.3}
$$

The proof is a direct stationary drift estimate for the mismatch indicator: while matched, an unconditional interface reset creates mismatch at rate at least `r_*`; while mismatched, repair can occur only by one of the `N+1` physical-site flips, each of rate at most one.

I accept this theorem. It does not imply a fixed-fraction contraction because `(24.1)` requires expectation of `w_F` on mismatch states. No proved statement prevents an optimizing controller from concentrating its unavoidable mismatch on states where `w_F` is small.

The precise missing estimate is therefore of the form

$$
\inf_{m\in K_{2N}}m(s_N^+)
+
\inf_{m\in K_{2N}}m(s_N^-)
\ge \rho D_N(h)-Ce^{-\gamma N}.
\tag{24.4}
$$

This is essentially the desired multiscale theorem expressed in its exact Bellman variable. F015 supplies no independent mechanism for `(24.4)`.

## 4. Independently constructed block correctors do not concatenate

F also proves a structural obstruction stronger than a failed numerical search.

For an optimal upper or lower `N`-block corrector, both boundary actions occur as tight actions somewhere. Now append an arbitrary right block and consider any additive corrector

$$
H(x,z)=F_N(x)+G(z),
$$

where `G` is completely arbitrary on the appended block. At a maximum of `G`, the appended-block generator contributes at most zero. Choosing an old state where the physical interface action at that maximum is tight gives

$$
\boxed{
\max_{x,z,u}
\{h(x)-L_{N+r}^u(F_N+G)(x,z)\}
\ge U_N(h).
}
\tag{24.5}
$$

At a minimum of `G`, the lower analogue gives

$$
\boxed{
\min_{x,z,u}
\{h(x)-L_{N+r}^u(F_N^-+G)(x,z)\}
\le \ell_N(h).
}
\tag{24.6}
$$

Therefore an old corrector plus any independently constructed appended-block corrector gives **zero strict endpoint improvement**. Any successful scale contraction must use genuinely joint dependence across the old/new interface.

F proves a conditional fixed-width extension of this maximum-principle obstruction and verifies its hypothesis exactly at `N=2` for the one-spin interface at `(a,b,c)=(1/10,3/10,4/5)`. This does not rule out arbitrary-width joint correctors at all scales, but it rules out the natural concatenation mechanism Meeting 023 was testing.

## 5. Adaptive feedback is not covered by the cited hard-East relaxation

At one controlled spin,

$$
U_1(x_0)=\frac{b}{b+1-c},
\qquad
\ell_1(x_0)=\frac{a}{a+1},
$$

whereas fixed boundary values give stationary densities

$$
p_0=\frac{a}{a+1-c},
\qquad
p_1=\frac{b}{1+b}.
$$

At `(1/10,3/10,4/5)`,

$$
U_1=\frac35,
\quad \ell_1=\frac1{11},
\quad p_0=\frac13,
\quad p_1=\frac3{13}.
$$

Thus state-dependent stationary feedback can bias the local law far outside the range produced by either fixed boundary. This confirms the concern recorded in Meeting 023: hard-East relaxation with a fixed or exogenous ergodic boundary does not control the adaptive weighted feedback in `(24.2)`.

A future use of East relaxation would need a new robustness theorem specifically controlling that feedback; the cited results themselves do not provide it.

## 6. Verifier scope

The verifier uses exact rational arithmetic at `(1/10,3/10,4/5)` and checks:

- the `N=1` Bellman endpoints and slacks;
- fixed-boundary densities versus adaptive-feedback extrema;
- exact enumeration of deterministic `N=2` controllers, giving
  $$
  U_2=\frac38,
  \qquad \ell_2=\frac{31}{137};
  $$
- the exact slack-occupation identities
  $$
  U_1-U_2=\frac9{40},
  \qquad
  \ell_2-\ell_1=\frac{204}{1507};
  $$
- exact `N=2` Bellman inequalities;
- both boundary actions tight in every one-spin interface cylinder;
- the `N=1` instance of the mismatch lower bound.

These checks support the finite algebra. They do not prove a multiscale contraction, and F does not claim one.

## 7. Stop-rule application

Meeting 023 authorized exactly one feasibility block. A positive continuation required a repeatable theorem, not further shrinking LP widths. F015 returns:

1. a precise exact formula for what repeatability would require;
2. a uniform unweighted tracking theorem which falls short of that requirement;
3. a maximum-principle theorem refuting additive block concatenation;
4. confirmation that the proposed hard-East input does not control the remaining adaptive weighted feedback;
5. no recursion forcing `D_N(h)->0`.

This is more informative than the merely numerical stopping case, and it narrows the architecture substantially. It nevertheless does **not** justify a second optimization block on larger `N`, a wider interface ansatz, or a generic search for joint correctors. Such work would amount to searching directly for the missing theorem `(24.4)` without a new mechanism.

Accordingly the **current stationary boundary-control corrector-concatenation route stops**.

This does not refute the exact hierarchy `K_N`, monotone decay of `D_N`, the possibility that `D_N(h)->0`, or every conceivable stationary screening theorem. Those remain open.

## 8. Relation to G009 and current programme state

G's checkpoint `2cb0696` correctly fixes the exact predecessor-trail normalization and reverse-transfer recursion, including

$$
J_n=\frac Bg R_n=\frac gB N_n,
$$

so the depth-independent normalizations have the same exponential growth rate. It explicitly does not decide `(J-SPEC)`.

G009 remains in flight and is now the **sole active internal block**. The durability rule remains: commit nontrivial intermediate asymptotic reductions/certificates promptly.

Student F is idle. No F016 is issued.

If G009 also returns without a genuine asymptotic theorem, the programme returns to the Meeting-022 / consultation-002 state: no presently identified proof architecture clears the continuation bar, unless genuinely new external or principal input has arrived in the meantime.

## Ruling

- `state_narrowed: yes`.
- Exact Bellman scale-extension identities `(24.1)` are accepted.
- Bellman slacks are weighted adaptive boundary-action mismatches `(24.2)`.
- The controller-uniform unweighted mismatch bound `(24.3)` is accepted but insufficient for scale contraction.
- Additive independently constructed block correctors cannot strictly improve the Bellman endpoints.
- The cited hard-East relaxation does not control the remaining adaptive weighted feedback.
- No repeatable theorem proving `D_N(h)->0` was obtained.
- The current stationary boundary-control corrector-concatenation route stops; no larger-`N` continuation and no F016.
- Student F idle; G009 sole active block.
