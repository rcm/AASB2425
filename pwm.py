seqs = ['ATTG','ATCG','ATTC','ACTC']

def tabela_contagens(seqs, alfabeto = "ACGT", pseudocontagem = 0):
    return [{b : occ.count(b) + pseudocontagem for b in alfabeto} for occ in zip(*seqs)]

def pwm(seqs, tipo = "DNA", pseudocontagem = 0):
    """
        seqs: lista de sequências do perfil
        tipo: DNA ou PROTEIN, DNA por omissão
        pseudocontagem: valor da pseudocontagem

        Devolve: a matriz de dicionários com a PWM
    """
    assert all(len(seqs[0]) == len(s) for s in seqs), "As sequências não tem todas o mesmo tamanho!"
    tipo = tipo.upper()
    assert tipo in "DNA PROTEIN".split(), f"Tipo {tipo} inválido!"
    alfabeto = "ACGT" if tipo == "DNA" else "ARNDCQEGHILKMFPSTWYVBZX_"

    tabela = tabela_contagens(seqs, alfabeto = alfabeto, pseudocontagem = pseudocontagem)

    L = len(seqs[0])    # Tamanho do motif
    A = len(alfabeto)   # Tamanho do alfabeto

    return [{k : v / (L + A * pseudocontagem) for k, v in linha.items()} for linha in tabela]

def imprime_pwm(pwm, casas_decimais = 2):
    return [{k : round(v, casas_decimais) for k, v in linha.items()} for linha in pwm]


def prob_gerar_sequencia(seq, pwm):
    assert len(seq) == len(pwm), "tamanho da sequência e do motif não são iguais!"

    prob = 1
    for letra, coluna in zip(seq, pwm):
        prob *= coluna[letra]
    return prob


def seq_mais_provavel(seq, pwm):
    import re
    assert len(seq) >= len(pwm), "tamanho da sequência tem que ser maior ou igual ao do motif!"
    L = len(pwm)

    R = '.' * L
    probs = {}
    for s in re.findall(f'(?=({R}))', seq):
        probs[s] = prob_gerar_sequencia(s, pwm)
    maior_prob = max(probs.values())
    return sorted(set([k for k, v in probs.items() if v >= maior_prob]))
