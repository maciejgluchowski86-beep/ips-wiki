# Group meeting 026: exact dual renewal isolates a connected positive-frequency tail; one bounded `(J-SPEC)` block reopens

Date: 2026-08-17

Professor review of:

- Meeting 025 and its explicit restart condition;
- Student G's late checkpoint `394b7e3`, `students/student-g/009b-dual-renewal-checkpoint.md`;
- G009's canonical normalization checkpoint and final fixed-depth renewal report;
- F009 only for the growing-mode obstruction, and F013--F014 only to distinguish the old zero-frequency tail from the new connected operator;
- current `state.md` and `proof-spine.md`.

Operational correction: commit `394b7e3` landed after Meeting 025 because the Meeting-025 idle ruling had not yet been relayed to Student G. This is an orchestration overlap, not a student violation. The checkpoint is therefore evaluated as genuinely new post-stop input under Meeting 025's restart condition.

`state_narrowed: yes`.

Evidence pointer: G009b equations `(1)`--`(12)` for the exact `L^1` witness and renewal decomposition, `(13)`--`(22)` for the fixed rational filter, and `(23)`--`(25)` for the connected-tail criterion. No verifier accompanied `394b7e3`; the Professor independently reconstructed the displayed finite coefficients numerically from the exact finite generators and checked the exact value of `z_sigma`. Exact rational verification is required as the first durable step of the continuation.

## Ruling in one sentence

The late checkpoint **does clear Meeting 025's resumption bar for exactly one bounded block**. The reason is not the additional finite coefficients. It is the exact all-depth separator/connected decomposition: invariant projections are extracted *exactly* as renewal separators, while the remaining connected operator `Q_N^sigma J_N` has the exact invariant projection removed. The resulting sufficient target is the quantitative tail inequality `(26.8)` below. This is materially different from approximating a long segment by equilibrium and then controlling the F013/F014 tail-shift error. Student G is reactivated on one connected-tail block; Student F remains idle.

This does not reopen the exhausted predecessor-profile implementation generally, and it does not yet prove `(J-SPEC)`.

## 1. Exact fixed-filter `L^1` witness

Let `R_n` be G's exact raw reverse-transfer norm, so

$$
J_n=\frac Bg R_n
$$

up to the already fixed depth-independent normalization.

For any fixed measurable `sigma:[0,infty)->[-1,1]`, G defines

$$
W_n^\sigma
=Z\int
\left(\prod_{j=2}^n w(u_j)\sigma(u_j)\right)
S_n(0,u_2,\ldots,u_n)\,du_2\cdots du_n.
$$

Pointwise `|sigma|<=1` gives

$$
\boxed{R_n\ge |W_n^\sigma|.}
\tag{26.1}
$$

Hence one fixed filter with

$$
\limsup_n|W_n^\sigma|^{1/n}>1
$$

is a legitimate fixed-rate proof that `rho_J>1`. This is already different from the singular `epsilon->0` / fixed-depth mechanism of Meeting 025.

## 2. Exact separator/connected decomposition

Define

$$
H_N^\sigma=\int_0^\infty w(u)\sigma(u)P_u^N\,du,
\qquad
z_\sigma=\int_0^\infty w(u)\sigma(u)\,du,
$$

and

$$
\boxed{Q_N^\sigma=H_N^\sigma-z_\sigma\Pi_N.}
\tag{26.2}
$$

Then exactly

$$
Q_N^\sigma\mathbf 1=0,
\qquad
\pi_NQ_N^\sigma=0.
\tag{26.3}
$$

Let `J_N` denote the centered insertion/drop map and put

$$
c_1=m_0,
$$

$$
\boxed{
 c_k^\sigma
=
\pi_kJ_kQ_{k-1}^\sigma J_{k-1}\cdots Q_1^\sigma J_1,
\qquad k\ge2.
}
\tag{26.4}
$$

Expanding every `H_j^sigma=z_sigma Pi_j+Q_j^sigma`, each invariant projection is an **exact separator**. Suffix projectivity then gives the ordered-composition formula

$$
r_n^\sigma
=
\sum_{\ell_1+\cdots+\ell_s=n}
 z_\sigma^{s-1}\prod_i c_{\ell_i}^\sigma.
\tag{26.5}
$$

With

$$
v_0=1,
\qquad v_n=z_\sigma r_n^\sigma,
\qquad a_k=z_\sigma c_k^\sigma,
$$

this becomes the exact scalar renewal recurrence

$$
\boxed{v_n=\sum_{k=1}^n a_kv_{n-k}.}
\tag{26.6}
$$

For `V_n=(-1)^nv_n` and `lambda_k=(-1)^ka_k`, the same recurrence is

$$
\boxed{V_n=\sum_{k=1}^n\lambda_kV_{n-k}.}
\tag{26.7}
$$

I independently checked the composition algebra. It does not use a finite-volume asymptotic or a depth-dependent choice of filter.

## 3. Fixed rational filter and finite margin

At

$$
P_*=(1/1000,1/10,9999/10000),
$$

take

$$
\sigma(u)=1-2e^{-\tau u},
\qquad \tau=4/125.
$$

Then `-1<=sigma<=1`, and the resolvent formula makes every finite coefficient rational. In particular

$$
\boxed{
z_\sigma
=\frac{114559900}{205809}.}
$$

G reports

$$
\lambda_1,\ldots,\lambda_5>0,
\qquad
\lambda_6,\lambda_7<0,
$$

with

$$
\sum_{k=1}^7\lambda_k
\approx1.047155757329804.
$$

The Professor reconstructed these seven coefficients independently from the finite generators and obtained the same displayed values to numerical precision. Because no verifier was committed with `394b7e3`, the exact rational inequalities are not yet promoted as a durable certificate; Assignment 010 must bank that verifier first.

The signs at `k=6,7` matter: a naive positive truncation at five connected blocks is invalid.

## 4. Exact route-killing tail criterion

If

$$
\boxed{
\sum_{k\ge8}|\lambda_k|
<
\delta_7,
\qquad
\delta_7:=\sum_{k=1}^7\lambda_k-1
\approx0.0471557573,
}
\tag{26.8}
$$

then absolute summability gives

$$
\sum_{k\ge1}\lambda_k>1.
$$

For

$$
F(r)=\sum_{k\ge1}\lambda_kr^{-k},
$$

continuity yields an `r_*>1` with `F(r_*)=1`. The generating function of `(26.7)` is

$$
\sum_{n\ge0}V_nz^n
=
\frac1{1-\sum_{k\ge1}\lambda_kz^k},
$$

so

$$
\limsup_n|V_n|^{1/n}\ge r_*>1.
$$

Together with `(26.1)`, this proves

$$
\boxed{\rho_J(P_*)>1.}
$$

Thus `(26.8)` is a concrete quantitative all-depth theorem, not another finite-depth growth diagnostic.

## 5. Why this is not F014's zero-frequency tail-shift theorem

The connected operator is

$$
\boxed{\mathcal K_N^\sigma=Q_N^\sigma J_N.}
\tag{26.9}
$$

The key distinction from F013--F014 is algebraic. There, one approximated a long evolved profile by its invariant projection and the error retained a shifted invariant law. Here every invariant projection is separated **exactly** and contributes to the renewal through `z_sigma Pi`; the connected coefficient contains only the complementary `Q` factors. In particular `(26.3)` removes the exact invariant spectral projection from every internal connected block.

So proving geometric decay of the connected coefficients would not amount to proving `Delta_M` or `Delta_M^(2)` small.

There is also an important limitation. `Q_N^sigma Pi_N=Pi_NQ_N^sigma=0` does **not** by itself give a contraction on the centered subspace, and it does not suppress arbitrarily slow nonzero modes automatically. On centered eigenmodes, `Q` acts through the nonzero-frequency resolvent multiplier. A depth-uniform connected-tail bound is therefore a real new theorem, not a consequence of the projection identity.

This distinction is exactly why the checkpoint clears the restart bar but only for one feasibility/certificate block.

## 6. Relation to earlier obstructions

F009 proves that the exact mode hierarchy generated by the local dynamics grows with depth. Therefore Assignment 010 may not simply posit a fixed finite-dimensional invariant mode space.

Meeting 025's finite-cylinder reproduction obstruction also remains in force for invertible factorized resolvents. The new renewal reduction does not contradict it: it asks for decay of connected coefficients, not an exact finite-cylinder eigenprofile.

The acceptable analytic mechanisms now include a depth-uniform seminorm estimate on the actual connected orbit, a cluster/finite-propagation estimate for the centered resolvent sequence, or another theorem that proves `(26.8)` directly. Merely computing more `lambda_k` does not count.

## 7. Assignment decision

Student G receives exactly one new task:

`students/student-g/assignment-010.md`.

Primary objective: prove `(26.8)` for the fixed filter `(26.3)` at `P_*`, or another rigorous tail theorem for the same exact renewal recurrence implying `rho_J(P_*)>1`.

The first durable step must be the missing exact verifier for the finite coefficients and `delta_7`.

A negative outcome is also useful if it proves that the connected coefficients cannot be bounded by a depth-uniform positive-frequency mechanism, or that the new connected problem actually recreates one of the stopped zero-frequency objects. That equivalence must be proved, not asserted.

No filter optimization, larger-depth coefficient table, generic matrix-product search, or return to bare tail-shift is authorized.

Student F remains idle.

## Ruling

- `state_narrowed: yes`.
- The post-Meeting-025 commit is accepted as an orchestration overlap, not a student disregard of the stop.
- The fixed-filter `L^1` witness and exact separator/connected renewal decomposition are accepted.
- The exact invariant projection is removed inside each connected coefficient; this is mathematically distinct from the stopped F013/F014 zero-frequency replacement error.
- The reported first-seven coefficient pattern has been independently reconstructed numerically; exact durable verification is still required.
- The connected-tail inequality `(26.8)` would prove `rho_J(P_*)>1`.
- One bounded connected-tail block is authorized as genuinely new input under Meeting 025's restart condition.
- Student G active on Assignment 010; Student F idle.

## Post-composition overlap correction

Commit `e4452de` (`students/student-g/009b-dual-renewal-verifier.py`) landed at 03:01:50 while Meeting 026 was already being composed and before Meeting 026 committed at 03:06:13. The statements above that the exact verifier was still missing are therefore stale working-snapshot statements, analogous to the previously recorded overlaps around Meetings 009, 011, and 014.

The Professor accepts `e4452de` as satisfying Assignment 010's finite-prefix checkpoint. It reconstructs `z_sigma` and `lambda_1,...,lambda_7` by exact rational finite-generator/resolvent algebra, verifies

$$
\lambda_1,\ldots,\lambda_5>0,
\qquad
\lambda_6,\lambda_7<0,
$$

and verifies exactly

$$
\sum_{k=1}^3\lambda_k>1,
\qquad
\sum_{k=1}^7\lambda_k>1.
$$

Although the script does not separately print the enormous rational for `delta_7`, `sum7` is an exact rational object and

$$
\delta_7=\mathrm{sum7}-1>0
$$

is therefore exactly certified. No repair or duplicate verifier commit is required.

**Operational consequence:** Assignment 010's first checkpoint is already complete. Student G should proceed directly to the all-depth connected-tail theorem `(26.8)` or another rigorous theorem for the same fixed filter and recurrence implying supercritical witness growth. The mathematical ruling and one-block scope of Meeting 026 are otherwise unchanged.
