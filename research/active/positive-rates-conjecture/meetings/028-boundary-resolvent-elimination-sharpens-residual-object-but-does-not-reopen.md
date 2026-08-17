# Group meeting 028: boundary-resolvent elimination sharpens the residual object but does not reopen the connected-renewal branch

Date: 2026-08-17

Professor review of:

- Meeting 027 and its explicit restart bar;
- Student G's late durability checkpoint `75d0e8a`, `students/student-g/010h-boundary-resolvent-elimination-checkpoint.md`;
- G010's exact filtered boundary-response identity and source equation;
- current `state.md` and `proof-spine.md`.

Operational correction: `75d0e8a` landed after Meeting 027 because the idle ruling had not yet been relayed to Student G. This is an orchestration overlap, not student disregard of the stop.

`state_narrowed: yes`.

## Ruling

The checkpoint is accepted as a useful exact algebraic sharpening, but it does **not** clear Meeting 027's restart bar. No G011 is issued. Student G remains idle; Student F remains idle. Consultation 002 / Meeting 025 `no-credible-route` remains the operative proof-architecture assessment.

The reason is precise. Meeting 027 required, for restart of this branch, either:

1. an explicit complementary observable/seminorm with a proved depth-uniform two-component contraction covering the blind frequency; or
2. a theorem specific to the actual connected orbit that bounds the required coefficient pairings summably or geometrically.

Commit `75d0e8a` proves neither. It removes the marginal-discrepancy functional algebraically and identifies a narrower explicit boundary-resolvent block, but supplies no summable/geometric estimate and no new iterable contraction.

## 1. Exact elimination accepted

Use the notation

$$
r=1+b,
\qquad
S_N=(rI-L_N)^{-1},
\qquad
D_N=(I-L_N)S_N,
$$

$$
R_N=(dI-gL_N)S_N,
$$

and let

$$
q_N=Q_Nf_N,
\qquad
f_1=Y_1,
\qquad
f_N=Y_NQ_{N-1}f_{N-1}.
$$

The previously accepted identities are

$$
c_{N+1}=\delta_N(R_Nq_N)
$$

and

$$
\delta_NL_N=-B A_ND_NP_N,
$$

where

$$
A_N(f)=\pi_{N+1}(f),
\qquad
\delta_N=A_N-\pi_N.
$$

Set

$$
u_N=S_Nq_N.
$$

Since

$$
(rI-L_N)u_N=q_N,
$$

one has

$$
\delta_N(q_N)
=r\delta_N(u_N)+B A_ND_NP_Nu_N.
$$

Also

$$
c_{N+1}
=d\delta_N(u_N)+gB A_ND_NP_Nu_N.
$$

Because `pi_N(q_N)=0`,

$$
\delta_N(q_N)=A_N(q_N).
$$

Eliminating `delta_N(u_N)` gives the exact all-depth identity

$$
\boxed{
 c_{N+1}
 =A_N\!\left[
 \frac dr q_N
 +\left(g-\frac dr\right)B
 D_NP_NS_Nq_N
 \right].
}
\tag{28.1}
$$

At `P_*`, with

$$
\frac dr=-\varepsilon,
\qquad
\varepsilon=\frac9{10000},
\qquad
g_0=g+\varepsilon,
$$

this is

$$
\boxed{
 c_{N+1}
 =A_N(\mathfrak B_Nq_N),
}
\tag{28.2}
$$

where

$$
\boxed{
\mathfrak B_N
=-\varepsilon I
+g_0B(I-L_N)(rI-L_N)^{-1}
P_N(rI-L_N)^{-1}.
}
\tag{28.3}
$$

I independently checked this elimination from the accepted source equation. No estimate of the unrestricted norm of `delta_N` is logically required once `(28.1)` is used.

## 2. Consequence for the old tail-shift comparison

Meeting 027 already ruled only that the filtered pairing was **not proved equivalent** to F013/F014's unrestricted tail-shift norm. The new identity strengthens that separation: the functional `delta_N` can be eliminated from the coefficient entirely.

Therefore a future claim that the connected-renewal route is merely the old bare tail-shift problem must account for `(28.1)`--`(28.3)`. Such an equivalence would require additional mathematics; it does not follow from the zero-frequency source equation alone.

This is worth retaining as exact negative bookkeeping about route equivalence.

## 3. Why this still does not reopen

The elementary estimate in the checkpoint gives only

$$
|c_{N+1}|
\le C_*\operatorname{osc}(q_N),
$$

with

$$
C_*
=\frac{342081}{1718750}
\approx0.19902894545.
$$

The checkpoint itself notes that this is far too crude after the renewal factor `z_sigma`. More importantly, no depth decay of `osc(q_N)` is proved.

The all-depth problem has therefore been sharpened to

$$
\boxed{
\text{control }A_N(\mathfrak B_Nq_N)
\text{ along }
q_N=Q_N(Y_Nq_{N-1}).
}
\tag{28.4}
$$

But `(28.4)` is still a target, not a mechanism. The already accepted high-pass contraction controls `R_Nq_N`, and the blind frequency prevents generic recovery of `q_N`; `(28.1)` does not supply the missing complementary observable or an orbit-specific decay theorem.

Assigning “prove decay of `(28.4)`” would therefore be exactly the generic new theorem search that Meeting 027 declined to authorize.

## Current state

- `(J-SPEC)` remains open.
- `(CT)` remains open.
- The fixed dual-renewal witness is not refuted.
- The exact sandwiched high-pass contraction from Meeting 027 remains valid.
- The exact residual coefficient can now be written without `delta_N` as `(28.2)`--`(28.3)`.
- The sharpest restart condition for this branch is now either an explicit complementary positive-frequency contraction, or a theorem giving summable/geometric decay of `A_N(\mathfrak B_Nq_N)` on the actual orbit.
- No G011; Student G idle.
- No F016; Student F idle.
- No proof architecture active.
