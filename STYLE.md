# Paper style

This file records the writing and LaTeX conventions for the paper under `paper/`.

## Mathematical typography

- Write inline mathematics with `$...$`, not `\(...\)`.
- When prose runs directly into inline mathematics, insert a nonbreaking space: `for~$t\geq0$`, `write~$A\Subset\Lambda$`, `the profile~$\mathbf p$`.
- Use `equation*`, `align*`, or another appropriate display environment for unnumbered mathematics. Do not use `\[...\]`.
- Use numbered environments only for formulas that are referenced later. A displayed formula should not receive a label merely because it is important.
- Use `align` only when the alignment is part of the presentation. Use `equation` for a single referenced formula.

## Terminology

- In the general discussion, a state is `calm` or `facilitating`.
- Use the established model-specific term when one exists: infected/healthy for the contact process, vacancy/occupied for KCSM, and particle/empty site for particle systems.
- `Activity` is not a technical state variable. It may be used in the introduction as an umbrella term for births, refreshes, flips, and similar updates, but not as a formal synonym for the facilitating state.
- `Active set`, `active source`, and `local active indicator` remain the formal terminology for the signed dual.
- Use `bulk patch`, never `closed patch`.
- Describe the comparison results as centered-moment or monomial-moment comparisons, not stochastic domination.

## Prose and paragraphs

- A paragraph should develop one coherent mathematical point and normally contain several sentences. Avoid a sequence of one- or two-sentence paragraphs separated only because a display intervenes.
- A display does not by itself end a paragraph. Continue the same paragraph after the display when the mathematical sentence continues.
- Begin a new paragraph for a genuine change of subject, a theorem statement, or a distinct proof step, not for visual spacing.
- Prefer direct mathematical statements to administrative transitions such as `we now explain`, `the central condition is`, or `the next theorem states`.
- Avoid unnecessary adverbs and adjectives. Do not introduce informal phrases as though they were defined technical terms.
- Keep notation economical. Do not name an object used only once unless the name makes a later calculation substantially clearer.
