# MATHEUS RAMOS RODRIGUES DE SOUZA

def bynary_search(lista, value, begin=0, end=None) :

    if end is None :
        end = len(lista) - 1

    m = (begin + end) // 2
    ans = -1

    if begin <= end :

        if lista[m] > value :
            return bynary_search(lista, value, begin, m-1)
        
        elif lista[m] < value :
            return bynary_search(lista, value, m+1, end)
        
        else :
            ans = m
            return ans

    return ans

sequence = list(map(int, input().split()))
x = int(input())

index = bynary_search(sequence, x)

if index >= 0 :
    print(f'Pacote {x} localizado no índice {index}.')
else :
    print(f'Pacote {x} não consta no sistema.')