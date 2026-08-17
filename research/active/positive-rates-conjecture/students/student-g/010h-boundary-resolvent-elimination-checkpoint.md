# Student G 010h checkpoint: eliminate the filtered tail-shift functional exactly

**Status:** intermediate durable checkpoint for Assignment 010. This sharpens 010g. The one-step stationary marginal discrepancy `delta_N` is not an irreducible object in the connected coefficient: using its exact source equation and the terminal resolvent factor, it can be eliminated algebraically in favor of a probability expectation of an explicit right-boundary resolvent block. This does not yet prove the tail theorem.

## 1. Setup

Retain 010g notation at `P_*`. Put

\[
r=1+b=\frac{11}{10},\qquad
S_N=(rI-L_N)^{-1},
\]

\[
R_N=(dI-gL_N)S_N,
\qquad
d=-\varepsilon r,
\qquad \varepsilon=\frac9{10000},
\qquad g_0:=g+\varepsilon=\frac{999}{10000}.
\]

Let

\[
D_N:=(I-L_N)S_N.
\]

For the connected orbit

\[
f_1=Y_1,
\qquad
f_N=Y_NQ_{N-1}f_{N-1},
\]

write

\[
q_N:=Q_Nf_N.
\]

Then `pi_N(q_N)=0`, and 010g gives

\[
c_{N+1}=\delta_N(R_Nq_N),
\tag{1}
\]

and

\[
\delta_NL_N=-B A_ND_NP_N,
\tag{2}
\]

where `A_N` is the left `N`-site marginal of `pi_{N+1}` and hence a probability functional.

## 2. Exact elimination of `delta_N`

Set

\[
u_N:=S_Nq_N.
\]

Since `(rI-L_N)u_N=q_N`, applying `delta_N` and using `(2)` gives

\[
\delta_N(q_N)
=r\,\delta_N(u_N)+B A_ND_NP_Nu_N.
\tag{3}
\]

Also, from `(1)` and `(2)`,

\[
\begin{aligned}
c_{N+1}
&=d\,\delta_N(u_N)-g\,\delta_N(L_Nu_N)\\
&=d\,\delta_N(u_N)+gB A_ND_NP_Nu_N.
\end{aligned}
\tag{4}
\]

Because `pi_NQ_N=0`,

\[
\delta_N(q_N)=A_N(q_N).
\tag{5}
\]

Eliminating `delta_N(u_N)` between `(3)` and `(4)` yields

\[
\boxed{
 c_{N+1}
 =A_N\!\left[
 \frac dr\,q_N
 +\left(g-\frac dr\right)B
 D_NP_NS_Nq_N
 \right].
}
\tag{6}
\]

At `P_*`, `d/r=-epsilon` and `g-d/r=g_0`, so

\[
\boxed{
 c_{N+1}
 =A_N\!\left[
 -\varepsilon q_N
 +g_0B(I-L_N)(rI-L_N)^{-1}
 P_N(rI-L_N)^{-1}q_N
 \right].
}
\tag{7}
\]

This identity is exact at every depth.

Thus the appearance of the bare stationary discrepancy in 010g equation (6) is removable: no estimate of `||delta_N||` or of unrestricted tail-shift TV is logically required for the connected coefficient. What remains is an estimate on the explicit boundary-resolvent expression in `(7)` along the actual connected orbit `q_N`.

## 3. Elementary uniform bound and why it is not enough

The resolvent is a scaled Markov operator:

\[
S_N=\frac1rK_N,
\qquad
K_N=r(rI-L_N)^{-1}.
\]

Hence

\[
\|S_Nh\|_\infty\le\frac1r\|h\|_\infty.
\tag{8}
\]

Moreover

\[
D_N=(I-L_N)S_N=I-bS_N,
\]

so

\[
\|D_Nh\|_\infty\le\left(1+\frac br\right)\|h\|_\infty.
\tag{9}
\]

If `h=u+Y_Nv` is the last-coordinate decomposition, then

\[
v=\frac{h(\cdot,1)-h(\cdot,0)}B,
\qquad
P_Nh=Y_Nv,
\]

and since `|Y_N|<=c`,

\[
\|P_Nh\|_\infty\le\frac{2c}{B}\|h\|_\infty.
\tag{10}
\]

Because `pi_N(q_N)=0`, its range contains zero and therefore

\[
\|q_N\|_\infty\le\operatorname{osc}(q_N).
\tag{11}
\]

Combining `(7)`--`(11)` and that `A_N` is a probability functional gives

\[
\boxed{
|c_{N+1}|
\le C_*\operatorname{osc}(q_N),
}
\tag{12}
\]

with the exact rational constant

\[
\boxed{
C_*
=\varepsilon+
\frac{2cg_0}{r}\left(1+\frac br\right)
=\frac{342081}{1718750}
\approx0.19902894545.
}
\tag{13}
\]

This bound is much too crude by itself after multiplication by `z_sigma`; it is recorded only to make the remaining target explicit. A successful continuation must exploit cancellation/local structure inside

\[
\boxed{
\mathfrak B_N q
:=-\varepsilon q
+g_0B D_NP_NS_Nq,
}
\tag{14}
\]

rather than bounding its factors separately.

## 4. Consequence for the stopping alternatives

010g showed that the connected coefficient could be written as a filtered pairing against `delta_N`; `(7)` now shows that this does **not** establish equivalence to the stopped zero-frequency tail-shift problem. The exact Poisson equation removes `delta_N` completely.

The narrowed all-depth problem is therefore:

> prove summable decay of `A_N(\mathfrak B_Nq_N)` for the actual recursion `q_N=Q_N(Y_Nq_{N-1})`, or prove a structural obstruction to such a boundary-resolvent estimate.

Any negative equivalence with the old bare tail-shift object would have to survive the exact elimination `(7)` and therefore requires additional mathematics beyond 010g.
