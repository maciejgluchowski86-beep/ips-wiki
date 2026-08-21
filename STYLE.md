# Paper style

This file records the writing and LaTeX conventions for the paper under `paper/`.

## Mathematical typography

- Write inline mathematics with `$...$`, not `\(...\)`.
- When prose runs directly into inline mathematics, insert a nonbreaking space: `for~$t\geq0$`, `write~$A\Subset\Lambda$`, `the profile~$\mb p$`.
- Use `equation*`, `align*`, `gather*`, or another appropriate display environment for unnumbered mathematics. Do not use `\[...\]`.
- Use numbered environments only for formulas that are referenced later. A displayed formula should not receive a label merely because it is important.
- Use `align` only when the alignment is part of the presentation. Use `equation` for a single referenced formula.
- Avoid isolated short displays when an expression reads naturally inline or can be combined with an adjacent display.
- Use the shared delimiter macros `\bb`, `\Cb`, `\cb`, `\abs`, and `\norm` instead of manual `\left...\right` or `\bigl...\bigr` constructions. Use `\mb` and `\mbs` for bold mathematical symbols.
- When describing evolution of an initial measure, write `$(\mu P_t)(f)$`, not `$\mu(P_tf)$`. Use the latter only inside an operator calculation where the action on the observable is the point.

## Terminology

- In the generic theory, call the two spin values `0` and `1`. Do not assign them universal physical names. In particular, do not use `calm` anywhere in the paper.
- Use `facilitating` only in model-specific contexts where it is standard or useful, especially for KCSMs. In the KCSM convention used here, `0` is vacant and facilitating and `1` is occupied.
- Use the established model-specific terms when they exist: infected/healthy for the contact process, vacant/occupied for KCSMs, and particle/empty site for particle systems. If a model is written in complemented variables, state the relabeling explicitly rather than imposing generic state names.
- For a Bernoulli product measure~$\mu_{\mb p}$, describe~$p_i$ as the probability, density, or mean of state~$1$ at site~$i$, according to context. Do not call it a calm-state density.
- A spin system has one flip-rate function~$c_i$. The functions~$c_i^0$ and~$c_i^1$ are its restrictions according to whether the current spin is~$0$ or~$1$; equivalently, they give the~$0\to1$ and~$1\to0$ rates. Do not call them two separate flip rates.
- `Pure deaths` means environment-independent~$1\to0$ transitions in the spin system; the name comes from the signed dual. Use this terminology once it has been defined rather than rephrasing the transitions through a generic facilitating-state interpretation.
- In conceptual exposition, use `monotone`, `configuration monotonicity`, or `monotone coupling`. Use the traditional term `attractive` only when discussing the historical IPS terminology or quoting/comparing with literature that uses it.
- `Activity` is not a technical state variable. It may be used in the introduction as an umbrella term for births, refreshes, flips, and similar updates, but not as a formal synonym for either spin value.
- `Active set` and `active source` are formal terminology for the signed dual. Write `dual-active` when the distinction from the spin states matters.
- A single successful interaction has a `record`; the family of records is the `successful-interaction skeleton`.
- Describe patch boundaries through incoming and outgoing successful interactions. Do not use `touch` as a technical term.
- Use `bulk patch`, never `closed patch`.
- Describe the comparison results as centered-moment or monomial-moment comparisons, not stochastic domination.
- Write `patch-positive` with a hyphen when it modifies a noun, as in `patch-positive spin system`.

## Prose and paragraphs

- Section and subsection titles should name their main focus. Avoid catalogue titles of the form `X and Y` unless the pairing is itself a standard concept.
- Avoid numbered subsubsections. Use short paragraph headings for local subdivisions that do not need to be separate destinations.
- A paragraph should develop one coherent mathematical point and normally contain several sentences. Avoid a sequence of one- or two-sentence paragraphs separated only because a display intervenes.
- A display does not by itself end a paragraph. Continue the same paragraph after the display when the mathematical sentence continues.
- Begin a new paragraph for a genuine change of subject, a theorem statement, or a distinct proof step, not for visual spacing.
- Prefer direct mathematical statements to administrative transitions such as `we now explain`, `the central condition is`, or `the next theorem states`.
- Avoid unnecessary adverbs and adjectives. Do not introduce informal phrases as though they were defined technical terms.
- Keep notation economical. Do not name an object used only once unless the name makes a later calculation substantially clearer.
