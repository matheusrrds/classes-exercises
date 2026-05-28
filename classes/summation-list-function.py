def summation(lista) :

    if len(lista) == 0 :
        return 0
    
    return lista[0] + summation(lista[1:])

print(summation([782378,2323,22,1]))
