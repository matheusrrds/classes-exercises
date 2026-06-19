a, g, ra, rg = map(float, input().split())

kmgasoline = g / rg
kmalcohol = a / ra

if kmgasoline <= kmalcohol :
    print('G')
else :
    print('A')

