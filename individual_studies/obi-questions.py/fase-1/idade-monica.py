m = int(input())
a = int(input())
b = int(input())

# m = a + b + c

left = 1
right = 200

while left <= right :
    c = (left + right) // 2

    total = a + b + c

    if total >= m :
        ans = c
        right = c - 1
    else:
        left = c + 1

ages = [a,b,c]
print(max(ages))


