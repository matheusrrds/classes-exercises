grades = list(map(float, input().split()))
total = 0
n = len(grades) - 1

while n >= 0 :
    total += grades[n]
    n-=1

n = len(grades)
average = total/n

print(f'{average:.1f}')