# Proof spine: generalized patch representations

Date: 2026-08-17

## Target

Extend the patch representation / patch positivity mechanism beyond binary flip spin systems while preserving the core architecture:

1. a tensor basis of local observables;
2. an exact signed Feynman--Kac dual;
3. a graphical interaction process with a coarser successful-interaction skeleton;
4. conditional factorization into spacetime patches after hidden marks are averaged;
5. a local nonnegativity criterion on bulk patch contributions;
6. consequences such as order preservation, comparison, or convergence in concrete models.

## E0. Binary benchmark

**Settled by the canonical paper.**

Binary monomials yield the signed death/split/birth set process. The successful skeleton records source/time/target but hides split versus birth. Conditioning on that skeleton yields independent one-site patch laws.

Any generalization must reduce exactly to this construction.

## E1. Canonical local basis for a finite state space

**Settled in Assignment 001.**

For finite `E={0,...,d-1}` with reference state `0`, use

\[
h_0\equiv1,
\qquad h_a(x)=1_{\{x=a\}},\quad a\ne0.
\]

Tensor observables are indexed by finite typed partial maps `xi:Lambda -> E\{0}` and form a basis of every finite cylinder algebra.

Typed products merge equal labels and give zero on conflicting labels. The zero product is represented by a cemetery state `dagger`.

Decisive file: `students/professor/001a-typed-generator-action.md`.

## E2. Exact signed dual for single-site replacement dynamics

**Settled in Assignment 001.**

For general bounded single-site replacement rates, expansion in the typed tensor basis gives fixed local branch coefficients

\[
a_{i,r}^{0}(\tau)=\widehat c_i^{0\to r}(\tau),
\]

\[
a_{i,r}^{s}(\tau)=\widehat c_i^{s\to r}(\tau)-\widehat c_i^{0\to r}(\tau),
\quad s\ne0,r,
\]

\[
a_{i,r}^{r}(\tau)
=-\widehat c_i^{0\to r}(\tau)-\sum_{y\ne r}\widehat c_i^{r\to y}(\tau).
\]

Their absolute values are local Poisson rates; signs are sign marks. The source outcome `s` deletes, preserves, or retypes the active source. Typed target conflicts affect only the deterministic transition to `dagger`, not the clock rate.

The empty-target source-survival coefficient is inserted into the Feynman--Kac potential, giving an exact generator duality. Under the same type of FK integrability hypothesis as the binary paper, this yields semigroup duality.

The `d=2` specialization is exactly the paper's death/split/birth process.

Decisive files: `001b-signed-typed-dual.md` and `001-finite-state-duality-verifier.py`.

## E3. Hidden mark / successful interaction analogue

**Settled at the geometric level in Assignment 001.**

For nonempty typed target `tau`, superpose the clocks over source outcome `s` at fixed `(i,r,tau)` and record

\[
(i,t,r,\tau).
\]

The pre-interaction source type `r` is revealed. The post-interaction source outcome `s` is hidden.

Every branch has one outgoing endpoint at `i` and incoming endpoints at `supp tau`, so deletion/survival/retyping does not change patch geometry.

The source type `r` should normally be retained because the aggregate record intensity and outgoing consistency condition depend on it.

Decisive file: `001c-coarse-typed-skeleton.md`.

## E4. Generalized typed patch factorization

**Open and current load-bearing edge.**

The natural local patch state is now type-valued:

\[
X_u^P\in E,
\]

with `0` interpreted as dual-inactive and `a in E_*` as active with type `a`.

Expected boundary conditions:

- incoming start carrying type `a`: the new patch begins with local type `a`;
- outgoing start with record `(i,s,r,tau)`: the hidden source outcome chooses the post-interaction local type;
- outgoing terminal with source type `r'`: consistency requires `X_{e-}^P=r'`;
- incoming terminal carrying type `a'`: compatibility requires `X_{e-}^P in {0,a'}`; a different active type is a cemetery conflict.

The first question is whether these consistency constraints still factor into disjoint source--time-strip events under the Poisson reference law.

The serious new issue is the cemetery path. A conflicting incoming target can kill the entire typed dual, after which all future successful records disappear globally. The programme must determine whether conflict skeletons can be discarded as zero-weight histories or represented by local zero factors without losing the factorization needed for the semigroup representation.

Do not move to positivity until this is settled.

## E5. Generalized patch positivity

**Blocked on E4.**

Need a local criterion ensuring every bulk typed patch contribution is nonnegative. It must reduce to the binary multilinear coefficient inequalities.

## E6. Applications

**Blocked on E5, except for reconnaissance.**

Priority examples should genuinely use more than two local states or a non-flip replacement mechanism and should not be contrived binary encodings.
