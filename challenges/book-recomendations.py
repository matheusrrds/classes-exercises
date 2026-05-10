# Uma rede social voltada para leitores deseja recomendar livros para um usuário-alvo. A recomendação funciona comparando os livros lidos pelo

# usuário-alvo com os livros lidos por seus amigos.
# Um livro é considerado uma "Super Recomendação" se ele satisfizer duas condições simultaneamente:

# 1. Ter sido lido por todos os amigos do usuário-alvo na rede.
# 2. Não ter sido lido pelo próprio usuário-alvo.
# Além disso, o programa deve calcular o total de obras distintas (únicas) lidas por toda a comunidade analisada (usuário-alvo + amigos).
# Formato da Entrada:
# 1. A primeira linha conterá os dados do usuário alvo no formato Nome,ID.
# 2. A segunda linha conterá os títulos dos livros lidos pelo usuário-alvo, separados por vírgulas.
# 3. As linhas seguintes conterão os livros lidos por cada amigo (uma linha por amigo, contendo os títulos separados por vírgulas).
# 4. A lista de amigos tem tamanho indefinido. A entrada de dados será encerrada quando for digitada a palavra "FIM".
# Formato da Saída:
# ● A primeira linha deve apresentar os dados do usuário-alvo no formato:
# Relatório para {Nome} (ID: {ID})
# ● A segunda linha deve apresentar o tamanho do acervo único:
# O acervo da comunidade possui {total} livros únicos.
# ● A seguir, o programa deve imprimir, um por linha, os títulos que são uma "Super Recomendação".
# ● Caso não haja nenhum livro que atenda aos critérios, imprimir a frase:
# Nenhum livro atende aos critérios de Super Recomendação.

user_name, num_id = input().split(',')

user_books = set(input().split(','))

friends_books = set()
intersection_friends = set()

first_friend = True
first_friend_books = set()
n = 1

while True :
    alone_friend_books = input().split(',')

    if alone_friend_books == ['FIM'] :
        break

    friends_books.update(alone_friend_books)

    if first_friend :
        first_friend_books.update(alone_friend_books)
        first_friend = False

        intersection_friends = first_friend_books
    elif n :
        n = 0
        intersection_friends = first_friend_books.intersection(alone_friend_books)
    else :
        intersection_friends = intersection_friends.intersection(alone_friend_books)

super_recommendation = intersection_friends.difference(user_books)
total_books = len(user_books.union(friends_books))

print(f'Relatório para {user_name} (ID: {num_id})')
print(f'O acervo da comunidade possui {total_books} livros únicos.')

if len(super_recommendation) >= 1 :
    for book in super_recommendation :
        print(book)
else :
    print(f'Nenhum livro atende aos critérios de Super Recomendação.')