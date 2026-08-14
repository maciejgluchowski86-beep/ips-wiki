---
title: Self-consistent patch iteration for the quadratic Hessian PDE
status: proved here
tags:
  - PDE
  - parabolic equation
  - Hessian
  - Schauder estimate
  - H minus one
  - diffusion
---

# Self-consistent patch iteration for the quadratic Hessian PDE

For a small quadratic Hessian nonlinearity on the one-dimensional torus, the deterministic patch equation closes by a semi-implicit iteration. A uniform Schauder ball keeps every linearized coefficient in a fixed ellipticity window, while an [\(H^{-1}\) energy estimate](h-minus-one-energy-method.md) makes successive second-derivative profiles contract. The limit is the unique solution in the small uniformly parabolic class and admits an implicit diffusion representation whose coefficient contains the fixed point itself.

This theorem is deterministic. It uses the exact [finite-depth patch regrouping](finite-depth-duhamel-patch-regrouping.md), but it does not assert that the corresponding infinite random-patch importance sampler is integrable.

**References.** The linear regularity input is standard periodic parabolic Schauder theory; see [Parabolic maximum principle and Schauder estimates](parabolic-maximum-principle-and-schauder-estimates.md) and the references there. The \(H^{-1}\) argument is given in [The \(H^{-1}\) energy method on the torus](h-minus-one-energy-method.md). The theorem below is proved here.

## Forward equation

Let

$$
\mathbb T=\mathbb R/(2\pi\mathbb Z),
$$

fix \(T>0\), \(0<\alpha<1\), \(\lambda\in\mathbb R\), and \(\phi\in C^{2+\alpha}(\mathbb T)\). We consider

$$
\partial_tv
=
\frac12\partial_x^2v
+\lambda(\partial_x^2v)^2,
\qquad
v(0,\cdot)=\phi.
\tag{1}
$$

The corresponding backward terminal problem is obtained from \(u(t,x)=v(T-t,x)\).

Write

$$
z=\partial_x^2v.
$$

Then formally

$$
\partial_tz
=
\partial_x^2\left[
\left(\frac12+\lambda z\right)z
\right],
\qquad
z(0,\cdot)=\phi''.
\tag{2}
$$

## A uniform Schauder constant

Let \(\mathcal A_{\alpha,T}\) be the class of coefficients \(a\in C^{\alpha/2,\alpha}([0,T]\times\mathbb T)\) satisfying

$$
\frac38\leq a\leq\frac58,
\qquad
[a]_{C^{\alpha/2,\alpha}}\leq\frac18.
\tag{3}
$$

By periodic parabolic Schauder theory, there is a finite constant \(C_{\mathrm{Sch}}(\alpha,T)\geq1\), chosen uniformly over \(a\in\mathcal A_{\alpha,T}\), such that the solution of

$$
\partial_tv=a(t,x)v_{xx},
\qquad
v(0)=\phi,
\tag{4}
$$

satisfies

$$
\lVert v_{xx}\rVert_{C^{\alpha/2,\alpha}([0,T]\times\mathbb T)}
\leq
C_{\mathrm{Sch}}(\alpha,T)
\lVert\phi\rVert_{C^{2+\alpha}}.
\tag{5}
$$

The dependence on the Hölder bound in (3) is part of the definition of this uniform constant; ellipticity alone would not give (5).

Set

$$
R
=
C_{\mathrm{Sch}}(\alpha,T)
\lVert\phi\rVert_{C^{2+\alpha}}.
\tag{6}
$$

## Theorem

Assume

$$
|\lambda|R
\leq
\frac18.
\tag{7}
$$

Define \(z_0(t,x)=\phi''(x)\). Given \(z_n\), let \(v_{n+1}\) solve

$$
\partial_tv_{n+1}
=
\left(\frac12+\lambda z_n\right)
\partial_x^2v_{n+1},
\qquad
v_{n+1}(0)=\phi,
\tag{8}
$$

and set

$$
z_{n+1}=\partial_x^2v_{n+1}.
\tag{9}
$$

Equivalently,

$$
\partial_tz_{n+1}
=
\partial_x^2\left[
\left(\frac12+\lambda z_n\right)z_{n+1}
\right],
\qquad
z_{n+1}(0)=\phi''.
\tag{10}
$$

Then:

1. every iterate satisfies
   $$
   \lVert z_n\rVert_{C^{\alpha/2,\alpha}}
   \leq R,
   \qquad
   \frac38
   \leq
   \frac12+\lambda z_n
   \leq
   \frac58;
   \tag{11}
   $$
2. \((z_n)\) converges in \(L^2([0,T]\times\mathbb T)\) and uniformly on \([0,T]\times\mathbb T\) to a function \(z\), with
   $$
   \lVert z\rVert_{C^{\alpha/2,\alpha}}
   \leq R;
   \tag{12}
   $$
3. \((v_n)\) converges to a classical solution \(v\) of (1), with \(v_{xx}=z\);
4. this solution is unique among bounded weak solutions whose second derivative satisfies \(|\lambda z|\leq1/8\);
5. for every \(t\leq T\), the solution has the self-consistent diffusion representation
   $$
   v(t,x)
   =
   \mathbb E_x[\phi(X_t)],
   \tag{13}
   $$
   where, for this fixed terminal time \(t\),
   $$
   dX_s
   =
   \sqrt{1+2\lambda z(t-s,X_s)}\,dW_s,
   \qquad
   X_0=x,
   \qquad
   0\leq s\leq t.
   \tag{14}
   $$

The expectation in (13) is therefore implicit: the diffusion coefficient contains the already constructed fixed point \(z=v_{xx}\).

## Proof: preservation of the Hölder ball

Suppose

$$
\lVert z_n\rVert_{C^{\alpha/2,\alpha}}
\leq R.
$$

By (7),

$$
|\lambda z_n|
\leq\frac18,
\qquad
[\lambda z_n]_{C^{\alpha/2,\alpha}}
\leq\frac18.
$$

Hence

$$
a_n
:=
\frac12+\lambda z_n
\in
\mathcal A_{\alpha,T}.
$$

The Schauder estimate (5) applied to (8) gives

$$
\lVert z_{n+1}\rVert_{C^{\alpha/2,\alpha}}
\leq R.
$$

Since \(C_{\mathrm{Sch}}\geq1\), the time-independent initialization \(z_0=\phi''\) lies in the same ball. Induction proves (11).

The interval \([3/8,5/8]\) is the ellipticity window for the *linear iteration coefficient* \(a_n\). The nonlinear equation (1), viewed as a quasilinear equation in \(v_{xx}\), has derivative

$$
\frac{d}{dz}\left(\frac12z+\lambda z^2\right)
=
\frac12+2\lambda z,
$$

which lies in \([1/4,3/4]\) under the same smallness bound.

## Proof: \(H^{-1}\) contraction

For \(n\geq1\), put

$$
w_n=z_{n+1}-z_n.
$$

Subtracting the equations for \(z_{n+1}\) and \(z_n\) gives

$$
\partial_tw_n
=
\partial_x^2\left[
\left(\frac12+\lambda z_n\right)w_n
+\lambda z_nw_{n-1}
\right].
\tag{15}
$$

Every \(z_n\) has spatial mean zero because its initial datum is \(\phi''\) and the right-hand side of (10) is a second derivative. Hence \(w_n\) has mean zero and the [\(H^{-1}\) energy identity](h-minus-one-energy-method.md) applies.

Set

$$
\kappa=\frac38,
\qquad
\delta=|\lambda|R\leq\frac18.
$$

Using \(a_n\geq\kappa\) and \(|\lambda z_n|\leq\delta\), the energy estimate yields

$$
\sup_{0\leq s\leq t}
\lVert w_n(s)\rVert_{H^{-1}}^2
+
\kappa\int_0^t\lVert w_n(s)\rVert_2^2\,ds
\leq
\frac{\delta^2}{\kappa}
\int_0^t\lVert w_{n-1}(s)\rVert_2^2\,ds.
\tag{16}
$$

Therefore

$$
\lVert w_n\rVert_{L^2_tL^2_x}
\leq
q\,
\lVert w_{n-1}\rVert_{L^2_tL^2_x},
\qquad
q
=
\frac\delta\kappa
\leq
\frac13.
\tag{17}
$$

Thus \((z_n)\) is Cauchy in space-time \(L^2\).

## Proof: uniform convergence and passage to the limit

The uniform bound (11) makes \((z_n)\) equibounded and equicontinuous in the parabolic Hölder metric. By Arzelà--Ascoli, every subsequence has a uniformly convergent subsubsequence. Any such uniform limit must coincide almost everywhere with the unique \(L^2\) limit, so the whole sequence converges uniformly to \(z\). Passing to the Hölder inequalities also gives (12).

The Schauder estimates give a uniform \(C^{1+\alpha/2,2+\alpha}\) bound on \((v_n)\). Any convergent subsequence therefore has a limit with second derivative \(z\). The spatial mean

$$
m_n(t)
=
\frac1{2\pi}\int_{\mathbb T}v_n(t,x)\,dx
$$

removes the remaining constant ambiguity. From (8),

$$
m_{n+1}'(t)
=
\lambda\frac1{2\pi}
\int_{\mathbb T}z_n(t,x)z_{n+1}(t,x)\,dx.
\tag{18}
$$

Uniform convergence of the \(z_n\) therefore determines a unique limiting mean. Hence all subsequential limits of \(v_n\) coincide, so \(v_n\to v\). Passing to the limit in (8) gives

$$
\partial_tv
=
\left(\frac12+\lambda z\right)z,
\qquad
z=v_{xx},
$$

which is (1).

## Proof: uniqueness in the small class

Let \(z\) and \(\widetilde z\) be bounded weak solutions of (2) with the same initial datum and

$$
|\lambda z|,
|\lambda\widetilde z|
\leq
\frac18.
$$

Their difference \(w=z-\widetilde z\) satisfies

$$
\partial_tw
=
\partial_x^2\left[
\left(
\frac12+\lambda(z+\widetilde z)
\right)w
\right].
\tag{19}
$$

The coefficient in (19) lies in \([1/4,3/4]\). Testing in \(H^{-1}\) gives

$$
\frac12\frac{d}{dt}
\lVert w\rVert_{H^{-1}}^2
=
-
\int_{\mathbb T}
\left(
\frac12+\lambda(z+\widetilde z)
\right)w^2\,dx
\leq
-\frac14\lVert w\rVert_2^2.
$$

Since \(w(0)=0\), one gets \(w=0\). Once \(z\) is fixed, two periodic solutions \(v\) with \(v_{xx}=z\) differ only by a spatial constant, and the common initial condition together with the equation fixes that constant. Thus the solution \(v\) is unique in the stated small class.

## Proof: torus mean

Let

$$
m(t)
=
\frac1{2\pi}\int_{\mathbb T}v(t,x)\,dx.
$$

Because \(z=v_{xx}\) has zero spatial mean, averaging (1) gives

$$
m'(t)
=
\lambda\frac1{2\pi}
\int_{\mathbb T}z(t,x)^2\,dx.
\tag{20}
$$

Hence

$$
m(t)
=
m(0)
+
\lambda\int_0^t
\frac1{2\pi}
\int_{\mathbb T}z(s,x)^2\,dx\,ds.
\tag{21}
$$

This is the integration constant that is lost if one works only with \(z=v_{xx}\).

## Proof: self-consistent diffusion

For fixed \(t\leq T\), put

$$
a(r,x)=\frac12+\lambda z(r,x).
$$

The coefficient is Hölder continuous and satisfies \(3/8\leq a\leq5/8\). Let \(X\) be the one-dimensional periodic diffusion with time-reversed generator

$$
a(t-s,x)\partial_x^2,
$$

which is equivalently written as the SDE (14). The standard diffusion law is well defined for this uniformly elliptic Hölder coefficient.

Apply Itô's formula to \(s\mapsto v(t-s,X_s)\). Since the quadratic variation of (14) is

$$
d\langle X\rangle_s
=
2a(t-s,X_s)\,ds,
$$

the drift is

$$
-v_t(t-s,X_s)
+a(t-s,X_s)v_{xx}(t-s,X_s)
=0.
$$

Thus \(v(t-s,X_s)\) is a martingale. At \(s=t\), its value is \(v(0,X_t)=\phi(X_t)\), while at \(s=0\) it is \(v(t,x)\). Taking expectations proves (13).

## Deterministic patch interpretation

The mild form of (10) is

$$
z_{n+1}(t)
=
P_t\phi''
+
\lambda\int_0^t
\partial_x^2P_{t-s}
[z_n(s)z_{n+1}(s)]\,ds.
\tag{22}
$$

For fixed side profile \(z_n\), iterating (22) sums arbitrary consecutive left-spine Hessian events before the next outer Picard step. This is the deterministic patch resummation suggested by the [finite-depth patch theorem](finite-depth-duhamel-patch-regrouping.md). The convergence proof above uses Schauder regularity and \(H^{-1}\) contraction, not an absolute-moment bound for a random patch functional.
