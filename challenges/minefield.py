# Exercício 2 - Campo Minado
# Você vai programar parte do jogo Campo Minado. Considere que o módulo de geração de
# bombas já está pronto e entrega a você uma grade com a posição de todas as minas. Sua
# tarefa agora é gerar o "mapa de dicas": para cada espaço vazio no campo, você deve
# calcular quantas bombas existem exatamente ao redor dele (considerando as 8 direções:
# horizontais, verticais e diagonais).

# Entrada:
# ● A primeira linha contém dois números inteiros, L e C, indicando o número de linhas e
# colunas da grade.
# ● As próximas L linhas contêm, cada uma, uma string de C caracteres.
# ● Um asterisco * representa uma bomba.
# ● Um ponto . representa um espaço seguro.

# Saída:
# O programa deve imprimir a grade que representa o campo minado, mantendo as bombas *
# em seus lugares originais. Porém, todos os pontos . devem ser substituídos por um número
# de 0 a 8, indicando a quantidade de bombas adjacentes àquela célula.

# MATHEUS RAMOS RODRIGUES

lines, columns = map(int, input().split())
minefield = []
safe_indices = []
danger_indices = []
bomb = 0

for line in range(lines) :
    minefield.append(input())

for k in range(lines) :
    for i in range(columns) :
        if minefield[k][i] == '.' :
            safe_indices.append((k,i))

for k in range(lines) :
    for i in range(columns) :
        if minefield[k][i] == '*' :
            danger_indices.append((k,i))

for safe_par in safe_indices :

    if (safe_par[0], safe_par[1] - 1) in danger_indices :
        bomb += 1
    
    if (safe_par[0], safe_par[1] + 1) in danger_indices :
        bomb += 1

    if (safe_par[0] - 1, safe_par[1]) in danger_indices :
        bomb += 1

    if (safe_par[0] + 1, safe_par[1]) in danger_indices :
        bomb += 1

    if (safe_par[0] - 1, safe_par[1] - 1) in danger_indices :
        bomb += 1
    
    if (safe_par[0] - 1, safe_par[1] + 1) in danger_indices :
        bomb += 1

    if (safe_par[0] + 1, safe_par[1] - 1) in danger_indices :
        bomb += 1

    if (safe_par[0] + 1, safe_par[1] + 1) in danger_indices :
        bomb += 1

    minefield[safe_par[0]] = minefield[safe_par[0]].replace('.', f'{bomb}', 1)
    bomb = 0

for u in range(len(minefield)) :
    print('\n', minefield[u], sep='')
