# Staged method-entry template

Each finished method entry is one Markdown file under `entries/`, committed immediately when complete.

```markdown
---
method_id: <stable-slug>
title: <method name>
category: <coupling | graphical-duality | functional-inequality | spatial-mixing | lyapunov-regeneration | kcsm-model-specific | finite-to-infinite | other>
targets:
  - <ergodicity | uniqueness | convergence | coupling-agreement | spectral-gap | log-sobolev | mixing | extinction>
model_scope: <one-line scope>
source_status: primary-checked
primary_source: <full bibliographic citation>
primary_pinpoint: <Theorem/Proposition/Lemma/Section and page if useful>
primary_url: <stable DOI/arXiv/publisher URL>
application_source: <full citation or none>
application_pinpoint: <pinpoint or none>
application_url: <stable URL or none>
wiki_candidate: yes
---

# <Method name>

## Criterion

State a usable theorem/criterion with hypotheses and conclusion. Give the essential inequality, coupling condition, domination statement, or functional inequality explicitly when the method has one.

## Mechanism

Explain in a few paragraphs why the criterion yields the target conclusion. This should be enough for a reader to recognize when the method might apply, not a full historical survey.

## Representative IPS use

Give at least one spin-system/IPS/KCSM/Glauber-type application. For a model-specific method, explain the model feature it exploits.

## Limitations

State the main assumptions or failure modes: attractiveness, finite range, high temperature, reversibility, legal paths, boundary conditions, finite volume, etc.

## Sources

Give the primary source first, with the exact pinpoint used above. Add an origin source, survey, monograph, or second application only when useful.
```

## Writing rules

- Target 400–900 words; hard ceiling 1200 words excluding front matter and references.
- One method/concept per entry. Split genuinely different mechanisms even if one paper uses both.
- Be concise but theorem-level: do not replace the criterion by a slogan.
- Do not infer a stronger result than the cited source proves. Distinguish uniqueness, ergodicity, exponential convergence, spectral gap, and mixing time.
- Use the terminology of the cited source and note common aliases when that helps discovery.
- For a general Markov-chain theorem, a concrete IPS/spin application is required.
- `primary-checked` means the worker actually opened and read the primary source at the stated pinpoint.
- Repository research notes may suggest search terms but are not sources for a literature entry.
