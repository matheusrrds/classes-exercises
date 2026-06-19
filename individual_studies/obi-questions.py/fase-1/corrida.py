times = {}
shortest_time = 10**6

for _ in range(2) :
    n, d, v = map(int, input().split())
    times[n] = d/v

for key in times :
    if times[key] < shortest_time :
        shortest_time = times[key]
        answer = key

print(answer)
    