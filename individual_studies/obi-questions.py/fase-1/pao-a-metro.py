n = int(input())
k = int(input())

sizes = list(map(int, input().split()))

left = 1
right = 10**4
ans = 0

# x tq m1 // x + m2 // + m3 // x + m4 // x = n

while left <= right :

    m = (right + left) // 2
    total = 0

    for size in sizes :
        total += size // m

    if total >= n :

        ans = m
        left = m + 1

    else :
        right = m-1

print(ans)




