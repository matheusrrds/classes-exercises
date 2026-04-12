# MATHEUS RAMOS RODRIGUES DE SOUZA

# Exercício 7 - Produto interno [Peso 15]
# Faça um código que recebe duas coordenadas em R3 e imprime o produto interno dessas
# coordenadas.
# OBS1. De preferência, coloque apenas uma linha de input.

a1, a2, a3, b1, b2, b3 = map(float, input().split())
intern_product = a1*b1 + a2*b2 + a3*b3
print(intern_product)