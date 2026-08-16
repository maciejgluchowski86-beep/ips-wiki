# Project state

This file is the compact current-state index for the autonomous research programme. Detailed mathematics lives under `research/` and in Git history. `CHATGPT.md` governs the workflow except where the principal has explicitly fixed the present target below.

## Standing novelty standard

A quantitatively improved instance of an existing arbitrary-size/window/order method does not count as a new project result merely because it improves a numerical constant or range. Qualifying work must add structural mathematics or resolve/correct the target problem.

## Principal-fixed active scientific direction

**Positive rates conjecture for simple IPS.**

- Branch: `research/positive-rates-conjecture`.
- Workspace: `research/active/positive-rates-conjecture/`.
- Target fixed until changed or stopped by the principal: prove that every simple IPS with positive rates is ergodic.
- Latest meeting: `research/active/positive-rates-conjecture/meetings/020-recombined-zero-mode-survives-light-cone-screening-test.md`, `state_narrowed: yes`.
- Student F: active on `students/student-f/assignment-014.md`, the bounded light-cone screening test.
- Student G successor: idle. Common-uniform global-coalescence / zero-frequency occupation is abandoned as the load-bearing disagreement interface.

On `r11=0`, with

$$
a=r_{00},\qquad b=r_{01},\qquad c=r_{10},
$$

the unresolved residual chamber is

$$
\mathcal R=
\left\{0<a<b,\ \frac12\le c<1,\ c\ge a+b,\ b\ge\sqrt2(1-c)\right\}.
$$

### Current predecessor-trail target

Put

$$
B=b+c-a,\qquad g=b-a,\qquad\omega=1-c+a,
\qquad w(u)=e^{-\omega u}s_1(u).
$$

The centered predecessor-trail reduction leaves

$$
J_{x,r}
=B g^{n-1}\int\left(\prod_k w(u_k)\right)|\pi^0_{m,r}(F_{x,u})|du.
$$

Proving `J_{x,r}->0` with depth is sufficient for the nonempty-exit term. Every duration must remain visible until the final modulus.

### F013: intrinsic zero mode after signed recombination

With

$$
r_0=\frac1{1+b},
\qquad
m_0=\frac{b(1-c)-a}{1+b},
$$

and

$$
\rho_N=\mathcal J_N\pi_N-m_0\pi_{N-1},
$$

F013 proves for the full two-insertion defect

$$
E_{N,u}(f)
=m_0\rho_{N-1}(f)
+\rho_N(P_u-\Pi)[Y_{N-1}(f-\pi f)].
$$

Thus the zero temporal-frequency projection survives **before** any positive mass/disagreement split.

Moreover

$$
\rho_n(f)
=m_0(\bar\pi_n-\pi_{n-1})(f)
+B\pi_n[(\eta_n-r_0)f],
$$

and the covariance term is exponentially localized by F010. Hence off `m_0=0`, the remote zero mode differs from `|m_0|^2 Delta_{M+1}` only by an exponential error. The old zero-frequency obstruction was therefore not an artifact of splitting the signed insertion.

On the exact surface

$$
a=b(1-c),
$$

the zero-boundary invariant law is Bernoulli product, `J_N pi_N=0`, and the two-insertion defect vanishes identically.

### One remaining concrete mechanism

F013 does not decide the actual weighted norm

$$
\Gamma_M
=\sup_N\int_0^\infty w(u)\|E_{N,u}\|_{\mathrm{remote},M}du,
$$

because the transient complement may cancel the zero mode at the same duration.

Meeting 020 rejects generic depth-uniform observability/mixing as another restatement. It isolates one concrete finite-propagation mechanism instead. Since

$$
0\le w(u)\le e^{-\omega u},
\qquad
\|E_{N,u}\|_{TV}\le2c^2,
$$

late durations `u>=alpha M` already cost at most

$$
\frac{2c^2}{\omega}e^{-\omega\alpha M}.
$$

Thus it suffices to prove short-time **light-cone screening**, for example

$$
\|E_{N,u}\|_{\mathrm{remote},M}
\le
C e^{-\gamma M}
+C P(\operatorname{Pois}(\Lambda u)\ge\delta M),
\qquad 0\le u\le\alpha M.
$$

Assignment 014 first tests the static centered two-site suffix covariance at `u=0`, then the graphical finite-speed extension to positive time.

If this succeeds, `Gamma_M` decays exponentially. If it fails structurally or returns unresolved without a sharper mechanism, the present predecessor-trail/profile implementation is recorded as exhausted rather than continued by generic observability, third insertions, matrix products, or reopened common-uniform occupation.

## Most recently completed programme

`VOTER-CONC-001` is mathematically verified but not a new project result under the standing novelty standard.

## Wiki freeze

The live wiki remains frozen during active research.
