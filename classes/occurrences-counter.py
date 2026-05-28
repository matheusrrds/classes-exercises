def occurrences(value,lista, counter=0) :

    if len(lista) == 0 :
        return counter
    
    if lista[0] == value :
        return occurrences(value,lista[1:], counter+1)
    
    return occurrences(value,lista[1:], counter)

print(occurrences(7, [1,1,2,3,3,1,3, 7, 7,7,7,7,7,7,7,7]))