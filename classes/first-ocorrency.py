phrase = input().lower()
letter = input().lower()

for i in range(len(phrase)) :

    if phrase[i] == letter :

        final_indice = i
        break

    else :

        final_indice = -1 

print(final_indice)
