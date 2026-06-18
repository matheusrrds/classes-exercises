g1,g2,g3,g4 = map(int, input().split())

nmesas = g4 + g3

# 7 5 2 4

g1 = max(0, g1-g3)

nmesas += (g2 + 1) // 2

if g2 % 2 != 0 :

    g1 = max(0, g1-2)

if g1 :

    nmesas += (g1 + 3) // 4

print(nmesas)










