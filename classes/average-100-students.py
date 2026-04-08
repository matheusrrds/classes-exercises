grade = list(map(float, input().split()))
total = 0
n = 100

while n > 0 :
    total += grade[n-1]
    n -= 1

average = total / 100
print(f'{average:.1f}')