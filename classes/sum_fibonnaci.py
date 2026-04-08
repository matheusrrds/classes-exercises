first = 1
second = 1
n = int(input('Please type the number N: '))

while n > 2 :
    term = first + second
    first = second
    second = term
    n -= 1

print(term)

# 1, 1, 2, 3, 5, 8, 13...


