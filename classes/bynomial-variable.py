# MATHEUS RAMOS RODRIGUES DE SOUZA

# Exercício 5 - Simulação de uma variável binomial [Peso 15]
# Uma variável aleatória binomial com parâmetros n e p, em que n é um inteiro positivo e p é
# um número entre 0 e 1, pode ser vista como a soma de n variáveis de Bernoulli
# independentes. Uma maneira de simular essa variável é a seguinte: faça um sorteio de n
# números u[j] entre 0 e 1. Para cada u[j], se u ≤ p, então o valor da variável aleatória de
# Bernoulli correspondente é 1. Caso contrário, seu valor é 0. Faça um programa em Python
# que peça ao usuário: os valor de n e p; n valores u[j] entre 0 e 1. O programa deve imprimir
# como saída o valor da variável Binomial. 

n = int(input())
p = float(input())
u = []
bernoulli = 0


for i in range(n) :
    u.append(float(input()))

for j in range(len(u)) :

    if u[j] <= p :
        bernoulli += 1

print(bernoulli)




