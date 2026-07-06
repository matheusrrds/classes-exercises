# MATHEUS RAMOS RODRIGUES DE SOUZA

n = int(input())
user_hobbies = {}

for _ in range(n) :

    sequence = input().split(',')

    user = sequence[0]
    hobbies = set(sequence[1:])

    user_hobbies[user] = hobbies
try :
    user_a = input()
    user_b = input()

    interest_common = user_hobbies[user_a].intersection(user_hobbies[user_b])

    exclusiveA = user_hobbies[user_a].difference(user_hobbies[user_b])
    exclusiveB = user_hobbies[user_b].difference(user_hobbies[user_a])

    print(f'Interesses em comum: {interest_common}.')
    print(f'Exclusivos de {user_a}: {exclusiveA}.')
    print(f'Exclusivos de {user_b}: {exclusiveB}.')

except KeyError :

    print('Erro: Usuário não cadastrado.')

