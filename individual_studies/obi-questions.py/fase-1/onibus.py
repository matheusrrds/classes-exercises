n, t = map(int, input().split())

sequence = [int(input()) for _ in range(n)]
sequence.sort()

begin_time = sequence[0]
max_time = sequence[0] + t

onibus = 1

for i in range(len(sequence)) :

    if sequence[i] <= max_time :
        continue

    begin_time = sequence[i]
    max_time = sequence[i] + t

    onibus += 1

print(onibus)