f, r = map(int, input().split())

initial_indices = [indice for indice in range(1, f+1)]
infected_indices = list(map(int, input().split()))

initial_dist = infected_indices[0] - 1

final_dist = f - infected_indices[-1]

centrals = []

for i in range(len(infected_indices)-1) :

    central_distance = (infected_indices[i+1] - infected_indices[i]) // 2
    centrals.append(central_distance)

if len(centrals) == 0 :
    centrals.append(0)

distances = [max(centrals), initial_dist, final_dist]

print(max(distances))
    

# tem que achar o minimo (i - Pj) que seria no caso a quantidade de dias que um indice i
# leva para ser contaminado 

# ai tem que achar o maximo desse minimo (i-pj) para saber o maior numero de dias que
# o ngc leva pra ficar todo contaminado







