# MATHEUS RAMOS RODRIGUES DE SOUZA

# Exercício 3 - Ordenação de 5 elementos com 7 comparações [Peso 25]
# Escreva um programa em Python que recebe como entrada 5 valores e, efetuando no
# máximo 7 comparações, ordena os valores de entrada, conforme discutido na Aula 6. O
# programa deve imprimir os valores de entrada em ordem crescente. Inclua comentários no
# código para explicar o raciocínio por trás de cada trecho. Ao lado de cada comparação,
# inclua um comentário indicando quantas comparações foram realizadas até aquele ponto.

a, b, c, d, e = map(int, input().split())
ordered_list = []

if a > b : # 1º comparação
    a, b = b, a

# ordenamos os primeiros 2 elementos

if c > d : # 2º comparação
    c, d = d, c

# ordenamos os proximos 2 elementos

if b > d : # 3º comparação, comparando os maiores de cada par
    b, d = d, b
    a, c = c, a

# portanto temos que a <= b <= d   e   d >= c

if e > b : # 4º comparação, encaixemos agora o e utilizando essas informações, sabendo que c<=d para inserir c no final não é necessario comparar o c com o d, apenas com os outros 3, portanto iniciaremos comparando com o central entre esses 3 para realizar o minimo de comparações

    if e > d : # 5º comparação 
        ordered_list = [a,b,d,e]

        if c > b : # 6º comparação
            ordered_list = [a,b,c,d,e]
        else :

            if c > a : # 7º comparação
                ordered_list = [a,c,b,d,e]
            else :
                ordered_list = [c,a,b,d,e]

    else :

        ordered_list = [a,b,e,d]

        if c > b : # 6º comparação

            if c > e : # 7º comparação
                ordered_list = [a,b,e,c,d]
            else :
                ordered_list = [a,b,c,e,d]

        else :

            if c > a : # 7º comparação
                ordered_list = [a,c,b,e,d]
            else :
                ordered_list = [c,a,b,e,d]

else :
    if e > a : # 5º comparação
        ordered_list = [a,e,b,d]

        if c > e : # 6º comparação
            if c > b : # 7º comparação
                ordered_list = [a,e,b,c,d]

            else :
                ordered_list = [a,e,c,b,d]

        else :
            if c > a : # 7º comparação
                ordered_list = [a,c,e,b,d]
            else :
                ordered_list = [c,a,e,b,d]

    else :
        ordered_list = [e,a,b,d]

        if c > a : # 6º comparação
            if c > b : # 7º comparação
                ordered_list = [e,a,b,c,d]
            else :
                ordered_list = [e,a,c,b,d]
        else :
            if c > e : # 7º comparação
                ordered_list = [e,c,a,b,d]
            else :
                ordered_list = [c,e,a,b,d]

print(ordered_list)









