# Student G 011a2: the exact compatibility locus is the product surface

The symbolic one-move gate from `011a-distinguished-zero-one-move.md` factors through

$$
a=b(1-c).
$$

This is not an accidental depth-two locus. It is exactly the parameter relation on which the zero-boundary invariant family becomes a consistent Bernoulli product family.

Put

$$
\rho=\frac{b}{1+b}.
$$

Under the normalized simple-IPS convention, a rate-one ring at a site with current spin `x` and right neighbour `y` resets the site to `1` with probability `r_{xy}`. On `r_{11}=0`, the actual flip rates are therefore

$$
0\to1:\quad a\ \text{if }y=0,\qquad b\ \text{if }y=1,
$$

and

$$
1\to0:\quad 1-c\ \text{if }y=0,\qquad 1\ \text{if }y=1.
$$

For a Bernoulli-`rho` product law, the one-site detailed-balance equations conditional on the right neighbour are

$$
(1-\rho)a=\rho(1-c)
\qquad (y=0),
$$

and

$$
(1-\rho)b=\rho
\qquad (y=1).
$$

The second identity holds by `rho=b/(1+b)`. The first is then equivalent to

$$
a=b(1-c).
$$

Hence on this locus every local update is reversible with respect to the same Bernoulli marginal, for either value of the right neighbour. With the fixed zero boundary, the product law

$$
\mathrm{Ber}(\rho)^{\otimes N}
$$

is invariant for every finite zero-boundary chain. Strict positive rates make that finite chain irreducible, so

$$
\boxed{
\pi_N=\mathrm{Ber}(\rho)^{\otimes N}
\quad\text{for every }N.
}
$$

Consequently

$$
\bar\pi_{N+1}=\pi_N
$$

holds at every depth on the product surface.

This includes the corrected reversible reference point used in Assignment 010,

$$
P_0=\left(\frac1{10000},\frac1{10},\frac{999}{1000}\right),
$$

for which `a=b(1-c)` exactly. By contrast, at the hard point

$$
P_h=\left(\frac1{10000},\frac1{100},\frac{9999}{10000}\right)
$$

one has `b(1-c)=1/1000000`, not `a=1/10000`, and the prefix compatibility defect is already nonzero at `N=1 -> 2`.

Therefore the literal East induction survives exactly in the situation where the surrogate invariant family has reverted to the product-consistent structure that makes the East argument work. Off that surface, the new nonproduct zero-boundary family does not carry the needed prefix consistency even at the first nontrivial depth.
