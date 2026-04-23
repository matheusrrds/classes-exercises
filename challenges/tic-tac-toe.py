# Exercício 1 - Jogo da Velha
# Programe o jogo da velha!
# Seu jogo deve perguntar ao jogador em qual posição deve ser efetuada a próxima jogada,
# controlando se a posição selecionada já foi utilizada ou não. Caso a posição escolhida já
# tenha sido utilizada, uma mensagem deve ser apresentada e deve ser solicitada uma nova
# posição a ser jogada. O jogo irá encerrar quando a vitória de um jogador for identificada ou
# quando não houver mais jogadas possíveis. Após cada jogada, o estado corrente do
# tabuleiro deve ser impresso na tela. Além disso, quando for identificada vitória ou empate,
# essa informação deve ser impressa na tela bem como a identificação do jogador vencedor,
# quando for o caso.

# MATHEUS RAMOS RODRIGUES

places = [
          [' ', ' ', ' '], 
          [' ', ' ', ' '], 
          [' ', ' ', ' ']
          ]

winner = False
turn = 1

while True :

    line_choosed = int(input('Choose the line you wanna play: '))
    column_choosed = int(input('Choose the column: '))
    n = 0

    for line in range(1, len(places) + 1) :
        for column in range(1, len(places[line - 1]) + 1) :
                if line_choosed == line and column_choosed == column:

                    if places[line_choosed - 1][column_choosed - 1] != 'X' and places[line_choosed - 1][column_choosed - 1] != 'O' :

                        if turn % 2 == 1 :
                            places[line_choosed - 1][column_choosed - 1] = 'X'
                            turn += 1
                        else :
                            places[line_choosed - 1][column_choosed - 1] = 'O'
                            turn += 1

                    else :
                        print('Please choose a place hasnt been chosen yet')
                        n = 1

    if n != 1 :
        print('\n', places[0][0], ' | ', places[0][1], ' | ', places[0][2], sep='')
        print('---------')
        print(places[1][0], '|', places[1][1], '|', places[1][2])
        print('---------')
        print(places[2][0], '|', places[2][1], '|', places[2][2], '\n')

    for line in places :
         
         if line == ['X', 'X', 'X'] :
              winner = True
              print('Congratulations Player 1! You won!')

         if line == ['O', 'O', 'O'] :
              winner = True
              print('Congratulations Player 2! You won!')

    for w in range(len(places)) :

        if places[0][w] == 'X' and places[1][w] == 'X' and places[2][w] == 'X' :
            winner = True
            print('Congratulations Player 1! You won!')
            break

        if places[0][w] == 'O' and places[1][w] == 'O' and places[2][w] == 'O' :
            winner = True
            print('Congratulations Player 2! You won!')
            break

    if places[0][0] == 'X' and places[1][1] == 'X' and places[2][2] == 'X' :
         winner = True
         print('Congratulations Player 1! You won!')

    if places[0][0] == 'O' and places[1][1] == 'O' and places[2][2] == 'O' :
         winner = True
         print('Congratulations Player 2! You won!')
    
    if places[0][2] == 'X' and places[1][1] == 'X' and places[2][0] == 'X' :
        winner = True
        print('Congratulations Player 1! You won!')

    if places[0][2] == 'O' and places[1][1] == 'O' and places[2][0] == 'O' :
        winner = True
        print('Congratulations Player 2! You won!')

    if turn == 10 and not winner :
        print('It was a draw!')
        break

    if winner :
        break

