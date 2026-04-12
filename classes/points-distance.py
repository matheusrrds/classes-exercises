# MATHEUS RAMOS RODRIGUES DE SOUZA

# Exercício 6 - Distâncias entre pontos [Peso 15]
# Faça um código que recebe 3 pontos com coordenadas em R2, calcula todas as distâncias
# entre todos os pontos e imprime a soma dessas distâncias. (OBS: o código precisa pedir
# apenas uma linha de input)

xa, ya, xb, yb, xc, yc = map(float, input().split())

distanceAB = ((xb-xa)**2 + (yb-ya)**2) ** (1/2) 
distanceAC = ((xc-xa)**2 + (yc-ya)**2) ** (1/2) 
distanceBC = ((xc-xb)**2 + (yc-yb)**2) ** (1/2)
distance_sum = distanceAB + distanceAC + distanceBC

print(f'{distance_sum:.2f}')