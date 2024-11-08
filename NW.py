from blosum import Blosum62
from pprint import pprint

def align(s1, s2, g = -8):
    subst = Blosum62().subst
    score = [[0 for x in '-' + s1] for y in '-' + s2]
    trace = [[' ' for x in '-' + s1] for y in '-' + s2]

    # Primeira linha
    for p, x in enumerate(s1):
        score[0][p + 1] = score[0][p] + g
        trace[0][p + 1] = 'E'
    # Primeira coluna
    for p, y in enumerate(s2):
        score[p + 1][0] = score[p][0] + g
        trace[p + 1][0] = 'C'

    for p1, x1 in enumerate(s1):
        for p2, x2 in enumerate(s2):
            score[p2 + 1][p1 + 1] = max([
                    score[p2    ][p1    ] + subst(x1, x2),  # Diagonal
                    score[p2    ][p1 + 1] + g,              # Cima
                    score[p2 + 1][p1    ] + g,              # Esquerda
                    ]
                    )
            if score[p2 + 1][p1 + 1] == score[p2    ][p1    ] + subst(x1, x2):
                trace[p2 + 1][p1 + 1] = 'D'
            if score[p2 + 1][p1 + 1] == score[p2    ][p1 + 1] + g:
                trace[p2 + 1][p1 + 1] = 'C'
            if score[p2 + 1][p1 + 1] == score[p2 + 1][p1    ] + g:
                trace[p2 + 1][p1 + 1] = 'E'

    return score, trace

def print_matrix(mat):
    for linha in mat:
        for x in linha:
            print(f"{x:3d}", end = " ")
        print()

def print_trace(mat):
    for linha in mat:
        print(*linha)

def score(s1, s2, g = -8):
    return align(s1, s2, g)[-1][-1]

def reconstroi_align(s1, s2, trace):
    C = len(s1)
    L = len(s2)

    A1 = ''
    A2 = ''

    while C > 0 or L > 0:
        print(L, C)
        if trace[L][C] == 'D':
            L -= 1
            C -= 1
            A1 = s1[C] + A1
            A2 = s2[L] + A2
        elif trace[L][C] == 'E':
            C -= 1
            A1 = s1[C] + A1
            A2 = '-' + A2
        elif trace[L][C] == 'C':
            L -= 1
            A1 = '-' + A1
            A2 = s2[L] + A2
        else:
            abort("NAO PODE CHEGAR AQUI!!!")
        
    print(A1)
    print(A2)

s1 = "HGWAG"
s2 = "PHSWG"
S, T = align(s1, s2)
print_matrix(S)
print()
print_trace(T)

reconstroi_align(s1, s2, T)
