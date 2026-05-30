f, r = map(int, input().split())
initial_positions = list(map(int, input().split()))

infected_indices = {position-1 for position in initial_positions}

fita_contamined = [0]*f
counter = 0
proceed = True
transition = []

while proceed :

    infected_indices.update(transition)
    transition = set()

    for indice in infected_indices: 

        fita_contamined[indice] = 1

    for indice in infected_indices :

        if indice == 0 :
            transition.add(indice+1)

        elif indice > 0 and indice < (f-1) :
            transition.update([indice-1, indice+1])
        
        else :
            transition.add(indice-1)

        if fita_contamined == [1]*f :
            proceed = False

    if proceed != False :
        counter += 1
        

print(counter)

# AINDA NAO FINALIZADO ERRO TEMPO LIMITE :/






