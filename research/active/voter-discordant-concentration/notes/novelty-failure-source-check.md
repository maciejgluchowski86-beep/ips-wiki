# Professor source check: fatal prior-art comparison

Date: 2026-08-16

I independently checked the primary Avena--Baldasso--Hazra--den Hollander--Quattropani (2024) source after the negative novelty audit.

The publication-matching arXiv v2 contains:

- Proposition 4.1 proof, equation (4.2): on the event that the endpoint-walk families of two edges do not cross-interact by time `t`, the two discordance events satisfy the needed decoupling/negative-dependence upper bound;
- equation (5.5): the four-endpoint cross-family interaction time;
- equation (5.6):
  $$
  \mathbf P_{\nu\otimes\nu}(\tau^{e,f}\le t)
  \le4\mathbf P_{\pi\otimes\pi}(\tau_{\rm meet}\le t);
  $$
- Lemma 5.2, equation (5.8): the short-time stationary hitting estimate used with `E tau_meet = Theta(n)` and the spectral-gap input.

For Bernoulli initial opinions, the no-cross-interaction event separates the ancestral labels used by the two edge-discordance indicators. If `X_e,X_f` are those indicators, then

$$
\operatorname{Cov}(X_e,X_f)
\le \mathbf P(\tau^{e,f}\le t).
$$

Averaging over ordered uniform edges and using source (5.6) yields

$$
\operatorname{Var}(\mathcal D_t)
\le4\mathbf P_{\pi\otimes\pi}(\tau_{\rm meet}\le t).
$$

Thus the project's constant-`2` theorem is a sharper version of an immediate constant-`4` corollary of the source. Since the random-regular asymptotic conclusions discard constants, source (5.8) then already implies the same corrected and `t>=1` concentration scales by Chebyshev.

This independently confirms the novelty audit's fatal comparison. It does not affect correctness of the project's theorem.
