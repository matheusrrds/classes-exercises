i = 0
while True :
    n = int(input())
    i += 1

    if n == 0 :
        break

    x, y, u, v = map(int, input().split())

    cnlftx = x
    cnlfty = y

    cnrtx = u
    cnrty = v

    no_intersection = False

    for _ in range(n-1) :

        x, y, u, v = map(int, input().split())

        if cnlftx < x < cnrtx :
            cnlftx = x
        
        if cnlfty > y > cnrty :
            cnlfty = y
        
        if cnrtx > u > cnlftx :
            cnrtx = u
        
        if cnrty < v < cnlfty :
            cnrty = v
        
        # se o y mais alto do retangulo novo for menor q o antigo mais baixo n tem intersecção
        # se o y mais baixo do retangulo novo for maior que o antigo mais alto n tem intersecção

        # se o maior x do retangulo novo for menor que o menor x do antigo n tem intersecção
        # se o menor x do retangulo novo for maior que o maior x do antigo n tem intersecção

        if y < cnrty or v > cnrty :
            no_intersection = True
        
        if u < cnlftx or x > cnrtx :
            no_intersection = True

    if no_intersection :
        print(f'Teste {i}')
        print('nenhum')
        print()
    else :
        print(f'Teste {i}')
        print(cnlftx, cnlfty, cnrtx, cnrty)
        print()



        







        



