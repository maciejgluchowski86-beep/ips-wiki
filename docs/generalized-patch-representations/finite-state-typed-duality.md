# Finite-state typed tensor duality

> **Research status.** Current programme result on `research/generalized-patch-representations`; not yet independently audited. The binary specialization is checked against the canonical patch paper.

## Setup

Let

\[
E=\{0,1,\ldots,d-1\},
\qquad E_*=E\setminus\{0\},
\]

where `0` is a distinguished reference state. Consider bounded single-site replacement dynamics

\[
L f(\eta)
=\sum_i\sum_{x\ne y}
1_{\{\eta_i=x\}}c_i^{x\to y}(\eta_{N(i)})
\bigl[f(\eta^{i,y})-f(\eta)\bigr].
\]

No attractiveness, reversibility, refresh structure, or translation invariance is assumed.

For one site use

\[
h_0\equiv1,
\qquad
h_a(x)=1_{\{x=a\}},\quad a\in E_*.
\]

A **typed active configuration** is a finite partial map

\[
\xi:\Lambda\rightharpoonup E_*.
\]

Its tensor observable is

\[
H_\xi(\eta)
=\prod_{i\in\operatorname{supp}\xi}1_{\{\eta_i=\xi(i)\}}.
\]

For a finite coordinate set these observables form a basis of the full cylinder algebra. They are the multi-state replacement for binary monomials.

## Typed tensor expansion

For a typed partial map `tau:A->E_*` on a finite set `K`, write `H_tau` for the corresponding indicator product. Every `f:E^K->R` has a unique expansion

\[
f=\sum_\tau \widehat f(\tau)H_\tau.
\]

If `z^{tau,B}` equals `tau` on `B subseteq A` and is `0` elsewhere, then

\[
\widehat f(\tau)
=
\sum_{B\subseteq A}(-1)^{|A|-|B|}f(z^{\tau,B}).
\]

This is Boolean-lattice Möbius inversion after the nonzero labels have been fixed.

Typed products use compatible union. If two partial maps assign the same label at every common site, merge them; if they assign different labels somewhere, the product is zero. It is convenient to adjoin a cemetery state `dagger` with

\[
H_\dagger=0.
\]

## Exact local generator action

Expand each neighbour rate in the typed basis,

\[
c_i^{x\to y}
=\sum_{\tau}\widehat c_i^{x\to y}(\tau)H_\tau.
\]

Suppose the dual configuration has active type

\[
r=\xi(i)\in E_*
\]

at the source site. For a typed neighbour target `tau`, the physical transitions combine into one signed coefficient for each possible **dual source outcome** `s in E`:

\[
a_{i,r}^{0}(\tau)
=\widehat c_i^{0\to r}(\tau),
\]

\[
a_{i,r}^{s}(\tau)
=
\widehat c_i^{s\to r}(\tau)-\widehat c_i^{0\to r}(\tau),
\qquad s\in E_*\setminus\{r\},
\]

and

\[
a_{i,r}^{r}(\tau)
=
-\widehat c_i^{0\to r}(\tau)
-
\sum_{y\ne r}\widehat c_i^{r\to y}(\tau).
\]

Here `s=0` means that the dual source is deleted; `s=r` means that it survives with the same type; another `s in E_*` means that it is retyped.

Let `Theta_{i;s,tau}(xi)` remove the source, reinsert it with type `s` when `s ne 0`, and then compatibly merge the typed target. A conflicting target gives `dagger`. Then

\[
L H_\xi
=
\sum_{i\in\operatorname{supp}\xi}
\sum_\tau
\sum_{s\in E}
 a_{i,\xi(i)}^s(\tau)
 H_{\Theta_{i;s,\tau}(\xi)}.
\]

The coefficients depend only on the local rate expansion and the source type, not on the rest of the current dual configuration.

## Signed graphical dual

For every non-diagonal local tuple `(i,r,s,tau)`, use a Poisson clock of rate

\[
\lambda_{i,r}^s(\tau)=|a_{i,r}^s(\tau)|
\]

and attach sign

\[
\epsilon_{i,r}^s(\tau)=\operatorname{sgn}_{\pm}(a_{i,r}^s(\tau)).
\]

A ring acts only when site `i` is currently dual-active with type `r`. It applies `Theta` and multiplies the sign by `epsilon`. Existing target labels affect only the deterministic merge/cemetery result; they do not alter the clock rate.

The empty-target source-survival tuple `(s,tau)=(r,empty)` is diagonal and is placed in the Feynman--Kac potential. With

\[
v_{i,r}
=
\sum_{(s,\tau)\ne(r,\emptyset)}|a_{i,r}^s(\tau)|
+a_{i,r}^r(\emptyset),
\qquad
V(\xi)=\sum_{i\in\operatorname{supp}\xi}v_{i,\xi(i)},
\]

the exact generator identity is

\[
L_\eta H(Y,\eta)=D H(Y,\eta)+V(\xi)H(Y,\eta).
\]

Under the same kind of Feynman--Kac integrability assumption used in the binary paper, finite-volume Feynman--Kac and finite-speed exhaustion give the corresponding semigroup duality.

## Binary specialization

For `E={0,1}` there is only one non-reference dual type. A typed target is just an ordinary subset `S`.

The two source outcomes are

\[
a_{i,1}^{0}(S)=c_i^0(S),
\]

and

\[
a_{i,1}^{1}(S)=-c_i^0(S)-c_i^1(S).
\]

Thus:

- `s=0`, `S=empty`: death;
- `s=0`, `S ne empty`: split;
- `s=1`, `S ne empty`: birth;
- `s=1`, `S=empty`: the diagonal empty-target birth coefficient in the potential.

This is exactly the signed monomial dual in the canonical paper.

## First successful-interaction record

For a nonempty typed target, superpose the clocks over the hidden source outcome:

\[
\Lambda_{i,r}(\tau)
=
\sum_{s\in E}|a_{i,r}^{s}(\tau)|.
\]

The natural coarse record is

\[
(i,t,r,\tau),
\]

which retains the source site, time, pre-interaction source type, and typed target, but hides the post-interaction source outcome `s`.

Every hidden branch has the same spacetime endpoints: an outgoing endpoint at `i` and incoming endpoints at the sites in `supp tau`. Therefore deletion, survival, and retyping do not alter patch geometry.

The source type `r` should generally be retained because the superposed intensity and outgoing consistency condition can depend on it. In the binary case `r` is unique and disappears from the notation, recovering the paper's record `(i,t,S)`.

## Next question

The unresolved step is **conditional factorization**. An incoming typed target may find its target site inactive, already active with the same type, or active with a conflicting type. The programme must determine whether the corresponding compatibility/consistency conditions remain local to disjoint source--time strips so that the hidden marks factorize patchwise.
