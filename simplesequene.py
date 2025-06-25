seq1 = int(input())
seq2 = int(input())
seq3 = int(input())
seq4 = int(input())

if abs(seq1 - seq2) == abs(seq2 - seq3) == abs(seq3 - seq4):
    print(int(abs(seq1 - seq2)))
else:
    print('NO')
