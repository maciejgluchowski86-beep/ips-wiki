# Group meeting 011: finite linear mode closure is impossible; move to profile regeneration/truncation

Date: 2026-08-16

Professor review of:

- Student F, commit `0ca0ef3`, `students/student-f/009-mode-resolved-l1-block.md`;
- exact verifier commit `9c2db13`, `students/student-f/009-mode-resolved-l1-verifier.py`;
- Meeting 010 and Student G's still-in-flight Assignment 005.

Student G remains in flight on `students/student-g/assignment-005.md` and is not interrupted.

state_narrowed: yes

Evidence pointer: `students/student-f/009-mode-resolved-l1-block.md`, especially Sections 2--8, and `students/student-f/009-mode-resolved-l1-verifier.py`.

## Previous bottleneck

Meeting 010 split the active trail route into:

1. a coupling-side all-height Foster problem, reduced by G to a 16-edge-phase / 64-triple feasibility problem for a nearest-neighbour product/coboundary corrector;
2. a signed analytic problem for the common mass law, where F had already shown that duration variables cannot be integrated before the `L^1(w)` norm and that a short static spin context is not an exact state.

Assignment 009 asked F either to build a depth-uniform finite mode closure for the signed mass/reset sector or to prove that such a closure cannot exist.

F proves the latter, while also obtaining a favorable exact contraction for the first transient mass mode.

## Professor verification: equilibrium and transient scalar mass modes both contract

Write

$$
B=b+c-a,
\qquad
\omega=1-c+a,
\qquad
r_0=\frac1{1+b},
$$

and

$$
Z_\alpha
=\int_0^\infty e^{-\alpha u}s_1(u)\,du
=\frac{\alpha+1+B+a}{(\alpha+a)(\alpha+1+B)-a}.
$$

For a signed mass component `nu`, define

$$
A=\nu(1),
\qquad
C=\nu(\eta_y)-r_0A.
$$

Under zero-boundary evolution of the rightmost spin,

$$
(\nu P_u)(\eta_y)=r_0A+Ce^{-(1+b)u},
$$

so the total signed coefficient produced by the next centered insertion is

$$
M_{A,C}(u)
=(Br_0-c)A+BCe^{-(1+b)u}.
$$

The equilibrium type has the already accepted cost

$$
\kappa_E=|Br_0-c|Z<\frac23.
$$

For the pure transient type,

$$
\kappa_T
:=B Z_{\omega+1+b}.
$$

Writing `k=1-c`, F gives

$$
\kappa_T
=\frac{(1+b-a-k)(a+2b+3)}
{4ab+5a+2b^2+2bk+5b+3k+3}.
$$

I checked that the denominator minus the numerator is

$$
\boxed{
a^2+5ab+ak+7a+4bk+6k>0.
}
$$

Hence

$$
\boxed{\kappa_T<1}
$$

throughout the strict residual chamber. Along the near-East path,

$$
\boxed{
\kappa_T
=1-\frac{13}{3}\varepsilon^2
+\frac{38}{9}\varepsilon^3
+O(\varepsilon^4).
}
$$

Thus the first transient mass mode is not itself expansive. The hard near-East `7/5` one-step expansion arose from normalizing only by the small equilibrium scalar while discarding an order-one transient component.

At the profile level, for old duration variables `v`,

$$
\mathcal M(A,C)(v,u)
=(Br_0-c)A(v)+Be^{-(1+b)u}C(v)
$$

satisfies

$$
\|\mathcal M(A,C)\|_{m+1}
\le
\kappa_E\|A\|_m+
\kappa_T\|C\|_m,
$$

with the old duration variables kept outside the absolute value. This respects the Meeting 009 norm-order restriction.

## Exact operator-valued transfer

F identifies the correct one-segment object. Slice a signed law according to the current rightmost spin:

$$
\nu_0(f)=\nu(f1_{\{\eta_y=0\}}),
\qquad
\nu_1(f)=\nu(f1_{\{\eta_y=1\}}).
$$

If `L^0,L^1` are the left-block generators with boundary spin fixed to zero or one, then

$$
\frac d{du}(\nu_0,\nu_1)
=(\nu_0,\nu_1)
\begin{pmatrix}
L^0-I&I\\
bI&L^1-bI
\end{pmatrix}.
$$

With

$$
\mathcal S(\nu_0,\nu_1)=-c\nu_0+(b-a)\nu_1,
$$

the duration-resolved transfer is

$$
\boxed{
(\mathfrak T_y\boldsymbol\nu)(u)
=\mathcal S\bigl(\boldsymbol\nu e^{u\mathbb Q_y}\bigr).
}
$$

The `J`-compatible block norm is therefore profile-valued/infinite-dimensional: all segment durations remain visible until the final absolute-value norm. A product of duration-integrated finite matrices is not equivalent to this object.

## Professor verification: no depth-uniform finite linear mode closure

Let `L_N` be the zero-boundary generator on `\{1,\ldots,N\}` in the centered-trail spin convention. For a site spin `x` and its right neighbour `y`,

$$
\boxed{
c(x,y)(1-2x)
=1-cy-(1+b)x+Bxy.
}
$$

The only degree-raising term is `Bxy`.

Starting from `eta_1`, a degree increase at each of `j` successive generator applications has a unique support chain

$$
\{1\}
\to\{1,2\}
\to\cdots
\to\{1,\ldots,j+1\}.
$$

Every step contributes `B`. Therefore, for `0<=j<=N-1`,

$$
\boxed{
L_N^j h_{p_*}(\eta_1)
=\frac{B^j}{q_*}\eta_1\eta_2\cdots\eta_{j+1}
+R_j,
\qquad \deg R_j\le j.
}
$$

Since `B,q_*>0`, these vectors have distinct nonzero top polynomial degrees and are linearly independent. Thus any linear space invariant under the zero-boundary semigroup and containing the one-site centered insertion must satisfy

$$
\boxed{
\dim E_N\ge N.
}
$$

This obstruction already holds at disagreement height zero. Consequently:

$$
\boxed{
\text{bounded disagreement/restart height does not imply bounded mass-mode dimension.}
}
$$

The depth-uniform finite generator/mode state proposed in Assignments 008--009 is therefore closed.

This does not rule out a depth-growing matrix representation, an infinite-dimensional Banach/profile norm, or a quantitative regeneration/truncation theorem.

## Relation to G Assignment 005

G's current task does not need amendment in flight.

Its 16 coupling phases address disagreement/restart bookkeeping. F's theorem concerns the common mass semigroup and proves that even with zero disagreement the exact linear mode dimension grows with spatial depth. Therefore, if G succeeds, its finite coupling cocycle will still act on an infinite-dimensional/profile-valued common-mass state rather than closing the full signed trail kernel by itself.

Assignment 005 already explicitly forbids G from claiming otherwise. G should finish its finite Foster feasibility block unchanged.

## Revised analytic target

The next F task is not another finite-mode enlargement. The remaining analytic question is whether the growing common-mass hierarchy can be cut quantitatively in the correct profile norm.

The preferred replacement theorem is a **profile regeneration/truncation estimate**: for a depth cutoff `M`, retain only dependence within `M` sites of the moving trail boundary and show that the `J`-weighted contribution of ancestry penetrating farther than `M` tends to zero as `M->infinity`, uniformly in the remaining trail depth at each fixed strict parameter point.

Environment-independent reset clocks at rates `a` and `1-c` are the natural source of such a regeneration estimate. Constants may deteriorate arbitrarily as the East boundary is approached.

A successful truncation theorem, combined with a valid coupling Foster result from G and finite-`M` signed control, would restore a finite approximation with a controllable error and could yield `J_{x,r}->0`.

## Ruling

The programme narrows again.

- The equilibrium and first transient mass types are both strictly damped in the right-weighted profile norm.
- The exact common-mass transfer is operator-valued and must retain duration profiles until the `L^1(w)` norm.
- A depth-uniform finite linear mode closure is impossible, already at disagreement height zero.
- G's 16-phase task remains useful but cannot by itself close the signed trail kernel.
- F is redirected to quantitative profile regeneration/truncation rather than another finite-mode ansatz.

The predecessor-trail Poisson--Mecke factorization and complementary no-exit term remain separate mandatory audits after a proof of `J_{x,r}->0`.
