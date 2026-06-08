n, k = map(int, input().split())
sequence = list(map(int, input().split()))
count = 0

while True :
    total = 0

    for i in range(len(sequence)):

        total += sequence[i]

        if total == k :
            count += 1
    
    sequence.pop(0)

    if not sequence :
        break

print(count)

