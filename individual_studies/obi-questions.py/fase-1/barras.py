n = int(input())
lista = list(map(int, input().split()))

matriz = []

h = max(lista)

for number in lista :
    zeros = h - number
    linha = zeros*'0' + '1'*number
    matriz.append(linha)

for i in range(h) :

    for j in range(n) :

        print(matriz[j][i], end=' ')
    print()


