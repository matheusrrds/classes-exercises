n, f = map(int, input().split())
ciclos = list(map(int, input().split()))

# x // C1 + x // C2 + x // CN >= f
# se a soma der bem maior q f, significa que precisamos dum x menor

left = 1
right = 10**9
total = 0
ans = 0

while left <= right :

    m = (left + right) // 2
    total = 0

    for cicle in ciclos :
        total += (m//cicle)

    if total >= f :

        ans = m
        right = m - 1

    else :
        left = m + 1

print(ans)
