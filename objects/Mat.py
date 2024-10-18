class Mat:
    def __init__(self, rows, cols):
        self.mat = [[0 for c in range(cols)]
            for r in range(rows)]
    def numRows (self): return len(self.mat)
    def numCols (self): return len(self.mat[0])
    def __str__(self):
        "Devolve a matriz como uma string"
        return '\n'.join(' '.join(str(val) for val in row)
                for row in self.mat)
    def __repr__(self):
        "Utilizado no repl quando se pede para ver a matriz"
        return str(self)
    def __getitem__ (self, n):
        "Interface para a indexação []"
        return self.mat[n]
