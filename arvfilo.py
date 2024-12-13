def distancia(s1, s2):
    mat = [[0] * (1 + len(s2)) for _ in range(len(s1) + 1)]
    for i in range(len(s2) + 1):
        mat[0][i] = i
    for i in range(len(s1) + 1):
        mat[i][0] = i
    for L, x in enumerate(s1):
        for C, y in enumerate(s2):
            add = 0 if x == y else 1
            mat[L + 1][C + 1] = min(mat[L][C] + add, mat[L][C + 1] + 1, mat[L + 1][C] + 1)

    return mat[-1][-1]

def matriz_distancias(lista_seqs):
    dist = {}
    for s1 in lista_seqs:
        for s2 in lista_seqs:
            if s1 == s2: continue
            if s1 not in dist: dist[s1] = {}
            if s2 not in dist: dist[s2] = {}
            dist[s1][s2] = distancia(s1, s2)
            dist[s2][s1] = distancia(s1, s2)
    return dist

def par_com_dist_min(mat_dist):
    dist_min = None
    for s1 in mat_dist:
        for s2 in mat_dist[s1]:
            if dist_min is None or dist_min > mat_dist[s1][s2]:
                dist_min = mat_dist[s1][s2]
                seqs = s1, s2
    return seqs, dist_min

def atualiza_matriz_dist(mat_dist, s1, s2):
    linha_s1 = mat_dist[s1]
    linha_s2 = mat_dist[s2]

    del mat_dist[s1]
    del mat_dist[s2]
    for k in mat_dist:
        del mat_dist[k][s1]
        del mat_dist[k][s2]

    cluster = (s1, s2)
    mat_dist[cluster] = {}

    for k in mat_dist:
        if k == cluster:
            continue
        d = (linha_s1[k] + linha_s2[k]) / 2
        mat_dist[k][cluster] = d
        mat_dist[cluster][k] = d

    return mat_dist

def arv_filo(lista_seqs):
    D = matriz_distancias("CCG GT GTA AAT AT ACG ACGT".split())

    while len(D) > 1:
        (s1, s2), _ = par_com_dist_min(D)

        D = atualiza_matriz_dist(D, s1, s2)
    lista_de_chaves = list(D.keys())
    arv = lista_de_chaves[0]
    return arv

if __name__ == '__main__':
    from pprint import pprint
    D = matriz_distancias("CCG GT GTA AAT AT ACG ACGT".split())
    pprint(D)

    print(arv_filo(D))
