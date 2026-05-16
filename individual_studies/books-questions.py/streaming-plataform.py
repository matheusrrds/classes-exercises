name, id_num = input().split(',')
user_movies = input().split(',')

unique_movies = set(user_movies)
intersection_friends = set()

more_movies_watched = 0
first_friend = True

while True :

    friends_movies = input().split(',')

    if friends_movies == ['FIM'] :
       break

    if len(friends_movies) > more_movies_watched :
        more_movies_watched = len(friends_movies)

    if first_friend :
        intersection_friends.update(friends_movies)
        first_friend = False
    else :
        intersection_friends = intersection_friends.intersection(set(friends_movies))

    unique_movies.update(friends_movies)

super_recommendation = intersection_friends.difference(set(user_movies))

print(f'Relatório do usuário {name} (ID: {id_num})')
print(f'A comunidade possui {len(unique_movies)} filmes únicos.')
print(f'O amigo com maior catálogo possui {more_movies_watched} filmes.')

print('Filmes Recomendados:')

for book in super_recommendation :
    print(book)