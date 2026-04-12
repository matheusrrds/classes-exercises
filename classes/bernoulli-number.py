# MATHEUS RAMOS RODRIGUES DE SOUZA

# Considere uma variável aleatória de Bernoulli com parâmetro p, onde p é um número entre
# 0 e 1. Uma maneira de simular essa variável é a seguinte: faça um sorteio de um número u
# entre 0 e 1. Se u é menor ou igual a p, então o valor da variável aleatória de Bernoulli é 1.
# Caso contrário, seu valor é 0. Faça um programa em Python que peça ao usuário o valor u,
# p e que imprima o valor da variável de Bernoulli.

u = float(input())
p = float(input())

if 0 <= u <= 1 and 0 <= p <= 1 :

    if u <= p :
        bernoulli = 1
        print(bernoulli)
    else :
        bernoulli = 0
        print(bernoulli)
        
else :
    print('Valores inválidos')



