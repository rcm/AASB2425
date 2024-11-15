from collections import defaultdict
from pprint import pprint

DEBUG = False
def query_map(seq, window_size):
    """
    Returns a dictionary of all key/value pairs where
        key is a substring of size window_size
        value is a list of occurrences (offsets)
    """

    res = defaultdict(list)
    size = len(seq)
    for position in range(size - window_size + 1):
        if DEBUG:
            print( position, seq[position : position + window_size])
        subseq = seq[position : position + window_size]
        res[subseq].append(position)
    if DEBUG:
        pprint(res)
    return res

def get_all_positions(subseq, seq):
    return [P for P in range(len(seq) - len(subseq) + 1) if seq[P : P + len(subseq)] == subseq]
        
def hits(qm, seq):
    """
    for all keys Q in qm
        for all positions in seq where Q exists
        add the tuple of corresponding positions
    """
    res = []
    for Q, LstPos in qm.items():
        for P1 in LstPos:
            for P2 in get_all_positions(Q, seq):
                res.append((P1, P2))
    return res

def extend_hit_direction(query, seq, hit, window_size, direction):
    """
        query: first string
        seq: second string
        hit: tuple of offsets
        window_size:
        direction: +1 or -1


        try to extend in this direction one character at a time
        If both characters are the same, advance
        Otherwise continue if half the characters are the same


        returns a tuple with:
        - The initial position in query
        - The initial position in seq
        - The match size
        - The number of equal characters
    """

query = "AATATAT"
seq = "AATATGTTATATAATAATATTT"

qm = query_map(query, 3)

print(hits(qm, seq))
