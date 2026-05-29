n, k = map(int, input().split())
names = []

for _ in range(n) :
    name = input()
    names.append(name)

names.sort()

print(names[k-1])