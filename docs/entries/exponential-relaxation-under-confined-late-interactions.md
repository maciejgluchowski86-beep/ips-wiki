---
title: Late interactions and no-late relaxation
status: proved here
audit: current
tags:
  - patch
  - ergodicity
  - spin systems
  - convergence
  - pure deaths
---

# Late interactions and no-late relaxation

This entry contains the temporal part of the canonical paper's proof of the common invariant limit. It includes the comparison weights, the backward chain of outgoing-terminal patches, the late-interaction estimate, the probability-weighted continuation identities, the end-factor relaxation estimate, and the no-late-interaction bound.

Assume the spin system is patch positive and contains a uniform pure-death component of rate $\varepsilon>0$:

$$
\mathcal L
=
\mathcal L^\varepsilon
+
\varepsilon\mathcal N^{\mathbf0}.
\tag{1}
$$

Let $P_t^\varepsilon$ and $C^\varepsilon$ denote the semigroup and patch contributions for $\mathcal L^\varepsilon$. The two systems have the same signed dual jumps, successful-interaction skeleton, reference patch laws, and threshold profile $\mathbf p^\star$.

Fix $A\Subset\Lambda$. For $\mu\in\mathcal M_*$ define

$$
W_t^\mu
=
\prod_{P\in\mathcal B_t}C(P)
\,\mu\left(
\prod_{P\in\mathcal E_t}C(\eta(i(P)),P)
\right),
\tag{2}
$$

and let $W_t^{\varepsilon,\mu}$ be the analogous weight with $C^\varepsilon$. Define the full-patch weights

$$
W
=
\prod_{P\in\mathcal P}C(P)
\mathbf1_{\{|\mathcal P|<\infty\}},
\qquad
W^\varepsilon
=
\prod_{P\in\mathcal P}C^\varepsilon(P)
\mathbf1_{\{|\mathcal P|<\infty\}}.
\tag{3}
$$

## Nonnegative comparison weights

For every $\mu\in\mathcal M_*$ and $t\ge0$,

$$
0\le W_t^\mu\le W_t^{\varepsilon,\mu},
\qquad
\mathbb E_A[W_t^{\varepsilon,\mu}]
=(\mu P_t^\varepsilon)(\chi_A)
\le1.
\tag{4}
$$

Moreover,

$$
0\le W\le W^\varepsilon,
\qquad
\mathbb E_A[W^\varepsilon]\le1.
\tag{5}
$$

If $P$ has outgoing terminal boundary, then

$$
C(P)
=
e^{-\varepsilon(e(P)-s(P))}C^\varepsilon(P).
\tag{6}
$$

### Proof

For $\mathcal Q\subseteq\mathcal E_t$, write

$$
I(\mathcal Q)=\{i(P):P\in\mathcal Q\}.
$$

The centered end-factor expansion gives

$$
\begin{aligned}
W_t^\mu
={}&
\prod_{P\in\mathcal B_t}C(P)
\sum_{\mathcal Q\subseteq\mathcal E_t}
\mu(\chi^*_{I(\mathcal Q)})
\prod_{P\in\mathcal Q}\kappa(P)\\
&\hspace{8em}\times
\prod_{P\in\mathcal E_t\setminus\mathcal Q}
C(p_{i(P)}^\star,P).
\end{aligned}
\tag{7}
$$

For $\mu\in\mathcal M_*$, every centered moment in (7) is nonnegative. The patchwise [pure-death comparison](pure-death-comparison-under-patch-positivity.md) gives

$$
0\le C(P)\le C^\varepsilon(P),
$$

for bulk patches and

$$
0\le C(p_{i(P)}^\star,P)
\le C^\varepsilon(p_{i(P)}^\star,P),
\qquad
0\le\kappa(P)\le\kappa^\varepsilon(P)
$$

for end patches. Hence every term in (7) is nonnegative and is bounded by the corresponding $\varepsilon$-term. This proves the first inequality in (4). The [patch representation](patch-representation-of-spin-systems.md) for $\mathcal L^\varepsilon$ gives

$$
\mathbb E_A[W_t^{\varepsilon,\mu}]
=(\mu P_t^\varepsilon)(\chi_A)\le1.
$$

Pointwise comparison also gives $0\le W\le W^\varepsilon$. On $\{|\mathcal P|<\infty\}$, the all-one finite-horizon weights converge to $W^\varepsilon$, while $W^\varepsilon=0$ on the complementary event. Therefore

$$
W^\varepsilon
\le
\liminf_{u\to\infty}W_u^{\varepsilon,\mu_{\mathbf1}},
$$

and Fatou's lemma proves (5).

Finally, if $P$ has outgoing terminal boundary, consistency forces its base site to remain dual-active throughout $[s(P),e(P))$. Removing the pure deaths changes the one-site potential from $V_i$ to $V_i+\varepsilon$ and changes neither the patch sign nor the consistency normalizer. Thus pathwise

$$
F(P)
=
e^{-\varepsilon(e(P)-s(P))}F^\varepsilon(P),
$$

and taking the common consistent-patch expectation proves (6).

## Backward chain of outgoing patches

Let $(i,u,S)$ be a successful-interaction record with $u>0$. There are distinct patches $P_1,\ldots,P_n$, each with outgoing terminal boundary, such that

$$
s(P_1)=0,
\qquad
e(P_n)=u,
\tag{8}
$$

and, for $1\le k<n$,

$$
e(P_k)=s(P_{k+1}),
\qquad
i(P_{k+1})\in N_*(i(P_k)).
\tag{9}
$$

Consequently,

$$
\sum_{k=1}^n(e(P_k)-s(P_k))=u.
\tag{10}
$$

### Proof

Start with the patch at the source $i$ ending at $u$. Its terminal boundary is outgoing because $i$ is dual-active immediately before the successful interaction.

Trace predecessors backward. If the current patch begins with an incoming interaction, take the patch at the source of that incoming interaction that ends at the same boundary time. If the current patch begins with an outgoing interaction, consistency forces that interaction to be a birth, so the source remains active; take the preceding patch at the same site. In either case, the predecessor has outgoing terminal boundary.

The boundary times decrease strictly. Local finiteness therefore forces the backward construction to reach time $0$ after finitely many steps. Reverse the resulting list. Consecutive intervals meet at their endpoints, and the later base site is either the same site or a target of the earlier successful interaction, giving (9). The intervals partition $[0,u)$, which proves (10).

## Late interactions

For $0\le T<t$, let $L_{T,t}$ be the event that no successful interaction occurs in $(T,t]$, and let $L_T$ be the event that no successful interaction occurs after $T$.

Let $E_T^R$ be the confinement event from [spatial confinement](undoing-duality-under-confined-interactions.md). For every $\mu\in\mathcal M_*$,

$$
0
\le
\mathbb E_A\left[
W_t^\mu\mathbf1_{E_T^R\cap L_{T,t}^c}
\right]
\le
e^{-\varepsilon T},
\tag{11}
$$

and

$$
0
\le
\mathbb E_A\left[
W\mathbf1_{E_T^R\cap L_T^c}
\right]
\le
e^{-\varepsilon T}.
\tag{12}
$$

### Proof

On $L_{T,t}^c$, let $u\in(T,t]$ be the first successful-interaction time after $T$ and let $P_1,\ldots,P_n$ be the backward chain from (8)-(10). Every chain patch is a bulk patch at horizon $t$. By (6) and (10),

$$
\prod_{k=1}^n C(P_k)
=
e^{-\varepsilon u}
\prod_{k=1}^n C^\varepsilon(P_k)
\le
e^{-\varepsilon T}
\prod_{k=1}^n C^\varepsilon(P_k).
\tag{13}
$$

Compare the centered expansions of $W_t^\mu$ and $W_t^{\varepsilon,\mu}$ term by term. Every remaining bulk factor, end constant, and end slope is bounded by its $\varepsilon$ counterpart, while each centered moment is nonnegative. Hence

$$
W_t^\mu\mathbf1_{L_{T,t}^c}
\le
e^{-\varepsilon T}W_t^{\varepsilon,\mu}.
\tag{14}
$$

Taking expectations and using (4) proves (11); the extra indicator $E_T^R$ only decreases the left-hand side.

On $\{|\mathcal P|<\infty\}\cap L_T^c$, the same argument applied to the first successful interaction after $T$ gives

$$
W\mathbf1_{L_T^c}
\le
e^{-\varepsilon T}W^\varepsilon.
$$

Taking expectations and using (5) proves (12).

## Continuation without successful interactions

For $P\in\mathcal E_T$ and $t>T$, continue its local active process after $T$ using only future outgoing marks at $i(P)$ and no incoming boundary. Let $L_{T,t}^P$ be the event that no nonempty-target mark acts while this continuation is active in $(T,t]$.

Conditional on $\mathcal G_T$, the events $(L_{T,t}^P)_{P\in\mathcal E_T}$ are independent. A first successful interaction after $T$ must have its source in one of the end patches, and until that time its active indicator agrees with the corresponding one-site continuation. Hence

$$
L_{T,t}
=
\bigcap_{P\in\mathcal E_T}L_{T,t}^P,
\qquad
\mathbb P(L_{T,t}\mid\mathcal G_T)
=
\prod_{P\in\mathcal E_T}
\mathbb P(L_{T,t}^P\mid\mathcal G_T).
\tag{15}
$$

Let $L_T^P$ be the analogous event with no future successful interaction at any time after $T$.

### Proposition: probability-weighted continuation

On $L_{T,t}$,

$$
\mathcal B_t=\mathcal B_T,
\qquad
\mathcal E_t
=
\{P^{\uparrow t}:P\in\mathcal E_T\}.
\tag{16}
$$

For every probability measure $\mu$,

$$
\begin{aligned}
&\mathbb E\left[W_t^\mu\mathbf1_{L_{T,t}}\mid\mathcal G_T\right]\\
&\quad=
\prod_{P\in\mathcal B_T}C(P)
\,\mathbb P(L_{T,t}\mid\mathcal G_T)
\,\mu\left(
\prod_{P\in\mathcal E_T}
C(\eta(i(P)),P^{\uparrow t})
\right)\\
&\quad=
\prod_{P\in\mathcal B_T}C(P)
\,\mu\left(
\prod_{P\in\mathcal E_T}
C(\psi_{i(P)}(t-T,\eta(i(P))),P)
\right).
\end{aligned}
\tag{17}
$$

Moreover,

$$
\mathbb E\left[W\mathbf1_{L_T}\mid\mathcal G_T\right]
=
\prod_{P\in\mathcal B_T}C(P)
\prod_{P\in\mathcal E_T}C(p_{i(P)}^\circ,P),
\tag{18}
$$

where

$$
p_i^\circ
=
\frac{c_i^0(\varnothing)}{c_i^0(\varnothing)+c_i^1(\varnothing)}.
$$

The first equality in (17) also holds for $W_t^{\varepsilon,\mu}$ with $C$ replaced by $C^\varepsilon$; the conditional probability is unchanged because the two systems have the same dual and reference patch laws.

### Proof

The patch-family identities (16) follow directly from the geometric definition of $P^{\uparrow t}$: on $L_{T,t}$ no patch begins or ends after $T$.

Fix $P\in\mathcal E_T$, write

$$
i=i(P),
\qquad
S=S(P),
\qquad
\Delta=T-s(P),
\qquad
h=t-T.
$$

The consistency normalizers in the patch-contribution formulas give

$$
\mathbb P(L_{T,t}^P\mid\mathcal G_T)
=
\begin{cases}
\displaystyle
\frac{\varphi_i(\Delta+h)}{\varphi_i(\Delta)},
&\mathsf X(P)=\mathsf I,\\[1.3em]
\displaystyle
\frac{
\delta_i(S)+\beta_i(S)\varphi_i(\Delta+h)
}{
\delta_i(S)+\beta_i(S)\varphi_i(\Delta)
},
&\mathsf X(P)=\mathsf O.
\end{cases}
\tag{19}
$$

Multiplying the ordinary contribution of the geometric extension by (19), and using the semigroup identity

$$
\psi_i(\Delta+h,z)
=
\psi_i(\Delta,\psi_i(h,z)),
$$

gives the local probability-weighted continuation identity

$$
\mathbb P(L_{T,t}^P\mid\mathcal G_T)
C(z,P^{\uparrow t})
=
C(\psi_i(h,z),P).
\tag{20}
$$

For an incoming patch, this is exactly

$$
\frac{\varphi_i(\Delta+h)}{\varphi_i(\Delta)}
\frac{\psi_i(\Delta+h,z)}{\varphi_i(\Delta+h)}
=
\frac{\psi_i(\Delta,\psi_i(h,z))}{\varphi_i(\Delta)}.
$$

For an outgoing patch, the factor $\delta_i(S)+\beta_i(S)\varphi_i(\Delta+h)$ cancels and the same composition identity acts in the numerator. These are precisely the two rows of $C(\psi_i(h,z),P)$.

Conditional independence in (15) lets the local identities (20) multiply over end patches, proving the second equality in (17); the first is the conditional expectation of the finite-horizon weight on $L_{T,t}$. The same calculation applies to $\mathcal L^\varepsilon$.

Uniform pure deaths imply

$$
r_i=c_i^0(\varnothing)+c_i^1(\varnothing)\ge\varepsilon,
$$

so

$$
\psi_i(h,z)\longrightarrow p_i^\circ
$$

as $h\to\infty$. Taking the limit in (20) with $z=1$ gives the limiting local factor $C(p_i^\circ,P)$. The finitely many end-patch future increments are conditionally independent, so multiplying the local limits proves (18), including cases in which an infinite geometric extension itself has zero consistency probability.

## End-factor relaxation

Fix $\mathcal G_T$ and $0\le T<t$. For every $\mu\in\mathcal M_*$,

$$
\begin{aligned}
&\left|
\mathbb P(L_{T,t}\mid\mathcal G_T)
\mu\left(
\prod_{P\in\mathcal E_T}C(\eta(i(P)),P^{\uparrow t})
\right)
-
\prod_{P\in\mathcal E_T}C(p_{i(P)}^\circ,P)
\right|\\
&\quad\le
e^{-\varepsilon(t-T)}
\Bigg[
\mathbb P(L_{T,t}\mid\mathcal G_T)
\mu\left(
\prod_{P\in\mathcal E_T}C^\varepsilon(\eta(i(P)),P^{\uparrow t})
\right)\\
&\hspace{13em}
+
|\mathcal E_T|
\prod_{P\in\mathcal E_T}C(p_{i(P)}^\circ,P)
\Bigg].
\end{aligned}
\tag{21}
$$

### Proof

Put $h=t-T$. For $P\in\mathcal E_T$ based at $i$, define

$$
\begin{aligned}
a_t(P)
&=
\mathbb P(L_{T,t}^P\mid\mathcal G_T)
C(p_i^\star,P^{\uparrow t}),\\
k_t(P)
&=
\mathbb P(L_{T,t}^P\mid\mathcal G_T)
\partial_zC(z,P^{\uparrow t}),\\
a_t^\varepsilon(P)
&=
\mathbb P(L_{T,t}^P\mid\mathcal G_T)
C^\varepsilon(p_i^\star,P^{\uparrow t}),\\
k_t^\varepsilon(P)
&=
\mathbb P(L_{T,t}^P\mid\mathcal G_T)
\partial_zC^\varepsilon(z,P^{\uparrow t}),\\
b(P)&=C(p_i^\circ,P).
\end{aligned}
\tag{22}
$$

From (20) and the affine end-factor formula,

$$
a_t(P)=C(\psi_i(h,p_i^\star),P),
\qquad
k_t(P)=e^{-r_i h}\kappa(P),
\qquad
b(P)=C(p_i^\circ,P).
\tag{23}
$$

For the system with pure deaths removed, the empty-neighbour rate is $r_i-\varepsilon$, so

$$
k_t^\varepsilon(P)
=e^{-(r_i-\varepsilon)h}\kappa^\varepsilon(P).
$$

The patchwise pure-death comparison and the common continuation probability yield

$$
0\le a_t(P)\le a_t^\varepsilon(P),
\qquad
0\le k_t(P)\le e^{-\varepsilon h}k_t^\varepsilon(P).
\tag{24}
$$

Also $p_i^\star\le p_i^\circ$ by the empty-neighbour bound, and hence

$$
\begin{aligned}
b(P)-a_t(P)
&=
\kappa(P)(p_i^\circ-p_i^\star)e^{-r_i h}\\
&\le
e^{-\varepsilon h}b(P).
\end{aligned}
\tag{25}
$$

Now distribute the product probability in (15) among the end factors and expand around $\mathbf p^\star$:

$$
\begin{aligned}
&\mathbb P(L_{T,t}\mid\mathcal G_T)
\mu\left(
\prod_{P\in\mathcal E_T}C(\eta(i(P)),P^{\uparrow t})
\right)\\
&\quad=
\sum_{\mathcal Q\subseteq\mathcal E_T}
\mu(\chi^*_{I(\mathcal Q)})
\prod_{P\in\mathcal Q}k_t(P)
\prod_{P\in\mathcal E_T\setminus\mathcal Q}a_t(P).
\end{aligned}
\tag{26}
$$

All terms are nonnegative. For $\mathcal Q\ne\varnothing$, (24) bounds the corresponding summand by $e^{-\varepsilon h}$ times its $\varepsilon$ counterpart. Thus the difference between (26) and its $\mathcal Q=\varnothing$ term is bounded by

$$
e^{-\varepsilon h}
\mathbb P(L_{T,t}\mid\mathcal G_T)
\mu\left(
\prod_{P\in\mathcal E_T}C^\varepsilon(\eta(i(P)),P^{\uparrow t})
\right).
\tag{27}
$$

Enumerate $\mathcal E_T=\{P_1,\ldots,P_n\}$ and write $a_j=a_t(P_j)$, $b_j=b(P_j)$. The telescoping identity

$$
\prod_{j=1}^n b_j-
\prod_{j=1}^n a_j
=
\sum_{j=1}^n
(b_j-a_j)
\prod_{k<j}a_k
\prod_{k>j}b_k
$$

and (25) give

$$
0
\le
\prod_{P\in\mathcal E_T}b(P)
-
\prod_{P\in\mathcal E_T}a_t(P)
\le
|\mathcal E_T|e^{-\varepsilon h}
\prod_{P\in\mathcal E_T}b(P).
\tag{28}
$$

Both target quantities in (21) lie above the common product $\prod_Pa_t(P)$. Adding the bounds (27) and (28) proves (21).

## No-late-interaction relaxation

For $A\subseteq R\Subset\Lambda$, $\mu\in\mathcal M_*$, and $0\le T<t$,

$$
\left|
\mathbb E_A\left[
W_t^\mu\mathbf1_{E_T^R\cap L_{T,t}}
\right]
-
\mathbb E_A\left[
W\mathbf1_{E_T^R\cap L_T}
\right]
\right|
\le
(1+|R|)e^{-\varepsilon(t-T)}.
\tag{29}
$$

### Proof

Let

$$
B_T=\prod_{P\in\mathcal B_T}C(P).
$$

Use (17)-(18) and then apply the conditional estimate (21). The conditional absolute difference is bounded by

$$
\begin{aligned}
&e^{-\varepsilon(t-T)}B_T
\mathbb P(L_{T,t}\mid\mathcal G_T)
\mu\left(
\prod_{P\in\mathcal E_T}
C^\varepsilon(\eta(i(P)),P^{\uparrow t})
\right)\\
&\quad+
e^{-\varepsilon(t-T)}B_T|\mathcal E_T|
\prod_{P\in\mathcal E_T}C(p_{i(P)}^\circ,P).
\end{aligned}
\tag{30}
$$

On $E_T^R$, the map $P\mapsto i(P)$ sends $\mathcal E_T$ bijectively onto $\mathbf{Cone}_T$, so

$$
|\mathcal E_T|\le|R|.
\tag{31}
$$

Let $B_T^\varepsilon=\prod_{P\in\mathcal B_T}C^\varepsilon(P)$. Since $B_T\le B_T^\varepsilon$, the $\varepsilon$ version of the continuation identity gives

$$
\begin{aligned}
&\mathbb E_A\Bigg[
\mathbf1_{E_T^R}B_T
\mathbb P(L_{T,t}\mid\mathcal G_T)
\mu\left(
\prod_{P\in\mathcal E_T}C^\varepsilon(\eta(i(P)),P^{\uparrow t})
\right)
\Bigg]\\
&\qquad\le
\mathbb E_A\left[
W_t^{\varepsilon,\mu}\mathbf1_{E_T^R\cap L_{T,t}}
\right]
\le1.
\end{aligned}
\tag{32}
$$

Similarly, by (18), (31), and $\mathbb E_A[W]\le1$,

$$
\begin{aligned}
&\mathbb E_A\left[
\mathbf1_{E_T^R}B_T|\mathcal E_T|
\prod_{P\in\mathcal E_T}C(p_{i(P)}^\circ,P)
\right]\\
&\qquad\le
|R|\,\mathbb E_A\left[
W\mathbf1_{E_T^R\cap L_T}
\right]
\le|R|.
\end{aligned}
\tag{33}
$$

Taking expectations in (30) and using (32)-(33) proves (29).

## Three-term estimate

Combining [spatial confinement](undoing-duality-under-confined-interactions.md), the late-interaction estimates (11)-(12), and the no-late estimate (29) gives, for $\mu\in\mathcal M_*$,

$$
\left|
(\mu P_t)(\chi_A)-\mathbb E_A[W]
\right|
\le
2\rho_A(T,R)
+2e^{-\varepsilon T}
+(1+|R|)e^{-\varepsilon(t-T)}.
\tag{34}
$$

The [common invariant-limit theorem](common-invariant-limit-under-uniform-pure-deaths.md) completes the argument by choosing a linearly growing confinement ball and $T=t/2$.
