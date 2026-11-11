# Practising the full talk

Select `patches_talk_rehearsal.tex` as the main document in Overleaf and compile with pdfLaTeX. Each PDF page pairs a slide on the left with its complete spoken script on the right. It contains all 23 main slides with complete spoken scripts, revised from the recordings. The three backup slides are excluded from this practice version.

The one or two key sentences in each slide's script are coloured dark red. Learn those lines first, then use the surrounding black text to practise filling in the explanation. The wording and pacing are unchanged. In the script `.tex` files, `\keyscript{...}` marks the sentences to memorize.

## Editing the spoken script in Overleaf

Open the corresponding `.tex` file in the file list, then search for the slide number, title, or script command. The complete sentences to practise are in these files:

| Slides | Spoken script file |
| --- | --- |
| 1–4 | `patches_talk_opening_script.tex` |
| 5–9 | `patches_talk_results_script.tex` |
| 10–12 | `patches_talk_duality_script.tex` |
| 13–17 | `patches_talk_patches_script.tex` |
| 18–23 | `patches_talk_proof_script.tex` |

The matching `.txt` files are exports. `patches_talk_rehearsal.tex` selects the slides and places their scripts on the right; edit the sentences in the files above.

For the presentation, select `patches_talk_draft.tex`. Both versions read the same slide source, `patches_talk_opening_script.tex`, `patches_talk_results_script.tex`, `patches_talk_duality_script.tex`, `patches_talk_patches_script.tex`, and `patches_talk_proof_script.tex`. Plain-text copies use the same names with `.txt`.

The introduction is paced for about four minutes, and the results for another four minutes. General notation begins the results on slide 5. The standard-duality section is paced for three minutes. The patch-representation section is paced for four minutes. The full deck has 23 main slides and three backups, with a planned duration of 20 minutes; this is an estimate to check by rehearsal. Patch positivity and the final convergence argument take the last five minutes. The closing states how the convergence theorem gives ergodicity in the high-vacancy regime or on an orientable graph, without proving those extensions.

In the general theorem and its proof, epsilon is the rate of the independent pure deaths. In the noisy FA-1f/East application, epsilon is the refresh strength; q < 1 ensures that the noise contains a positive pure-death component. No additional symbol is assigned to that rate. The application assumes p <= q < 1 and states ergodicity of the noisy system in the high-vacancy regime or on an orientable neighbourhood graph.

## Source checks for the introduction

The convention is p = occupation density, so vacancy density is 1-p. The independent noise refreshes set a spin to 1 with probability q. The partial result on slide 3 is Blondel, Cancrini, Martinelli, Roberto and Toninelli (2013), Theorem 2.1 and Remark 2.3: 1-p > 1/2, with any Bernoulli initial occupation density u in [0,1). It does not assert convergence from every initial configuration in that whole range.

Published paper: https://math.univ-lyon1.fr/~blondel/Papiers/fa1fversionfinale.pdf

For the general open conjecture and the role of non-monotonicity, see Martinelli, *Kinetically Constrained Spin Models: A Short Survey*, section 2.2.1, Conjecture 2.11 (ICM 2026): https://doi.org/10.1137/25M180425X

## Duality notation

The talk suppresses finite-volume and zero-boundary superscripts, as requested. In the manuscript, the signed Feynman-Kac identity is first justified in finite volume and the infinite-volume passage uses localization and patch positivity. The final estimates compare two initial laws directly and use the number of end patches |E_t|. That random count remains inside the averaged error bound. No auxiliary finite-region or limit constants are introduced. This shorthand does not assert absolute integrability of an unrestricted signed infinite-volume weight.

The obstruction slide states positivity of the noisy FA-1f potential only when epsilon(1-q) < 2p. Growth of the exponential weight is described qualitatively; no universal quadratic-in-time growth rate is asserted. The dual figure uses the paper geometry and labels the trajectory {3,4} → {3} → {2,4} → {1,2,3,4}, with both new targets shown at the split and birth.

## Patch-representation slides

The recording is implemented through the representation, stopping before the patch-positivity interpretation. The conditioning motivation first considers the signed exponential weight; its unconditional mean is P_t chi_A(1), and terminal spin dependence is handled by the end factors in the representation. The conditional-law display expresses factorization over patches, with an explicit one-site law for each patch. It introduces no patch-variable symbol or consistency event.

The overview shows all four bulk types using the paper's original activity-prism and interaction geometry, arranged in four panels. Headers spell out incoming and outgoing; no extra legend is required. The geometry figure and the previously approved representation are otherwise unchanged.

The second patches recording revises slides 12 and 14–17. Slide 13 is unchanged. The patch-type overview is a brief illustration, planned for about ten seconds; its incoming/outgoing labels are retained. The remaining time in the four-minute patches section is allocated to conditional independence and the representation. The weight W_t^mu is introduced by its definition before it is used in the semigroup identity.

## Proof ending

The final scripts are in `patches_talk_proof_script.tex`. The event L_t means no interaction in (t/2,t]; there is no separate time parameter T. The late-interaction estimate compares with the system obtained by removing the independent 1-to-0 transitions. The no-late-interaction estimate includes the probability of that event and keeps the end-patch count |E_t| inside the expectation with the primed weights. Polynomial graph growth controls the accumulated error. The common invariant law belongs to M_star because the semigroup preserves this class. The final slide states the two ergodicity extensions and displays the precise centered-moment burn-in bound for an orientable graph. Lists use explicit flat bullet markers; the three backups are retained.
