n = int(input())
s = int(input())

sequence = list(map(int, input().split()))
right = len(sequence)

freq = {0:1}

accumulation = 0
answer = 0

for r in range(right) :

    accumulation += sequence[r]

    answer += freq.get(accumulation - s, 0)

    freq[accumulation] = freq.get(accumulation , 0) + 1


print(answer)

