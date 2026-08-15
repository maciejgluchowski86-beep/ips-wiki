#!/usr/bin/env python3
"""Exact verifier for a finite-window BABP right-edge corrector.

This file certifies positive drift at lambda = 1/40 with window k = 10.
The 1024 corrector values were obtained by a floating-point linear-program
search and rounded to denominator 10^6. Verification below uses only exact
fractions, so the certificate itself does not depend on a numerical solver.
"""

from __future__ import annotations

import base64
import itertools
import struct
import zlib
from fractions import Fraction

K = 10
LAMBDA = Fraction(1, 40)
DENOMINATOR = 1_000_000
CERTIFICATE_B85 = """c-keDcYIY<)`mj|BSs+<9ohs(AQYuaO#q1?y@igLgx(~8K%~YGDWQYNfQX2Mjvyk6j1eLrO>pRlFo2>+)M1}<?mg$8dvBh3{e6Etzjy7m*6wTXn3$NDykFqc{qRaYoahDb^@iJXp?elMM+<3vtdR3p3MqB2kW;1LZ>1HFg%YxFMx%5Wm5Ud0C#I05357JSp}g{i)UQxT=b?o(6HUh!@>@nB)y5Q3cXT1WMinw=L?Jt4qf9RmrFu-1Uy4MTS29X%F}GNhZpEWyBu2@p6XkC0C}pL|Pe(aWIZEJfQQj8Ev!jfg6Xox7qkJe`w^HpDQ7SEp(r|H<wo9UfrQXsg6J=k|iSkhGouZ8x84Q#DAWYkfVdmZlbLPu1WsijEaWYKCi7<T*hDi|L9||-7voO0p4|71=SKhh9Vfx++Gv#)eEjPog{84?R4aF3(R3x9%*k`1omWaC$=FRhAW{XZ@&a4RICr8L19wB*5gbqU@bQJSmi?Bd67#m@${OhF^#FUH(jm40W5jKyA@Y2Kx(a{lxs{apar^#PLq|5$79GCxEdW5^;3lR|A#Y2%R4u9t}@pGSo<v!1D^!d22PjafyQ<**=P4LN#_gNyGYCh4YeQ4~{tclN{=05YA`po!mh;TuOYvR86+73}qc=FGA6yk6ZpZFN{E$;JPQJ+ese5RE2$rJxB;d8&fPhw4<>wnFo@pqT;IU^F|d`gKekNI>}yQ}nqw5l{mni=bJL-w1>$t>-Ys(JPl^ZAYt>%@A^c|lmpt*JRHia#{xNU>V;zAtSl(g%fU-ziLqI$>Hh4l_6=%yH2?UUyY4Ov){vHsZ6Nd^X<kS^KAKF~ss2{mAFVyFN1&FSzM5=|`Ur{^OG*F3Xp2+oy}{sj`2Nex&wG8fV)*?On7JCrgJ(i}*bL(B}z_*Y3K{1QFF-BShvUpUoG20+)R*%D#BTCtD;ar~WmcRhqx7<{qN>@~b}6l-ov(Rqk?8MZQm^r4>IY-6SoL-j_}jyWbDdVQz@QDIwYq2od|xBPga<4Drd6A+}8PxFcp{du*QJ5x3i8g6Ol~<6qJZKf6r6>vCC|^pndd-=%oSrSc<}w#KDaZI9#6d9-NgQKz0q6=~uN9_7WP1|GYzT)vv%a%-5&q~R_@2f1X5XNS5h6sHx7AMY|lB#HUTIhx^eX{1X7abT}Y(`}mbLzmnwE?alF#0Yn*@^W2f?$)?!-`lAiu}1dP?Jnh{>!j(sT&}<4^2TJBFJ`;^+R5eBS6uyBE^P+8G^yi~Ut4oGaM@H>`)uxVO=Pxq+1=9RR5O>7FSz`k=<<F&mjR-j*sa`B_5MFLTY5-L5E*KxKku?pv=ecw<<EA>9^*1N)1`B7mla~4=6^KArCV2*MqONDySwa^-M5E}k)5QRxL#W0IF~zVE;R<Y^wE0VzS_6Q>F07x*!^7wsZAf30`W?!OLw)WNQ;Q=2|g|KenMA6#Qhqg<I)hNmxajPAL6M!A@Uo9_*0~{2{Er(hz&#Z&c)cY5Qm0_h+Oknds+8-)nmjJ)x^)b@1H!5-tt&?+hbu-{RJ^0)|OVk;(C{5LVPFtSFxp3h-UffbI4=-4v(69JuZCU@laIQ>d{mj-s#amv0ud^;mX%poZhB-5}D^b%AN2yljm{isK?%89_>Xh+24y6r##v!{!ok+&T)^>H;PHq#o&4&CaTsGj7Pty>iKJrzpLL#?W?Nxb83ZrV$nK}yfq$OwtI{gNveHY>#6dV$AeiOUEkFDXKKH5^+rUg*&cJmH;X)KEbure9lX#ZcZt@X<Kc<^BIS%n{Uh3AuE)qdLUZMc3L88IuJ`cO=Xdo#x7cHp#@Mg^UH@XaN9|=Ek91bYw6?d^r^RaJ$+t-CRs1(GO1>_NZ4)VC_DYZS(jC$|qMF|JxtBdIMqECs=<)8`E;knIEqv|L<A_Vbk3rtL738QJBvKG0UNxK3&}FXbzH}p(69l*w36NYYNT-+}w`&HOmk^{|e2@+mgG?9~q^?MLGf2ZJK`KuVQeGrX3$k)*kh39&GX)MSZaG}K=aBW6ihbg@+YSSZ2goTJAVxedP8)}wqE*1*isSH9R)AfT0-PTop!viAEoW&xGXs1xH9*F+0Bsa+E&Xstfbr7<6qnumjR4Pyh;km>uqnv1sl3jnd#=r@aW<PK*gTqNvsQHOYx9h#Fwo{?Kbv2MNnf+sK3usOHZvF4%$seqVVX_TESp}^u_9BHm~N9YQTbyu$7q{Y((<p{jFPXYs3>k`IE?S%u%L;<i%AYYS96H3;qY!9hcbx{-aj0Ef7YRFEr;0W9R8W$a9(VbeP6MGFFNe6>##w6_9^d%`d6*)kSCVPS4+9~syf`N;?PK%D=LV?;&ajLu*LdS7K3_Pj2mUqK4>6h=#pR&t!~k6r6D8|KQ!E0Z|Ik=*l|OR(}rFr4eL7?DzrAd+QP7;rJ?%EhG2@JVq3$sc7`2e3}r_eT8uaJmz^`gkR)!a-9ZeSZm64P*seaCdKmh?ps^Yn?rE%ktqc>J7&@vwsFC46(y`KiOXtZSX>6GMs-czorE0#*8l#rhvPSeyGPF)Mq<1yc*P51SozEy<L|XhML%cLr>`t~BS<NQqq0S*<k-gm_W0%Dfr!4YLTD(5SVxLHuYLWK3MP#AH@WmE~msy-$VzGCK#l=1rH@jP0&>7z8Yw?39)!QOQ{&VRTpS)_3oMut%HH*M-i#ejQxRIfGHe0OFm`{zgs5IGPaf(G;M~j?Pi{&EF!lF@g&DF}HW=o4b$+AWDmn@pM*PRX1dU|QiYUgya=$T~kmH4Tx#kO`9L*=WeSgLXtifq}}rKhEPM5QFXopJ&Fj}8OwIxOz#P&w7%>|(vG1r8~n*bF<MIz40a<<~YNu*omtaIU1o{}pw(U@R!Gc=^8;-~M4SB-ZBn$85?JS`=W>v4{G1vuQiXCPDA0>;Rji{cRo-@1@$*X{a-+YO%Gn#jYnU%Enk66r+n<tSKR%VmqI)*daEFoH(856BfDUEXs+D<rcqX>uj?urp>ZQe9NM!xH?;VpKGyXzQtS8vGa6C(z|mk@)fHs^`!m3G#ve>A#Ic)GfQ>V!0@!{YglK)#a9f4#SC#G@iD`Nl7`2hRvn5{RSoT{s2*#mj^YhV74Q6n>M_=kC7u^WA2+Nkr#{j@6(1nq=_d`#;`D|@Z_(N^Jh-OXJ!m+4%rN5}&G)Wh_*TQ`;=wY*oh62zD^#nplUM0Ih)Qb><(0efW5c(b3<-)?l<(4F!wWfvcb95E%I~q-5F<NPzDHt!?A{u$k2FcVHs5Bx?xtP5&4T(i@9eYq_*08xcPz@>R=qT~sNY02sG7`HU5%Y&F+p|OXu9ftipBRw^u|6lR6U?`6ff&<_~aYIm-6@gN^|Hx*`+=H?i-4^23I;?lomDg&vek=a!BWXTkkkH+K{66n%qtAHC5-?&#+;D-g#d`p4!93XT1$qdg=Yjo+bYSozY_Ld-p;^3GFvkx?CI*Hx?P*(Eh{PuhHH+Nta1`>Wtb;>xr~Q7CrP9hu71a)|=^n-!S@t_M>{dTGFEYX5HBbhCRD<*13iT`v1mhf2+UMU7gT+G{%v+`ZH%3@@E<b%5E;QW~nA->n^pnRl1vHy0c~4Yl_+fb#Jla)EYw|qIKLe)XdX(XAKSCGo0V3z3wqA6!VwsPt`p=(ipX5UsS(*(M~nne4Xm^uxdeT%if?lwbsEJ|A?rdxDngs>!esC{oTvNAF>}xgVIale>*0ecK"""


def load_corrector():
    raw = zlib.decompress(base64.b85decode(CERTIFICATE_B85.encode("ascii")))
    numerators = struct.unpack("<1024i", raw)
    return [Fraction(n, DENOMINATOR) for n in numerators]


def drift(phi, u, z):
    """Exact generator drift of R + phi(edge word).

    u[j] = 1_{R-j-1 is occupied}, j=0,...,K-1, and z is the next
    unresolved exterior bit 1_{R-K-1 is occupied}.
    """
    states = list(itertools.product((0, 1), repeat=K))
    index = {state: i for i, state in enumerate(states)}
    i = index[u]

    value = LAMBDA - u[0]

    # Birth from the rightmost particle to R+1.
    t_plus = (1,) + u[:-1]
    value += LAMBDA * (phi[index[t_plus]] - phi[i])

    # If R-1 is occupied, it annihilates the rightmost particle at rate 1.
    if u[0]:
        t_minus = u[1:] + (z,)
        value += phi[index[t_minus]] - phi[i]

    # Flips of the k sites immediately behind the right edge.
    for j in range(K):
        left_neighbor = 1 if j == 0 else u[j - 1]
        right_neighbor = z if j == K - 1 else u[j + 1]
        occupied_neighbors = left_neighbor + right_neighbor
        rate = occupied_neighbors * (LAMBDA if u[j] == 0 else 1)
        if rate:
            flipped = list(u)
            flipped[j] = 1 - flipped[j]
            flipped = tuple(flipped)
            value += rate * (phi[index[flipped]] - phi[i])

    return value


def verify():
    phi = load_corrector()
    states = list(itertools.product((0, 1), repeat=K))
    minimum = None
    argmin = None

    for u in states:
        for z in (0, 1):
            value = drift(phi, u, z)
            if minimum is None or value < minimum:
                minimum = value
                argmin = (u, z)

    assert minimum == Fraction(1033, 40_000_000), (minimum, argmin)
    assert minimum > 0
    print("k =", K)
    print("lambda =", LAMBDA)
    print("minimum drift =", minimum, "=", float(minimum))
    print("argmin =", argmin)


if __name__ == "__main__":
    verify()
