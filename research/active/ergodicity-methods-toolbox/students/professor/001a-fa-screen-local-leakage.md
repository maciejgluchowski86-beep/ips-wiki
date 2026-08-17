# FA-SCREEN-001a: exact local leakage of the naive marker and dimer

Date: 2026-08-17

## Result

The literal East-style distinguished vacancy fails the FA causal-measurability gate in one ring. An adjacent-zero dimer delays but does not remove the same local leak.

Use sites `0,1,2`, where site `0` is protected, site `1` is the proposed right boundary, and site `2` is on the screen/exterior side. A ring at site `1` with refresh coin `z` has output

$$
U(l,x,r;z)=
\begin{cases}
z,& l=0\text{ or }r=0,\\
x,& l=r=1,
\end{cases}
$$

where `l=eta_0`, `x=eta_1`, `r=eta_2`.

For fixed screen-side data

$$
x=0,\qquad r=1,\qquad z=1,
$$

one has

$$
U(0,0,1;1)=1,
\qquad
U(1,0,1;1)=0.
$$

Thus whether the proposed distinguished vacancy fills depends on the protected neighbour. Conditioning on its future path would reveal protected future information. This is exactly the failure absent in East.

The full one-ring classification is equally simple. For fixed `(x,r,z)`, the output depends on the protected neighbour iff

$$
r=1\quad\text{and}\quad z\ne x.
$$

These are the two contexts

$$
(x,r,z)=(0,1,1),\qquad(1,1,0).
$$

This gives an exact definition of a **dangerous boundary mark** for any attempted screen which refuses to inspect the protected side.

## Dimer gate

Now start with adjacent vacancies at boundary sites `1,2`, so the boundary state is `00`. A refresh-to-1 mark at the outer site `2` is legal because site `1` is vacant, independently of the protected spin and farther exterior. Hence the dimer can reach

$$
(\eta_1,\eta_2)=(0,1)
$$

without using any protected information.

In that state, the next refresh-to-1 mark at the inner vacancy `1` is precisely the dangerous one-ring context above: its legality depends on the protected site `0`. Therefore a dimer rule which continues through this event leaks. A faithful dimer rule may instead declare screen failure at that dangerous mark; that failure event is itself measurable from boundary/exterior marks because the rule can declare failure regardless of the actual protected-side legality.

Thus:

- single-marker exact regeneration is locally false;
- a dimer can produce a faithful **killed** screen primitive, but not a failure-free one;
- the next question is persistence/scaling of such killed finite boundary automata, not the spectral gap.

## Verifier

`001a-fa-screen-local-leakage-verifier.py` exhaustively checks the 8 local `(x,r,z)` contexts, the exact danger criterion, and the dimer transition into the vulnerable state.

## Scope

This is not yet `STOP-LOCAL-SCREEN`: the assignment permits a finite automaton to declare failure at dangerous marks and asks whether a dimer/corridor can propagate or hand off often enough to overcome that failure. The result only kills the literal East marker and failure-free two-site dimer.
