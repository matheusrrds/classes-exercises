n, k = map(int, input().split())
sequence = list(map(int, input().split()))

ans = 0
accumulator = 0

freq = {0:1}

for r in range(len(sequence)) :

    accumulator += sequence[r]

    ans += freq.get(accumulator-k, 0)

    freq[accumulator] = freq.get(accumulator, 0) + 1

print(ans)
