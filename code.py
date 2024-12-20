import pdb

def revcomp(dna : str) -> str:
    """
        Return the reverse complement of a dna string

        dna: str
            a string of dna (should only have bases ACGT)
        returns
            a string with the reverse complement
    """
    #reverse = dna[::-1]
    reverse = ""
    for base in dna:
        reverse = base + reverse
        
    result = ""
    for base in reverse:
        result += complementary_character(base)
    return result
def complementary_character_stupid(base: str) -> str:
    "Gives the complementary base"
    if base == 'A': return 'T'
    if base == 'T': return 'A'
    if base == 'C': return 'G'
    if base == 'G': return 'C'
def complementary_character(base: str) -> str:
    "Gives the complementary base"
    norm = "ACGT"
    comp = "TGCA"

    pos = norm.index(base)
    return comp[pos]
def complementary_character(base: str) -> str:
    "Gives the complementary base"
    norm = "ACGT"
    comp = "TGCA"

    translation = dict(A = 'T', C = 'G', G = 'C', T = 'A')
    return translation[base]
def complementary_character(base: str) -> str:
    "Gives the complementary base"
    norm = "ACGT"
    comp = "TGCA"

    translation = dict(zip(norm, comp))
    return translation[base]

def get_codons(dna):
    result = []
    for pos in range(0, len(dna), 3):
        codon = dna[pos : pos + 3]
        if len(codon) == 3:
            result.append(codon)
    return result

def codon_to_amino(codons):
    from table import table
    res = ''
    for codon in codons:
        res += table[codon]
    return res

def get_prots(amino):
    inside_prot = False
    prots = []
    prot = ''

    for aa in amino:
        if aa == 'M':
            inside_prot = True

        if aa == '_':
            if inside_prot:
                prots.append(prot + '_')

            inside_prot = False
            prot = ''

        if inside_prot:
            prot += aa
    return prots

def get_orfs(dna):
    """ Recebe uma cadeia de dna e devolve uma lista com 6 componentes correspondente às 6 ORF
    3 5' -> 3' e 3 3' -> 5'
    """
    tres_orfs = lambda dna: [get_codons(dna[p : ]) for p in range(3)]
    def tres_orfs(dna):
        return [get_codons(dna[p : ]) for p in range(3)]
    return  tres_orfs(dna) + tres_orfs(revcomp(dna))

def get_all_prots(dna):
    orfs =  [codon_to_amino(O) for O in get_orfs(dna)]
    prot_orfs = [get_prots(O) for O in orfs]
    LPs = {p for LP in prot_orfs for p in LP}
    return sorted(LPs, key = lambda P : (-len(P), P))


if __name__ == '__main__':
    """
    amino = 'UUU_AAMYY_GGGGM_XXXMRTM_OOO_MARRECO'
    print(amino)
    get_prots(amino)
    """

    dna = 'TGTGGGGAGGTCATAGGTACTGGCCCCCATGATGGGGCAGGAGTAAATACTGACACAGCACGGTCGTGCTAATTTATTCGTTTGACTGGATTTGCGTATATCAAACTGAAACCTCGTGTCCATATGTGAGTCTAGCAATCTCCTTGTCGGAGGTCTAATACCGCCTTGGATAGAATTATCGCGAACTGATTCTCCGAGGCATCATAGGGCTAGAGGCACTAGCGTGGTAATTTTGTAGTCCCTATCTGATTAAACTGGGTCTGCTCCCCAGCTTATGTGCTCTGACACCAGACTATCTAGCACGTAGCCCGGATAGAAGCGACAATTGGATAGCCATGCGTGTAAGATGCGCCCGTTTGTTGTGGAGATCACCAATAGGGAGAAATTTTTAAGCGAGGCTAGTACAGATTGATAAACAAACCGCACAGAGCGTACTCGTTTCCCTGCGTGACTCACCGATCTAGCAAGCATGTTTTTTGCGTCCCGCGGTTTGTGCGGAATCTACCAACTGTTCCGGTTCGAATTTACCCACACCTGCGTCCATGCAGCAGGCGGTCAAACGCGTCGGCCTGCTGATCAGGATCCACCCTAAATCTCAAGCTTTGAGAATTATCGTGGGCTACAATTCTATTATGTCACATGGGTAATTTTTGCGAACGCGCTTCTGCCCTACGCATGCATCTAGAGGCGGACGTCTACTCGGTACTAGTTTATCCCACAGAAGATATTTTTGGTGGTCCGCCTTATCTCGTGTGTTTGCAAGATGCTTGTGGCACTGATGCGCCCGGTAGAACCACGCCCCGCAAAACGGAAAGCGCACTCCCGGGTATGTCTATCTCCCATAAGTGGCCAGCGCCGGACGTCAGTAATCACTAAGTATTAACTAGCGCGACTACAGTATTATGTTCTAAATCCACCAAGTTAGTTCCGGTAAGATAATTTAGCAAACACGAAGCATCTTGTCCGGGTTTCCAACAGCGCCCATTCAGAAGGATAACCCGCTACCCCAGGTTTTACCTACAGACCTAAGGCCCCCGCGAAACGTGTCCCCGAGGGTGGATCCAGATGAGTTCAATCCACCGGATACCCGGGTTGCTCCCAAGGACCTAGATGCTTGGCACCATCCGACTTGCTTGGACCCCAGTCATGCGTACACGGTCAAAACGTCCCGGCAGGACCCACGAAAAGGACTTGCGTTTCATACTTGAACTATGTAACAAACTCCGAACTTGGTAGTTACAAACACAGTTGCTGGCGTCCTCACGGTGGGGAGCCGCTCGAGGCGGGAAATCCTAACGCGCTCAAGAACGTCATGCGGCTGTCCCTTCGGCTGACTCATCTACGATGCACGATAGATCAACTGGACTGGTGAGTACAATCGTTCTTTTTCCTGGAGCTATAAGTTATTCCACGGTGGGTCGTTCGAAGTGGATTCAACAGAAAAGACACGATAGGTCTCACCGCAGAAGTCCCTGCCTTATACTCCGAGGGTCCTGTGAGGCTCGTGGTACGACCCTTGAAAGGCCTTCTCGATAAGTTTTAGGTTTCCAAGTTGTGCGCCGCATAAACAACACTCACCATGGTGATGGGCAGTCCGTGATTAGCCCGATGTGCACAACGAGGGGTAGGACTACTGAGTATGAGCTCGGACCCTGCTATTCATATGGTGGACATACCACTCGATACTCTCTCCGGACAGCCTCCAACGTCCCCCACTGATTCTGTATCCCCGAGGACGCCCGCTAGCCCGCTCCACGAGTTGTCGGTTTGCGCCTTCCTGGGCACAGTCCCGTTCCCCTGGAGGCTTGGCCACAATTGCAAGACAATATGGCTGTCTACAGACCGGAGTGTTAGTGGGCGGAAAACGCGTTAGTATACGGCGTATGGGCTCGCCTGAATGCACGGCGGTGCACGGTCTATTGCCGCTACTCGTGCTCGAGGGAGCCCTATCAAAGCCGCTTGCCTGCCGACGTAAGCATGCGCCTAACGGCGGTACGAATGTACGTACCGGTTTTGTCGCTAGGCCCTGTCTCCATTATCCTCAACGGGTCTCGGGTTCGTAAGTGTGGTTCGGGCTGGACTTACGCGCTCTTAAAAGGAAGGAGTTCGATCGTGGACTGAGTAACCTCCTACCATGAGTAAGCTAGGACACAAATGGATTGATTGATACAAGTATTGAGTAGTGCAGTACCGGTCCAGACTCTTAGTCTGCCGAAGCCATCATGGGAGTAAGCCACCTATGCGATGGTTATGGGTCGCGGGCACTATAGGGCGTACTGTGATCTCGGTCGCATCGCGCAGTTCTGGTATTTACACCCTTCCACACATGCGGACTGTTCCGTGAGCGAGTGAGCCCGTCATGTCCACCCAAAAGCCGCACAGCTACGTCAAGGGAAGACGCCAACCTGATACTCTTCTTGTTAAGCCTTAGTGTGCTACTTCAGGTACACCGTACACGGATAACCAACTCGTTCCATCAACTGCGGTCGCACAAACTTGGTTACCACAATCTAGTAACACCGAAAAACTGAGTACCTAAGCCTAGCAAGTGATACAGAGGGGCATTGGTACCAGACACAACTACCAGAGCATCATGCTCCGGCTCGCGCTCACTTGCAAACACGGACCCGGCCTTTGGTGTCTGAGCTGAGATAATAGAGCGGCATTGGCTTTGGTCGGAAAGGTACTACAGTTCCCGTGGAGAACATAGCTACTTGTTGTTCTGTCCATTGCTGCGATCGAGTTGATATAAAATTGAGGGGACATACCCTTCCTCGCGAGAGCACCCAGTTTGGGTTGGATGACGGTACACGTCCCTTGACAGATTGACCACAACCTCGAACAGCCTTCAATGAATCGCCTGACGTCTCATACGAAGTCAGTGCAGGGAATAGGCGTTCGCTACGCCGTTCCTTCAAGGTAGGACAGTGCTGGGACGAGCGGAATCCCAGAGGGACTAACCATGGCCCTTCCCACCTGTGGCCGCAATCCCTGGGATCGTGCTACCTGCGGGGGTATGTTAGTCTCTCTGAACCCTATGAACCGCTACTTGCCCGCAACTTCCGCCTGGCTACAGTAGCCCCATAGACCGCGTACTCTCAGAGTCGTGGGAGCACTTGTCGGCGGATGCGTAGCCAATTATGTTCGGCCATCTGTGGATTGGATGTACGACTCTGGAGAATCGCGGACCGGTACGCAAATACAGTGGCCGACTATAAGCGGGCGGGATCTCACCTCTTGAATAGTAGCGTCCCCGTGTGTTCTCACAGTACGCCGGCGGGCATATAAACGGTTTCGGTGAAGTCAGAATAGACAAGCGTGCATTGTGTACTCAGTCAAAAATTGATAGGCAGTGTCCCACCGCTATCCTGCCGCACTCTAGTACGGCATGTCATACAGAAAAGCGCCCTTTACCCGGTCCGCGCACCGGGCGGGCGACCGCCGTTATGAATCGTAAACTAAGGTCCGGGGGTTACCTAAGTACCCCTCCCTGGGAGACTAAACGATTTCGTTGAAAAAAAAAGTCTCGCTTTGGTGAATCTTCGATACCGGGAACGGCACCTGCAATAGACGATCGACCTCATTCAGGTAAACTGGAACAAGAGCGATCTTTAAATGAATGTTTGTGGGAAAATGGCGGTACACGACTGAGGCAACATCTGTGATCCCTCTAGGCGAATAGGGGTTGTAGTAGCGCAACAGGACCTGAAACTAGAACATCCTTTGAATCCCCCCTCGTGGGTAAGCCTAAATTTTCCTCGTATCGCTACTTCGAGATTCGTCCAGGGTGAGTTTCCCCCAAGCATTTGGCATTACTGGTTAATGTATAAACTGAACTTAGGACGAGGCGCCTAGAATGAAGACACGGTGAGGCAGGTCTTAACACGAATTCGCTCGGCGCATCTCAAATAGCAACAAAAAGGCCCTTTACCGCAGTGGATTGCTTTTGGCTCCGTTCGGCTGGTTTCCATAAGCGCCCGACTTTGAGTTTCGATCACCACATAGGATATACCTAGCTGGCAAAGCGGGCCACGCAAAGTTCGACTCTGACGAATATAAACAAAGTTCCACTAGTGAAAGCTGAGCGTGGCCTACAGAGTTCGATGTACAGGTCCGCACAGGACAGTTAGTATAATTGCAGGAGAGAACCGCCACATCACGCATTGCTCCGCAAACATATCCTGGCGTGGCTAGAAGTATGTTAGCGCTTGCGGTACGAACCTAAAGGTAGGATACTGAGTCAAGAAACTTAAGTTTTTCAAAGTAACGCGAAAGGATATCATCCTGTCCAATAATGAATTCTACTTACATGGCACAGATACTAACATGTGCCCGTAAGGACTATGCCTTATCGCCGACGAAAAAGCTCAACGTTGTGCCCCCATAGGACCACGCGCAAAGCAGGGTCCTCGTCCCAACTTGATATCCGCGATATCTGCACACTCAAGCCTATTGAGATGGATCCGCGCGTACGGAAGGTCTACCAGCCTTGCGTTCCTAACAAATATTATTGAGATGATTCTAACATACGTGATCGATACACCATACTCACGAAGGCTGTATTTACGCCATGAGGCAGCGCTGCTTTGACGCCGGTTATGACCATGCCTGGCAGACCTTCTCTTAGAGTAAGATCTACCAAGGAGTAGAAGACGATGGTCTGCGCATACCGAAATGAGTATACAACAACTACTGTTAAGGTTAGACCTAATCTGCCACCTGCCGTTCTACTACGAAACTACCCCGCATTCGGGAGGTTCTTTCCTACTCTTAACATCGTCTATAACACTGCGACGGTCCCAGCTACAGCAGTGGTGTGTCCGTGTCCAGCGGAGGAATCTGGGATTGGCCGCTACGTAGTAAAATCGCATCGCAGTTGCGTCTGAAATCTCTGACCTCATAGTGAGATCCGCATAGGTATGGTGAGCCTGCGCAATACTTCTAATATGTTCGGCAACCGTCTGTGTACTTCAGGGTGGGCCAGGCGCAAGATCATAGAG'
    print(dna, get_all_prots(dna), sep = '\n')

