# Research workspace

This directory contains non-rendered working material for the autonomous research group.

It is laboratory space, not part of the public wiki. Tentative claims, failed calculations, partial proofs, exploratory literature notes, computations, and student work belong here rather than under `docs/`.

The group model is one persistent ChatGPT Professor with persistent graduate students, all working on one active programme. The Professor owns scientific direction and the proof spine; students own technical attacks. See `CHATGPT.md`.

For each active programme:

1. create a branch `research/<short-programme-slug>`;
2. create `research/active/<short-programme-slug>/`;
3. maintain `state.md`, `proof-spine.md`, `literature.md`, and `audit-log.md`;
4. use `meetings/` for Professor synthesis and stagnation metadata;
5. use `students/` for substantial student calculations and reports;
6. keep long mathematics in durable files rather than compressing it into browser handoffs; and
7. treat the repository as canonical long-term memory, with sessions regularly re-grounding from the current files.

The templates under `research/templates/` are starting points, not fixed response forms. Mathematical prose and calculations may use whatever structure serves the problem.

`research/claim-registry.md` is different from the active-programme scratch space. It records project-specific mathematical claims promoted to `main` and their status. A manuscript on `main` is a draft artifact by default unless the registry says a claim is verified or principal-designated canonical.
