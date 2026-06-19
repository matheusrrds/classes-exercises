a = int(input())
b = int(input())
c = int(input())
d = int(input())

answer = ''
i = 0

while d*i <= c :

    if a <= (c - d*i) <= b :
        answer = 'S'
        break
    else :
        answer = 'N'
    i += 1

print(answer) 