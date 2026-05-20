n, q = map(int, input().split())

matriz = []

for _ in range(n) :
    matriz.append(list(input()))

for _ in range(q) :

    matriz_nova = [linha[:] for linha in matriz]

    for i in range(n) :
        for j in range(n) :
            qtdm = 0
            qtdv = 0
            for y in [-1, 0, 1]:
                for x in [-1, 0, 1]:
                    if i+y < 0 or i+y > n-1 or j+x < 0 or j+x > n-1 or (y == 0 and x == 0):
                        continue

                    if(matriz[i+y][j+x] == '0'):
                        qtdm+=1
                    else:
                        qtdv+=1
                    
            if matriz[i][j] == '0' and qtdv == 3 :
                matriz_nova[i][j] = '1'
            
            if matriz[i][j] == '1' and qtdv < 2 :
                matriz_nova[i][j] = '0'
            
            if matriz[i][j] == '1' and qtdv > 3 :
                matriz_nova[i][j] = '0'

    matriz = [linha[:] for linha in matriz_nova]

for line in matriz:
    print(*line, sep="")
