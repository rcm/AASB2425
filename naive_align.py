from blosum import blosum62
from collections import defaultdict
from pprint import pprint

def subst(x, y):
    return blosum62[x][y]

N = 0
problemas = {}

def score(s1, s2, g = -8):
    global N
    global problemas
    N += 1
    chave = (s1, s2)
    if chave in problemas:
        return problemas[chave]
    if s1 and s2:
        res =  max(
            score(s1[:-1], s2[:-1]) + subst(s1[-1], s2[-1]),    # substituir o último em cada
            score(s1[:-1], s2) + g,                             # apagar o último caractere da primeira
            score(s1, s2[:-1]) + g)                             # apagar o último caractere da segunda
    else:
        res = max(len(s1), len(s2)) * g
    problemas[chave] = res
    return res

print(score("HGWAG","PHSWG"))
print(N)
pprint(problemas)
