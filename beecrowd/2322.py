n = int(input())
pieces = list(range(1, n+1))

data = input().split()

for piece in pieces :
    piece = str(piece)

    if piece not in data :
        print(piece)

