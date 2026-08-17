# 002a: typed patch local state and noncemetery consistency

Date: 2026-08-17

This note executes Parts A--C of Assignment 002 up to, but not including, the mandatory finite gate. It fixes the local objects used in that gate and in any later Mecke argument.

## 1. Typed successful records

The typed signed dual from Assignment 001 has local branch clocks indexed by

\[
(i,r,s,\tau),
\qquad r\in E_*:=E\setminus\{0\},\quad s\in E,
\]

where `tau` is a typed partial map on `N(i)`. For nonempty `tau`, the branch clocks at fixed `(i,r,tau)` are superposed. Their combined rate is

\[
\Lambda_{i,r}(\tau)=\sum_{s\in E}|a_{i,r}^s(\tau)|,
\]

and, conditional on a coarse point, the hidden source outcome has law

\[
q_{i,r,\tau}(s)
=\frac{|a_{i,r}^s(\tau)|}{\Lambda_{i,r}(\tau)}.
\]

A coarse nonempty-target point is successful when the global typed dual is not in cemetery and its pre-interaction source type is `r`. Its record is

\[
(i,t,r,\tau).
\]

The record therefore reveals the pre-source type and typed target but hides the post-source outcome `s`.

## 2. One-site typed patch geometry

Fix a realized finite list of successful records, together with the deterministic typed initial record at time zero. Exactly as in the binary paper, every record creates

- one outgoing boundary on its source line `i`;
- one incoming boundary on each target line `j in supp tau`.

At an incoming boundary on `j`, retain the incoming type `tau(j)`. At an outgoing boundary retain the source type `r` and the typed target `tau`, since both determine the coarse-clock intensity and hidden-outcome law.

Consecutive boundary times on one site line define one-site vertical patches. For a patch `P` on site `i`, write

\[
X_u^P\in E,
\]

where `0` means dual-inactive and `a in E_*` means active with type `a`.

The finite boundary orientations are the same geometric four possibilities as in the binary paper: incoming/outgoing start crossed with incoming/outgoing terminal. End patches have terminal label `E`.

## 3. Reference patch law

The interior of a patch on site `i` contains the independent local Poisson clocks originating at `i` strictly between its endpoints.

The actual jump-clock family consists of

- every nonempty-target clock `(r,s,tau)`;
- empty-target clocks `(r,s,empty)` with `s != r`;

while the empty-target source-survival coefficient `(r,r,empty)` is diagonal and remains in the Feynman--Kac potential, exactly as in Assignment 001 and in the binary paper.

At an incoming initial boundary carrying type `a`, set

\[
X_s^P=a.
\]

At an outgoing initial boundary with record `(i,s,r,tau)`, sample the hidden source outcome `S_P` with law `q_{i,r,tau}` and set

\[
X_s^P=S_P.
\]

Read interior marks chronologically. A mark whose source-type label is `r'` acts on the local source state iff `X_{u-}^P=r'`; if it acts, the post-source state becomes its outcome `s'`. Marks whose source-type label does not match are ignored. This source-line reconstruction is defined even on reference histories later rejected by consistency.

## 4. Local consistency event

For a patch `P`, define `Con(P)` by the following conditions.

### Interior condition

Every interior nonempty-target mark `(r',s',tau')` must satisfy

\[
X_{u-}^P\ne r'.
\tag{4.1}
\]

Otherwise it would be an additional successful record omitted from the selected skeleton.

### Outgoing terminal

If the terminal record is outgoing from the patch site with revealed source type `r_e`, require

\[
X_{e-}^P=r_e.
\tag{4.2}
\]

### Incoming terminal

If the terminal record is incoming with target type `a_e`, require

\[
X_{e-}^P\in\{0,a_e\}.
\tag{4.3}
\]

The two allowed cases correspond respectively to activation of an inactive line and idempotent merge with the same active type. Any other active type conflicts with the incoming target and sends the global typed dual to cemetery.

### End terminal

There is no extra terminal condition. Condition (4.1) already says that there is no unrecorded successful nonempty-target clock before the horizon.

After a compatible incoming terminal carrying `a_e`, the next incoming-start patch begins deterministically at type `a_e`, whether the preceding state was `0` or already `a_e`.

## 5. Noncemetery local-consistency equivalence

Fix a finite candidate record list `g` and its induced patches. Couple the patch reference marks to the inserted selected record points in chronological order.

Then the following are equivalent:

1. the global typed dual remains outside cemetery through the horizon and its successful record list is exactly `g`;
2. every induced patch satisfies `Con(P)`.

### Proof

Assume all patch events hold. At time zero, incoming initial patches reproduce the typed initial configuration. Between selected record times, (4.1) excludes every nonempty-target mark whose source type matches the current local type, so there is no omitted successful record. Matching empty-target marks update only the source type, and the global and local source-line recursions agree.

At a selected outgoing record, (4.2) makes its revealed source type equal to the actual pre-source type, so the record is successful. Its hidden branch outcome initializes the next outgoing-start patch with exactly the global post-source type. At each target line, (4.3) makes the incoming typed merge compatible. The global process therefore does not enter cemetery, and the next incoming-start patch begins at the correct target type. Induction over selected record times gives exact agreement through the horizon.

Conversely, suppose the global process remains noncemetery and has record list exactly `g`. Any interior nonempty-target mark with matching source type would be an extra successful record, proving (4.1). Every selected outgoing record must have its revealed pre-source type, proving (4.2). Since cemetery is never hit, every selected incoming target must meet either an inactive line or the same active type, proving (4.3). The local source processes are restrictions of the global one, so all patch events hold.

This proves the equivalence.

## 6. Why full conditioning on the record list can still fail

The equivalence above deliberately includes the noncemetery condition. If a selected incoming target conflicts, that selected record is still present: success was decided at its source immediately before applying the branch. The conflict then sends the global dual to cemetery, after which no future coarse point can be successful.

Consequently, for a record list `g` whose last selected interaction may conflict, the bare event

\[
\{G_T=g\}
\]

can contain both

- cemetery histories, on which every future no-record condition is automatic; and
- noncemetery histories, on which all end patches must suppress matching nonempty-target clocks.

Thus the bare skeleton event is generally a union rather than a product of local patch events. This does not yet prove failure of full conditional-law factorization; the mandatory finite gate in 002b will test it exactly.

What is already exact is the weighted identity at the level of indicators:

\[
1_{\{\tau_\dagger>T\}}1_{\{G_T=g\}}
=
\prod_{P\in\mathcal P_T(g)}1_{\operatorname{Con}(P)}
\tag{6.1}
\]

on the inserted-record reference space, where `tau_dagger` is the cemetery hitting time. Equation (6.1) is the candidate repair allowed by Assignment 002. The finite gate must determine whether it really restores product structure under the reference law.
