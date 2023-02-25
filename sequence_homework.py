class Sequence:
    def __init__(self, seq: list):
        self.seq = seq

    def __str__(self):
        seq_str = ', '.join(str(x) for x in self.seq)

        return f'Последовательность {seq_str}'

    def __add__(self, other):
        nl = [i for i in other.seq if i not in self.seq]
        nl2 = self.seq + nl
        print(nl2)
        return Sequence(nl2)


seq1 = Sequence(
    input('1: ').split()
)

seq2 = Sequence(
    input('2: ').split()
)

new_seq = seq1 + seq2
print(new_seq)
