a, b, c = map(int, input().split())

rt = a // 2
eggs = b // 3
cs = c // 5

ingredients = [rt, eggs, cs]
mininum = min(ingredients)

print(mininum)