from pwm import pwm, seq_mais_provavel

# Le quantas sequencias sao
N = int(input())

seqs =  []

#Le as sequencias
for _ in range(N):
    seqs.append(input())

# Le a pseudocontagem
P = float(input())

# Le a sequencia
seq = input()

PWM = pwm(seqs, pseudocontagem = P)
print(seq_mais_provavel(seq, PWM))
