def recursive_sum(lista) :

    total_sum = 0

    if len(lista) == 0 :
        return total_sum

    if len(lista) == 1 :
        total_sum = lista[0]
        return total_sum

    total_sum += lista[-1] 
    lista.pop()

    total_sum += recursive_sum(lista)

    return total_sum

n = int(input())
signals_notunique = set()

for _ in range(n) :

    signals_notunique.update(list(map(int, input().split())))

x = int(input())

unique_ordered = list(signals_notunique)
unique_ordered.sort()

right = len(unique_ordered) - 1
left = 0
m = 0
ans = -1

while left <= right :

    m = (left + right) // 2

    if unique_ordered[m] > x :
        
        right = m - 1

    elif unique_ordered[m] < x :

        left = m + 1

    else :

        ans = m
        left = right + 1

print(f'Sinais processados: {unique_ordered}')

final_sum = recursive_sum(unique_ordered.copy())
print(f'Somatório dos sinais: {final_sum}')

if ans >= 0 :
    print(f'Sinal {x} encontrado no indíce {ans}.')
else :
    print(f'Sinal {x} não foi captado.')