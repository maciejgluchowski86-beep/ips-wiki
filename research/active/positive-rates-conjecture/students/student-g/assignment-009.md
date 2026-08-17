# Student G assignment 009: decide whether the absolute-duration `J` norm is asymptotically supercritical

Work on branch `research/positive-rates-conjecture`.

Read first:

- `meetings/022-no-credible-proof-architecture-but-j-route-decision-reopened.md`;
- `notes/principal-target-hierarchy-and-j-norm-evidence.md`;
- `notes/principal-centered-trail-reduction.md`, especially the canonical singleton predecessor-trail quantity;
- current `proof-spine.md`;
- Meeting 021 only for the fact that the previous profile implementation is exhausted.

Read F013/F014 only if needed to avoid accidentally reintroducing their stopped zero-frequency mechanism. Do not restart your common-coupling work.

The scientific target remains the positive rates conjecture. This assignment is **not** a proof attempt for the conjecture. It is a route-decision problem: determine whether the absolute-duration `J` bound which has been treated as a sufficient predecessor-trail target is itself false at a strict residual point.

## 1. Canonical object

Use the exact singleton depth-`n` specialization of the predecessor-trail quantity in the current proof spine. Denote it by `J_n`.

The principal's separate numerical study used a normalization `N_n` with

$$
J_n=\frac gB N_n,
\qquad
B=b+c-a,
\qquad
g=b-a.
$$

Since `g/B` is depth-independent, define

$$
\boxed{
\rho_J(a,b,c)
:=
\limsup_{n\to\infty}J_n^{1/n}
=
\limsup_{n\to\infty}N_n^{1/n}.
}
\tag{J0}
$$

The rendered principal capture mangled some intermediate profile symbols. Reconstruct the exact `J_n` / `N_n` recursion from the canonical predecessor-trail files. Do not rely on ambiguous rendered notation.

## 2. Primary parameter point

Work first at the strict residual point

$$
\boxed{
(a,b,c)=\left(\frac1{1000},\frac1{10},\frac{9999}{10000}\right).
}
\tag{P*}
$$

The principal's unverified finite-box calculation reports

$$
N_{10}\approx2.3975,
\qquad
\left(\frac{N_{10}}{N_7}\right)^{1/3}\approx1.153.
$$

A secondary point, if algebraically easier, is

$$
\left(\frac1{500},\frac1{10},\frac{9999}{10000}\right),
$$

where the reported three-depth ratio is about `1.070`.

You must independently reconstruct any finite-depth values you use. The principal's numbers are motivation, not input authority.

## 3. Primary objective: prove the route-killing alternative

Prove

$$
\boxed{
\rho_J(P_*)>1.
}
\tag{J+}
$$

This requires an **asymptotic theorem**. Finite-depth values, however accurate, do not prove `(J+)`.

A successful certificate may take any rigorous form. Examples include:

1. a finite block of durations and a finite cone/class of normalized signed profiles which reproduces after each block and expands the absolute-duration mass by a factor `lambda>1`;
2. a positive minorization / regeneration kernel giving
   $$
   J_{n+m}\ge\lambda J_n
   $$
   along an infinite subsequence with `lambda>1`;
3. a Perron--Frobenius lower certificate for an exact finite positive operator which is genuinely embedded in the full depth recursion and has spectral radius above one;
4. a periodic duration-sector/sign construction producing a repeatable lower bound with exponential growth;
5. another exact asymptotic argument implying `limsup J_n^(1/n)>1`.

The principal observed alternating signed duration sectors. You may exploit a subset on which the relevant integrand has controlled sign, but the subset must recur under the exact depth evolution rather than being selected independently at each finite depth.

## 4. Opposite valid outcome

If the numerical growth is transient and you instead prove

$$
\rho_J<1
$$

at `(P*)`, or on a genuine residual subregion containing it, that is equally decisive.

A stronger theorem `rho_J<1` throughout the residual chamber would revive the absolute-duration target, though the exhausted proof implementation would still need replacement.

## 5. What does not count

Do not return as a positive result:

- `N_n` computed at larger finite depths;
- Monte Carlo evidence with smaller error bars;
- stabilization of finite-volume temporal spectral gaps;
- a finite block diagnostic above one with no theorem that the block can repeat;
- a lower bound for an artificial profile process which is not embedded in the canonical `J` recursion;
- a signed resolvent pairing which decays while the absolute `J` norm remains undecided.

Those may be diagnostics inside the work, but they do not decide `(J-SPEC)`.

## 6. Computational standard

You may use computation heavily to discover a certificate. The final decisive statement must be rigorous.

For a finite certificate, prefer exact rationals, interval arithmetic, or analytic remainder bounds. If numerical quadrature is unavoidable, certify the tails and all sign/minorization inequalities. A floating-point optimizer output alone is not evidence for `(J+)`.

If you derive a finite positive operator, document exactly why repeated application is dominated by / embedded in the true infinite-depth `J` recursion. This embedding is the load-bearing step.

## 7. Do not work on the later signed-resolvent route yet

The principal's study also proposes scalar signed Laplace-resolvent decay `(ML)` and eventual exact right-region targets `(JT)` / `(MR)`.

Do **not** make those the main task here.

They become relevant only after `(J-SPEC)` is decided. In particular, a small sampled value of a signed resolvent does not prove ergodicity and does not by itself refute the absolute-duration norm.

## 8. Stopping rule

This is one bounded route-decision block justified by new principal evidence after consultation 002 returned `no-credible-route`.

End with exactly one of:

- `J-SPEC refuted absolute-duration route: rho_J >= ... > 1 at ...`;
- `J-SPEC supports absolute-duration route: rho_J <= ... < 1 on ...`;
- `unresolved after substantive work; asymptotic J blocker: ...`.

If the third outcome contains only deeper finite-depth evidence and no new asymptotic mechanism, do not propose another larger-`n` assignment.

**Meeting 023 routing update:** the mathematical assignment above is unchanged, but a genuinely new stationary boundary-control architecture is now being tested independently by Student F. Therefore an unresolved G009 stops the `J-SPEC` branch only; it no longer by itself returns the entire programme to `no-credible-route` while F015 is in flight.

## 9. Workflow durability addendum

Your Assignment 009 session has twice been lost during long uninterrupted reasoning runs before a final report could be committed. To avoid losing another substantive block, commit intermediate results whenever they become mathematically durable, even if the final `(J-SPEC)` decision is not yet reached.

Good checkpoint material includes:

- an exact reconstruction of the canonical depth recursion;
- a proved lower-sector invariance lemma;
- a candidate embedded positive operator with exact entries;
- a rigorous obstruction showing why a proposed repeatable sector cannot close;
- verifier code for any exact finite algebra used later.

Use clearly labelled intermediate files or commits; do not overstate them as the final Assignment 009 conclusion.

## 10. Durable output

Commit the final report to

`research/active/positive-rates-conjecture/students/student-g/009-j-norm-growth-route-decision.md`

with verifier/certificate code beside it when computation is used.
