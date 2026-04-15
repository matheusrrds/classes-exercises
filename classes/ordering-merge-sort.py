# MATHEUS RAMOS RODRIGUES DE SOUZA

a, b, c, d, e = map(int, input().split())

if a > b : # 1º comparação
    a, b = b, a

# ordenamos os primeiros 2 elementos

if c > d : # 2º comparação
    c, d = d, c

# ordenamos os proximos 2 elementos

if a > c : # 3º comparação
    a, c = c, a

# ordenamos os menores de cada par

if b > d : # 4º comparação
    b, d = d, b

# ordenamos os maiores de cada par

if b > c : # 5º comparação
    b, c = c, b

# comparamos os do meio, finalizando assim a ordenação dos 4 primeiros elementos, falta apenas um

if e > c : # 6º comparação
    if e < d : # 7 comparação, se o e < d é necessario que ele troque de posição com d
        e, d = d, e 
        print(a,b,c,d,e)
    else : # se o e for maior ou igual ao d não é necessario mudar a ordem
        print(a,b,c,d,e)
else:
    if e > b : # 7º comparação, se e >= b e e <= c temos a seguinte ordem final:
        print(a,b,e,c,d)
    else :
        if e > a : # 8º comparação, se e <= b e e >= a temos a seguinte ordem final:
            print(a,e,b,c,d)
        else : # se e <= a temos a seguinte ordem final:
            print(e, a, b, c, d)

# O programa apresenta 7 comparações em todos casos exceto e <= c and e <= b






    















