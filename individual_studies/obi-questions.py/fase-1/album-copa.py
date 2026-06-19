total = int(input())
m = int(input())
bought_stickers = set()

for _ in range(m) :
    bought_stickers.add(int(input()))

missing = total - len(bought_stickers)

print(missing)