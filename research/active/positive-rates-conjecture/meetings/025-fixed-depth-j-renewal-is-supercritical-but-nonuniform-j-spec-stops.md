# Group meeting 025: fixed-depth `J` renewal is supercritical but nonuniform; `(J-SPEC)` branch stops

Date: 2026-08-17

Professor review of:

- Meeting 024 and its explicit fallback if G009 did not produce a target-relevant asymptotic theorem;
- Student G final commit `1fe3637`, `students/student-g/009-j-norm-growth-route-decision.md`, and its exact verifier;
- G's durable checkpoint `2cb0696` / `2a2f66b`, which fixed the canonical recursion and normalization before the later session freezes;
- Assignment 009 and its requirement that finite-depth growth count only if embedded in a repeatable fixed-parameter mechanism;
- F013--F014 only at the interface needed to identify the all-depth long-reset error;
- current `state.md` and `proof-spine.md`.

`state_narrowed: yes`.

Evidence pointer: G009 equations `(0.3)`--`(0.5)`, the all-depth East Green identity `(3.3)`, the fixed-depth short/long renewal argument in Section 4, the order-of-limits obstruction in Section 5, and Proposition 6.1. The verifier checks the exact rational constants and the East basis identity through depth nine; the fixed-depth convergence argument is analytic and is carried by the report rather than by the verifier.

## Ruling in one sentence

G009 produces real asymptotic structure but does **not** decide `(J-SPEC)` at any fixed strict residual point. Its supercritical factor `499/341` belongs to the singular order of limits `epsilon -> 0` at fixed depth; making the long-reset channel repeat uniformly in depth requires the same uncontrolled spatial reset/tail-shift theorem already isolated by F014 and stopped in Meeting 021. Therefore Assignment 009's route-decision branch stops, no G010 is issued, both students are idle, and the programme returns to consultation 002's `no-credible-route` proof-architecture state pending genuinely new principal or external input.

This is not a closure of the positive-rates conjecture and not a proof that `rho_J<=1` or `rho_J>1` anywhere.

## 1. Canonical normalization and exact recursion remain accepted

The checkpoint `2cb0696` gives the exact reverse-transfer formulation. With

$$
Y=B\eta-c=g h_{p_*},
$$

successive insertions can be written as

$$
F_1=Y_1,
\qquad
F_{j+1}=Y_{j+1}P_{u_j}^{j,0}F_j,
\qquad
A_n(u)=\pi_n(F_n).
$$

Writing

$$
I_n
=\int_{(0,\infty)^{n-1}}
\left(\prod_{j=1}^{n-1}w(u_j)\right)|A_n(u)|\,du,
$$

one has

$$
J_n=\frac Bg ZI_n.
$$

Equivalently, for G's raw reverse-transfer norm `R_n` and the principal normalization `N_n`,

$$
\boxed{
J_n=\frac Bg R_n=\frac gB N_n,
}
$$

so all three sequences have the same exponential growth rate. This normalization issue is closed.

At

$$
P_*=\left(\frac1{1000},\frac1{10},\frac{9999}{10000}\right),
$$

the exact calibration remains

$$
B=\frac{10989}{10000},\qquad
 g=\frac{99}{1000},\qquad
\omega=\frac{11}{10000},\qquad
Z=\frac{19100}{31}.
$$

The depth-one values are normalization checks only and carry no asymptotic conclusion.

## 2. Fixed-depth singular renewal theorem accepted in its actual scope

G considers the strict residual family

$$
a=\varepsilon,
\qquad b=\frac1{10},
\qquad 1-c=\frac\varepsilon{10},
\qquad 0<\varepsilon<\frac1{10},
\tag{25.1}
$$

which contains `P_*` at `epsilon=10^{-3}`.

For every **fixed** depth `n`, G proves

$$
\boxed{
\lim_{\varepsilon\downarrow0}
\frac{I_n(\varepsilon)}{|m_0(\varepsilon)|}
=
\left(\frac{499}{341}\right)^{n-1},
}
\tag{25.2}
$$

where

$$
m_0=\frac{b(1-c)-a}{1+b}=-\frac9{10}\varepsilon.
$$

Consequently

$$
\boxed{
\lim_{\varepsilon\downarrow0}J_n(\varepsilon)
=
\frac{2079}{341}
\left(\frac{499}{341}\right)^{n-1}.
}
\tag{25.3}
$$

The fixed-depth base splits as

$$
\boxed{
\frac{499}{341}
=
\frac{10}{11}+rac{189}{341}>1.
}
\tag{25.4}
$$

I accept this as a genuine explanation of the principal's finite-depth growth, not as a finite-depth fit.

The analytic mechanism is a binary short/long renewal decomposition with threshold `T_epsilon=epsilon^{-1/2}`. At fixed volume, short gaps converge to an East Green extraction and long gaps converge to the invariant projection. Because the number of sectors is finite for fixed `n`, their limiting weights sum to `(r+mu)^{n-1}`.

The verifier exactly confirms

$$
r=\frac{10}{11},
\qquad
\mu=\frac{189}{341},
\qquad
r+\mu=\frac{499}{341},
$$

and the associated rational normalization. It does not, correctly, assert any fixed-`epsilon` statement about `rho_J`.

## 3. The short channel has an all-depth exact East identity

At the East endpoint, with

$$
X_i=(1+b)\eta_i-1,
$$

G introduces the linear functional

$$
\ell_m(X_A)=b^{|A|}{\bf1}_{\{1\in A\}}.
$$

For multiplication/extraction at the rightmost site `E_m`, the centered East generator satisfies

$$
\boxed{
\ell_{m-1}E_m(-L_m^E)^{-1}
=
\frac1{1+b}\ell_m
=
\frac{10}{11}\ell_m
}
\tag{25.5}
$$

on the centered subspace.

The proof is combinatorial: all interior terms cancel under `ell`, and only the zero-boundary contribution survives. This is genuinely all-depth. The verifier checks the underlying basis identity on every nonempty subset through `m=9`; the algebraic proof itself is depth-free.

Thus the short multiplier `10/11` is not the source of nonuniformity.

## 4. The long regenerated channel is exactly where uniformity fails

Along `(25.1)`, the long invariant-projection weight satisfies

$$
\boxed{
|m_0|Z\longrightarrow\mu=\frac{189}{341}.
}
\tag{25.6}
$$

At every fixed finite depth, a gap `u>T_epsilon` is long enough for the current finite zero-boundary chain to relax to its invariant projection. This gives the second renewal channel in `(25.4)`.

But `(J-SPEC)` fixes `epsilon>0` and sends depth to infinity. The finite-volume relaxation replacement used in the long channel is not uniform in depth. What is needed is a depth-uniform statement saying that after a sufficiently long gap the evolved signed profile can be replaced by its invariant scalar mass against **all future left tests**, with a summable or contracting error.

F013--F014 identify the error in precisely such a replacement. After local suffix and finite-propagation pieces are removed, the remaining remote term contains the one-/two-step shifted zero-boundary invariant-law defect. In F014 notation this is the same spatial zero-frequency/tail-shift information represented by

$$
\Delta_M^{(2)}
=\|\theta^2\mu-\mu\|_{\mathcal F_M}.
$$

Therefore the missing uniform long reset is not a new G009 mechanism waiting for one more estimate. It is the same all-depth spatial reset theorem at which the predecessor-profile implementation was stopped in Meeting 021.

The order of limits is consequently load-bearing:

$$
\lim_{\varepsilon\downarrow0}\quad\text{at fixed }n
$$

does not control

$$
\limsup_{n\to\infty}\quad\text{at fixed }\varepsilon.
$$

The supercritical fixed-depth base cannot be promoted to `rho_J(P_*)>1`.

## 5. Factorized finite-cylinder Perron--Frobenius closure is also obstructed

G proves a separate algebraic obstruction. For an invertible suffix-compatible factorized duration operator `K_m` preserving the natural suffix subspaces, define

$$
T_mf=Y_{m+1}K_mf.
$$

There is no nonzero finite-cylinder profile `phi`, block length `p>=1`, and `lambda!=0` satisfying an exact reproduction cycle

$$
T_{m+p-1}\cdots T_m\phi
=\lambda\,\phi\circ\theta^p.
\tag{25.7}
$$

The proof peels the suffix-invariant subspace backwards through the invertible factors until `phi` is forced to be constant, after which multiplication by the nonconstant nowhere-zero `Y` prevents reproduction.

The ordinary Laplace-resolvent filters considered in G009 are invertible in the relevant half-plane, so this obstruction applies to that generic finite-memory implementation.

I accept this at its stated scope. It does not refute `(J+)`; it rules out an exact finite-cylinder eigenprofile for nonsingular factorized resolvents. Infinite-memory, singular-filter, or nonfactorized constructions are not thereby disproved. They are also not concrete continuation mechanisms presently supported by an independent theorem.

## 6. `(J-SPEC)` remains mathematically open

G proves neither

$$
\rho_J(P_*)>1
$$

nor

$$
\rho_J(P_*)<1,
$$

and no corresponding inequality at the secondary strict point.

The principal's depth-ten growth evidence remains compatible with genuine supercriticality, but an eventual late-depth crossover caused by remote signed spatial memory remains equally unexcluded.

Thus the route-decision question itself remains open.

## 7. Why the new structure does not clear the continuation bar

There is a wording point worth making explicit. Meeting 024 said that if G009 returned without a genuine asymptotic theorem, the programme would revert to the consultation-002 state. G009 **does** prove an asymptotic theorem, but it is a singular fixed-depth theorem in the parameter `epsilon`; it is not the target-relevant uniform-in-depth theorem required by Assignment 009.

Assignment 009 pre-registered the stronger requirement: a valid positive outcome must embed a repeatable mechanism in the canonical recursion at fixed strict rates. A finite block diagnostic or a mechanism that repeats only after taking `epsilon->0` at each fixed depth does not count.

G's own analysis identifies why no such embedding is currently available: the missing uniform reset is the stopped tail-shift problem. Hence the report materially narrows the state but does **not** clear the continuation bar for another `J` block.

The same zero-frequency spatial-memory object has now appeared from three genuinely different reductions:

1. F013's unsplit two-insertion spectral projection;
2. F014's short-time light-cone screening normal form;
3. G009's attempt to repeat the long regenerated renewal channel uniformly in depth.

This convergence of obstructions is evidence against issuing another representation-level variant without new input.

## 8. Stop-rule application and current programme state

Meeting 024 left G009 as the sole active internal block and stated that an unresolved fixed-rate route decision returns the programme to consultation 002's `no-credible-route` proof-architecture state absent genuinely new principal or external input.

No such new input has arrived between Meetings 024 and 025.

Accordingly:

- the `(J-SPEC)` **internal route-decision branch stops**; no larger-depth numerical continuation is authorized;
- no G010 is issued;
- Student G becomes idle;
- Student F remains idle; no F016;
- the stationary occupation hierarchy remains valid reusable mathematics, but its current Bellman-concatenation implementation is stopped by Meeting 024;
- the common-uniform occupation interface remains abandoned;
- the centered predecessor-trail/profile implementation remains exhausted;
- `(ML)`, `(JT)`, `(MR)`, generic trajectory exactness, generic joint Bellman-corrector searches, and alternative coupling/norm searches are **not** activated merely because all present branches have stopped.

The programme therefore returns to the following precise state:

> The principal-fixed positive-rates conjecture remains the scientific target, but **no presently identified proof architecture clears the continuation bar for another substantial internal block**.

This is consultation 002's `no-credible-route` conclusion updated with the additional exact negative/structural information from F015 and G009.

Work should resume only after a genuinely new mathematical or literature input supplies a concrete rate-level mechanism that is not a restatement of tail-shift/spatial reset, common-coupling occupation, generic path-space contraction, or generic Bellman/joint-corrector search.

## Ruling

- `state_narrowed: yes`.
- G009's canonical normalization and reverse-transfer recursion are accepted.
- The fixed-depth singular renewal theorem `(25.2)`--`(25.4)` is accepted in its stated order of limits.
- The all-depth East Green extraction identity `(25.5)` is accepted.
- The fixed-depth supercritical base `499/341` does **not** imply `rho_J>1` at any fixed strict residual point.
- Repeating the long channel uniformly requires the same unresolved spatial reset/tail-shift information isolated by F014.
- The finite-cylinder exact reproduction cycle is unavailable for invertible suffix-compatible factorized resolvents, at the scope proved by G.
- `(J-SPEC)` remains open and its authorized internal branch stops.
- No G010 and no F016.
- Both students idle.
- No current proof architecture is active; consultation 002's `no-credible-route` assessment is reinstated as the operative proof-architecture status pending genuinely new input.
