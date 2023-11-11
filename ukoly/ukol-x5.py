
#Mějme zadaný následující seznam naměřených teplot. 
#Seznam obsahuje teploty naměřené pro každý den v týdnu ve čtyřech časech - ráno, v poledne, večer a v noci.

#Vytvoř seznam průměrných teplot pro každý den.
#Vytvoř seznam ranních teplot.
#vytvoř seznam nočních teplot.
#Vytvoř seznam dvouprvkových seznamů obsahujících pouze polední a noční teplotu.


teploty = [
    [2.1, 5.2, 6.1, -0.1],
    [2.2, 4.8, 5.6, -1.0],
    [3.3, 6.5, 5.9, 1.2],
    [2.9, 5.6, 6.0, 0.0],
    [2.0, 4.6, 5.5, -1.2],
    [1.0, 3.2, 2.1, -2.0],
    [0.4, 2.7, 1.3, -2.8]]

#prumer teplot za kazdy den
# rano: 0, poledne: 1, vecer: 2, noc: 3

denni_prumer = [sum(den) / len(den) for den in teploty]

# ranni teplota

ranni_teplota = [den[0]for den in teploty]

# nocni teploty

nocni_teplota = [den[3] for den in teploty]

# poledni a nocni

poledni_a_nocni = [den [1] for den in teploty + den [3] for den in teploty]

#komentar M.Jurosz
# posledni cast ukolu nefunguje, zkus kdyz tak nahradit kodem co je nize
#poledni_a_nocni_teploty = [[den[1], den[3]] for den in teploty]
#print(poledni_a_nocni_teploty)
