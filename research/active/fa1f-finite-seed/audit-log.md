# Audit log

## 2026-08-15 — programme initialization

Professor read the governing `CHATGPT.md`, `project-state.md`, and `README.md` at commit `a719652`, and the principal-designated canonical patch paper.

Direction selected: 1D hard FA-1f from a single vacancy, all `q in (0,1)`.

Closed-route check: the target and initial centered `h`-transform route were mathematically distinct from the closed 1D Bernoulli-quench sibling-cancellation route and from the closed 2D relaxation/capacity routes.

Initial Professor calculation: `notes/professor-initial-reduction.md`.

## 2026-08-15 — Meeting 001

Student A independently verified the exact centered `h`-transform dual, including nonexplosion and infinite-volume semigroup duality. Pointer: `students/student-a/001-centered-h-transform.md`.

The same note showed that on finite cycles the transform is an invertible similarity of the transpose FA-1f generator and that the obvious structural handles do not simplify the finite-seed theorem. The transform was retained as an exact identity but demoted as the active proof mechanism.

Meeting record: `meetings/001-h-transform-review.md`.

`state_narrowed: yes`.

## 2026-08-15 — Meeting 002 and closure

Student A derived the exact unnormalized successful-skeleton expansion, hard-FA patch amplitudes, first complete branching composition, and global centered coefficient transfer. Pointers:

- `students/student-a/002-unnormalized-patches.md`;
- `students/student-a/002-transfer-normalization-clarification.md`.

The Professor independently verified the load-bearing coefficient identification in `notes/professor-transfer-verification.md`:

$$
K_t(A,B)=q^{|A|-|B|}Q_t(A,B),
$$

with `Q_t` the E1 Markov semigroup. Hence the complete `h`-weighted coefficient transfer has row mass one.

The unnormalization-only mechanism is therefore closed: consistency probabilities create a real loss on restricted routing sectors but no loss in the full transfer. This is a different obstruction from the previously closed absolute sibling-cancellation route.

Meeting record: `meetings/002-unnormalized-patch-review.md`.

`state_narrowed: yes`.

Direction decision: `close` on expected-value grounds. The finite-seed FA-1f conjecture remains open; this closure makes no impossibility claim.
