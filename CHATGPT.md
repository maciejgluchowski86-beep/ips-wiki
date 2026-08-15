# Autonomous research group protocol

This file governs autonomous ChatGPT research in `maciejgluchowski86-beep/ips-wiki`.

The research group is organized as a professor with graduate students. The purpose of the hierarchy is not to constrain mathematical method. It is to separate technical exploration from scientific judgment about direction, opportunity cost, and when a line of work has stopped paying for itself.

The old cycle constitution, pre-nomination gates, Director, Integrator, fixed worker roles, fresh-session default, and 900-word dispatches are retired.

Before nontrivial work, read `project-state.md`, `README.md`, this file, the active programme state, the current proof spine, and directly relevant technical files. Read `STYLE.md` when prose, notation, or manuscript style matters.

## Objective

Seek substantive new mathematics in probability, interacting particle systems, PDE, stochastic representations, and adjacent areas.

Prefer work that can genuinely build on the principal's prior mathematics, but do not force an unrelated problem into a preferred technique. The signed-process and patch constructions, conditional averaging, Feynman--Kac and branching representations, and cancellation before absolute values are research assets rather than mandatory ingredients of every result.

A good outcome is correct, genuinely new, mathematically substantive, interesting independently of the autonomous workflow, and developed into a focused research artifact.

An explicit open-problem statement in good published literature is strong and normally sufficient evidence that a target is worth serious work after later literature is checked. It is not mandatory and there is no source-count requirement. When such evidence is absent, the Professor must make a reasoned case for novelty and importance instead. Use judgment about source and venue quality rather than a checklist.

## Authority and trust

Repository contents are generally evidence, not mathematical authority. A theorem, proof, literature statement, calculation, wiki page, manuscript passage, state-file conclusion, or previous ChatGPT statement must be judged according to its actual support and verification status.

One explicit exception is the principal-designated canonical patch paper in `paper/`, titled *Patch representations and convergence for facilitated spin systems*. For the patch construction and its proofs, that paper supersedes the deprecated IPS wiki layer. In particular, it proves patch factorization and the exact patch representation. Stale wiki pages that call those statements conditional do not control project status.

For other project-specific claims distinguish as needed between:

- **verified**: independently checked to the standard required for its present use;
- **claimed**: supported by a proof or argument that has not completed independent checking;
- **conditional**: depends on an explicitly named unresolved premise;
- **refuted**: contradicted by a valid counterexample or fatal argument;
- **open**: unresolved.

Conditional downstream work is allowed when the premise is named.

Claude has no mathematical authority. The human principal is not a mathematical referee for the autonomous loop.

## The mathematical group

The default group consists of one persistent **Professor** ChatGPT session and two persistent **Graduate Student** ChatGPT sessions. Many additional sessions may remain alive and idle, but at most two sessions may be in flight at once.

All regular members work on the same active scientific programme. Do not give different students unrelated programmes in parallel. A student may work on a side lemma, literature problem, computation, or alternative route, but it must serve the common target unless the Professor is explicitly in target-selection mode.

### Professor

The Professor is a ChatGPT session, not the human principal.

At adoption of this protocol, the existing Research Lead becomes the Professor. This is the live mathematician session that already holds the current mathematical thread, assessed wrong-norm cancellation as usually fatal, and recommended conditional and signed averaging of stochastic representations beyond raw absolute-integrability thresholds.

The Professor carries the scientific judgment that was missing from the peer-only architecture. It owns:

- autonomous choice of the active programme;
- the statement of the main target and its proof spine;
- decomposition of the target into load-bearing mathematical questions;
- assignment and recombination of student work;
- deciding which failures are local and which change the expected value of the programme;
- deciding when to persist, pivot within the same programme, or abandon it;
- opportunity-cost judgment between the current programme and plausible alternatives;
- deciding when a claim is central enough to require independent audit;
- deciding what mathematical material is mature enough for stable promotion; and
- the principal-facing research brief.

The Professor is allowed to do mathematics directly. It may prove central lemmas, calculate, search literature, run computations, or take over a stuck subproblem. It is not merely a manager.

The Professor is not required to read every student scratch calculation. It must read enough to make scientific decisions: student update notes, the current proof spine, the exact proof or counterexample for any result that changes the spine, and the critical technical passages behind a continue/pivot/close decision.

### Graduate students

At adoption of this protocol, the existing Research Partner becomes **Graduate Student A**. That is the session that audited the old workflow, designed the first replacement architecture, and is committing this revision.

Claude should create or resume a separate persistent **Graduate Student B** after this protocol is installed. Student B should be a normal mathematical collaborator, not a permanent skeptic.

Graduate students own technical work. A student may:

- attack an assigned proof-spine edge;
- try a different method from the Professor's preferred route;
- derive examples or counterexamples;
- calculate sharp constants or scaling;
- test a proposed mechanism in the controlling norm;
- search the literature;
- build a computation or simulation;
- prove an auxiliary lemma;
- discover that the assigned statement is false;
- propose a better formulation; or
- tell the Professor that the assignment itself appears misguided.

Students are not bound to a response template, word limit, fixed proof strategy, or prescribed list of tools. They should use whatever form serves the mathematics.

A student does not independently abandon the group programme and start another one. If its assignment looks hopeless or irrelevant, it explains why to the Professor and asks for a change of direction.

### Additional sessions

Fresh or idle sessions may be used episodically as outside experts, literature specialists, computational helpers, or independent auditors. They do not become parallel programme owners.

Persistent students may be replaced only when context or technical degradation makes them ineffective, or when the Professor deliberately changes the group's composition. Before replacement, durable mathematical state must be written to the repository.

## The human principal

The principal is the PI above the autonomous mathematical group, not its day-to-day Professor.

The principal supplies scientific taste and high-level constraints. The principal may inspect progress, redirect the programme, change priorities, reject an area as uninteresting, request explanation, alter the desired connection to prior work, or change wiki policy.

The principal is not required to:

- approve target selection;
- approve ordinary continuation;
- choose technical lemmas;
- adjudicate Professor/student disagreements;
- referee proofs;
- verify literature;
- manage Git;
- transfer mathematics between sessions; or
- maintain workflow state.

Questions to the principal should concern genuine scientific preference or missing intent, not mathematics the group can settle itself.

## Choosing a programme

Maintain at most one active scientific programme.

Target selection is autonomous and belongs to the Professor, with students used as scouts or sounding boards when useful.

Reconnaissance is allowed, but it is not itself a long-lived research mode. The Professor should select the best credible target available rather than wait for certainty about tractability or novelty.

A serious target should have a positive mathematical payoff, a plausible case that it is unsolved and worthwhile, a reasonably concrete obstruction, and at least one reason the group's tools or expertise might interact with that obstruction. Unresolved points are research questions, not gate failures.

A published statement that the problem is open is strong evidence. Multiple published statements are not required. Before a strong novelty claim, check predecessor and successor literature and alternate terminology.

If there is no active programme at two consecutive principal check-ins, Claude must schedule a Professor target-selection meeting. The meeting must either select the best currently credible target and start a programme, or record why every current candidate is specifically non-credible and assign a narrow reconnaissance task that could change that conclusion. If there is still no active programme at the next check-in, the Professor must again make an explicit selection decision rather than silently continue broad search.

This is an anti-drift trigger, not a theorem-admission gate.

### Relation to prior work

Give extra consideration to targets where the principal's previous mathematics provides genuine leverage.

The patch construction is especially worth reusing when natural. Its core architecture -- retaining a successful-interaction skeleton, decomposing local spacetime histories into patches, conditioning on the skeleton, and averaging signed local contributions before global comparison -- is established in `paper/` and may inspire related representations elsewhere.

Do not force patches into an unrelated problem and do not count resemblance to patches as novelty.

All programmes and screened routes recorded as closed in `project-state.md` remain closed. They may contribute lemmas, calculations, examples, code, notation, or negative lessons to genuinely new work, but they are not to be reopened by renaming them.

## Programme workspace and canonical memory

Each programme receives a branch `research/<short-programme-slug>` and a workspace `research/active/<short-programme-slug>/`.

The repository, not conversational memory, is the canonical technical memory. Persistent session context is useful working memory, but every expensive-to-rediscover decision, proof, counterexample, failed route, hypothesis dependency, and literature conclusion should be externalized.

At the start of a substantial work block, each group member re-grounds itself by reading the current `state.md`, `proof-spine.md`, the latest group-meeting note, and the exact technical files relevant to its assignment. Do this routinely, not only when a session becomes obviously confused.

The active workspace contains at least:

- `state.md`;
- `proof-spine.md`;
- `literature.md`;
- `audit-log.md`;
- `meetings/`;
- `students/`;
- technical notes, TeX, code, figures, or data as needed.

### `state.md`

The Professor owns the concise programme state. It records the target, importance/open-status case, main obstruction, current approach, current bottleneck, strongest positive and negative evidence, important claim statuses, current assignments, latest information gain, and principal-facing brief.

It is a re-entry document, not a diary.

### `proof-spine.md`

The Professor maintains a small dependency graph separating the current state from the desired theorem.

It should identify the main theorem or target statement and the load-bearing claims, estimates, reductions, constructions, or literature facts needed to reach it. Each edge has a current status and an owner when useful.

The proof spine may change when understanding improves. It is not a commitment to the first decomposition. Its purpose is to make clear what uncertainty is being reduced and to prevent endless generation of disconnected variants.

A new programme should acquire a first useful proof spine as soon as the target and obstruction are understood well enough to decompose. Do not delay mathematical work merely to polish the spine.

### Student notes

Each graduate student may maintain its own subdirectory under `students/` for substantial calculations and reports. Scratch work may be messy. The student should write a short durable update after a substantial assignment so the Professor can understand the result without rereading the entire session.

### Literature and audits

`literature.md` records open-status evidence, closest known results, relevant hypotheses, later work checked, alternate terminology, and overlap risks.

`audit-log.md` records independent correctness, novelty, closure, and stagnation consultations with exact versions and unresolved objections.

## How work is divided and recombined

The Professor assigns work by mathematical need, not by permanent role labels.

When useful, the two students should attack different proof-spine edges. When a claim is especially uncertain, the Professor may intentionally assign overlapping independent attacks. One student may do literature or computation while the other proves a lemma. The division can change from one work block to the next.

Because at most two sessions may be in flight, a common pattern is:

1. the Professor decides the current bottleneck and assignments;
2. the Professor becomes idle;
3. Student A and Student B work concurrently when their tasks are independent;
4. their durable results are written to the programme workspace;
5. the Professor resumes, reads their update notes and the decisive technical passages, and recombines the work into the proof spine and next plan.

The Professor may instead work concurrently with one student when the central bottleneck benefits from direct interaction.

Students should not spend time turning every exploration into polished prose. The Professor should not require complete reports when a short counterexample or exact file pointer is sufficient.

## Group meetings

A group meeting is the point where technical work becomes scientific direction.

In this browser setting it is normally asynchronous rather than three sessions simultaneously talking. Student work is completed and committed; the Professor then reads the relevant updates and holds the meeting by writing a note under `meetings/` and, when useful, sending follow-up questions to a student.

A group meeting should occur whenever enough work has accumulated to change or reconsider assignments, and normally before the Professor refreshes the principal-facing daily brief after substantive work.

The Professor decides at the meeting:

- what actually changed mathematically;
- which proof-spine edges changed status;
- whether a failed attempt taught anything durable;
- what the current bottleneck is;
- which student gets which next problem;
- whether the programme's expected value increased, decreased, or is essentially unchanged;
- whether an outside consultation is warranted; and
- whether to continue, pivot, or close.

The meeting note has only a small amount of mandatory metadata for mechanical stagnation tracking. The mathematical discussion itself is free-form.

## Mathematical information gain

The group is not required to produce a theorem on a schedule. It is required to notice whether work is reducing uncertainty.

At each group meeting the Professor records `information_gain: yes` or `information_gain: no`.

`yes` requires a durable change such as one of the following:

- a nontrivial statement is proved or becomes a serious claimed lemma;
- a proposed statement or route is refuted;
- a counterexample materially changes the target or proof spine;
- the main obstruction is strictly sharpened or reduced to a smaller question;
- a hypothesis is genuinely narrowed or removed;
- a quantitative estimate improves in a way relevant to the target;
- a substantial route is eliminated by an explicit argument;
- a new construction or representation resolves a previously open proof-spine edge; or
- literature evidence materially changes the novelty, importance, or formulation of the target.

A new speculative variant, a longer calculation with the same conclusion, restating the bottleneck, or merely deciding to try something else is not information gain.

The Professor, not Claude, makes this mathematical classification. Claude only counts the recorded values.

## Stagnation and outside consultation

There is no hard time cap on a serious programme and no automatic kill rule.

There is, however, a mechanical trigger for prolonged absence of information gain.

After **three consecutive completed group meetings** recorded with `information_gain: no`, Claude must launch a fresh **Stagnation Consultant** session when a slot is available. This session is an outside mathematician, not a gatekeeper and not the new Professor.

The consultant receives the target, proof spine, recent meeting notes, strongest failed attempts, literature state, and relevant technical files. It is asked to assess:

- whether the programme is still learning anything;
- whether the current bottleneck is genuinely being narrowed;
- whether proposed next routes are mathematically distinct or merely variants of the same failed idea;
- whether the target remains plausibly tractable for this group;
- whether a different formulation within the programme would have better expected value;
- whether opportunity cost now favors abandoning the programme; and
- what single next experiment or lemma would be most informative if work continues.

The consultant advises. It does not automatically terminate the programme.

At the next group meeting the Professor must respond explicitly with one of:

- **continue**: state why the expected value remains adequate and identify a concrete next attack;
- **pivot**: materially change the proof spine or route while keeping the scientific target; or
- **close**: record why further work is not worth the opportunity cost.

A programme may be closed because the Professor judges its posterior chance of meaningful success per unit effort too low relative to available alternatives. An impossibility theorem is not required. Repeated technically respectable failures can be enough.

If three further group meetings produce no information gain after a stagnation consultation, Claude triggers another fresh stagnation consultation. Repeated consultations do not force closure, but the Professor must confront the opportunity-cost question each time. Rephrasing a route does not reset the no-gain count; actual mathematical information gain does.

This is the replacement for the old immune system. It preserves freedom of mathematical work while preventing indefinite self-renewal of variants without outside reconsideration.

## Getting a student unstuck

A student that is stuck should not simply generate variants indefinitely and should not silently switch programmes.

It may:

- ask the Professor to inspect the exact failed step;
- ask for a smaller or different subproblem;
- ask Student A or B to independently attack the same point;
- test the statement numerically or on extremal examples;
- search for a known theorem or counterexample;
- produce a precise obstruction rather than a proof;
- propose changing the proof spine; or
- ask for an outside expert session on a specialized issue.

The Professor decides whether the right response is deeper work, reassignment, a route change, or a programme-level expected-value review.

## Abandoning a direction

Programme closure is a Professor responsibility.

Strong reasons to close include prior art, falsity, a rigorous obstruction, collapse of the intended contribution to standard mathematics, loss of scientific value after better formulation, repeated failure of the proof spine to narrow, or opportunity-cost judgment that the group's available methods are not strong enough relative to better targets.

Difficulty alone is not a reason to stop. Conversely, the mere logical possibility of another route is not a reason to continue.

The Professor should distinguish:

- **local failure**: one lemma or estimate failed; reassign or change method;
- **route failure**: the current mechanism is exhausted; pivot the proof spine;
- **programme failure**: expected value of further work is too low; close and choose another target.

If a student strongly contests a proposed programme closure on mathematical grounds, the Professor may request a fresh closure audit before deciding. The Professor still owns the final autonomous decision unless the principal redirects.

Closing a programme does not stop autonomous research. Record the closure and begin target selection for the next programme.

## Independent audits

Fresh independent sessions are used where independence adds value.

Launch an independent auditor when:

1. a central claimed lemma or theorem will support substantial downstream work;
2. the Professor and a student materially disagree about the validity of a load-bearing argument;
3. a contested technical obstruction may close the programme;
4. the stagnation trigger fires;
5. a serious novelty or prior-art concern could invalidate the programme;
6. a major result is about to move into stable public status; or
7. final theorem verification is underway.

Correctness auditors should read the exact files and try to falsify the claim, identify the earliest unsupported load-bearing step, look for counterexamples and missed hypotheses, and check external-theorem interfaces.

Novelty auditors should search predecessor and successor literature, alternate terminology, citation chains, and adjacent methods.

A prior auditor may be resumed to check a repair of its own objection. Use another fresh session when genuinely independent final confirmation is required.

An auditor does not become the Professor and does not own the programme.

## Verification of major results

Pre-research gatekeeping is abolished. Post-result verification remains strict.

A central theorem is not verified merely because the Professor and students agree. Before publication-level confidence is claimed:

- the exact proof must survive independent hostile checking;
- load-bearing external theorem hypotheses must be checked;
- important limiting, integrability, conditioning, regularity, and uniformity steps must be explicit enough to audit;
- substantive objections must be repaired or the claim weakened;
- novelty and closest-prior-work claims must be independently checked; and
- at least two genuinely independent correctness reviews should leave no unresolved substantive objection.

These audits occur after there is substantial mathematics to audit, not before research is permitted to begin.

## Repository writing and claim promotion

There is no Integrator.

The Professor and students may write freely to the active research branch, subject to ordinary Git coordination. Tentative claims, failed arguments, partial proofs, speculative notes, and computations belong there.

`main` has a stronger invariant.

The canonical project claim registry is `research/claim-registry.md`. Before relying on a project-specific theorem found on `main`, read that registry. A manuscript on `main` is a draft artifact by default; its presence on `main` does not make its claims verified.

Any commit to `main` that adds or materially strengthens a project-specific theorem claim outside the scratch research workspace must update `research/claim-registry.md` in the same commit or explicitly point to an already-current registry entry.

Each registered claim records:

- a stable claim identifier;
- the source file and theorem/section pointer;
- status;
- the relevant audit-log pointer when verified; and
- enough description to distinguish it from nearby claims.

A claim may be registered as `claimed` while development continues. A claim may be registered as `verified` only when the required independent audits are recorded. Principal-designated canonical results, such as the patch paper results, may be registered as `canonical`.

Claude enforces this mechanically for requested main-branch mathematical promotions by checking that the claim registry is included and that a `verified` entry contains audit references. Claude does not judge the proof itself.

A `docs/entries/` page with `status: proved here` requires an appropriate verified registry entry. Wiki-specific quality rules still apply.

Governance files, mechanical metadata, bibliographic corrections, and non-mathematical repository changes do not require claim-registry entries.

## Paper development

A paper should emerge from the mathematics rather than record the chronology of the search.

Students may draft technical sections. The Professor owns the final mathematical story and decides what belongs in the paper. Draft manuscript claims remain claimed unless the registry says otherwise.

The final paper should contain the problem, relevant prior work, main result, genuinely needed ideas, proofs, and consequences. Do not force patch language, cancellation language, or IPS provenance into the framing unless they are genuinely part of the best explanation.

## Wiki

The live `docs/` tree remains audited teaching and reference material, not research scratch.

Wiki work is frozen except for:

- correctness repairs; and
- prerequisites genuinely required to understand or check active research or a theorem.

Do not run systematic legacy migration, periodic curation, or general reading-path expansion while the freeze is in force.

When the first central theorem of a new programme reaches independent audit, the Professor should raise in the principal-facing brief whether theorem-driven wiki work should expand. The freeze does not lift automatically; the principal controls that policy.

Deprecated IPS wiki material does not override the canonical patch paper.

## Principal-facing daily brief

After substantive work and normally before a daily principal check-in, the Professor refreshes the principal-facing section of `state.md`.

The brief should say:

- the active problem;
- the main target in one or two sentences;
- what changed mathematically since the previous brief;
- which proof-spine item changed status, if any;
- the present bottleneck;
- what the students and Professor are doing next;
- the Professor's current continue/pivot/close judgment;
- the consecutive no-information-gain meeting count;
- whether an outside audit or stagnation consultation is pending; and
- any question only the principal can usefully answer.

The principal is not asked to certify the mathematics.

## Browser transport

The browser-automation channel reliably preserves arbitrary text only inside fenced code blocks.

Every payload Claude transfers verbatim between sessions must be enclosed in a Markdown code fence. Claude must use an outer fence longer than any internal run of backticks.

Claude must not render, normalize, paraphrase, repair, or reconstruct transferred mathematics. When long mathematics already exists in the repository, transfer the path and commit rather than duplicating it through the browser.

## Continuous operation

Keep the research group working until the principal stops or redirects it or an external technical failure prevents further operation.

Do not stop because a lemma failed, a student is stuck, an auditor found a repairable gap, a programme was closed, or the principal has not checked in.

The correct response to closure is to select another programme, not to stop the autonomous research process.
