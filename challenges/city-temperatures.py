# Questão 1: Análise Meteorológica
# Uma estação meteorológica registra as temperaturas diárias de várias cidades ao longo de uma semana (7 dias). Você deve desenvolver um programa que
# processe essas informações para identificar a cidade com a maior temperatura média na semana e contar, para cada cidade, quantos dias registraram
# temperaturas acima de um limite especificado.
# Formato da Entrada:
# 1. Um número inteiro N indicando a quantidade de cidades analisadas.
# 2. Nas N linhas seguintes, uma string contendo o nome da cidade seguido por 7 números reais (representando as temperaturas da semana). Todos os
# dados na linha estarão separados por vírgulas.
# 3. Na última linha da entrada, um número real representa a temperatura limite.
# Formato da Saída:
# ● Para cada cidade lida, o programa deve imprimir uma linha com o formato:
# {cidade} teve {dias} dias com temperatura acima de {limite}°C.
# ● Ao final do processamento, o programa deve imprimir a conclusão no formato:
# A cidade com a maior média foi {cidade} com {media}°C. (Nota: a média deve ser arredondada para duas casas decimais)

n = int(input())

city_data = []
city_names = []
temperatures = []
averages = []

total_sum = 0
greatest_average = -100.0

for _ in range(n) :
    city_data.append(input().split(','))

limit = float(input())

for city in city_data :
    first_iteration = True

    for data in city :

        if first_iteration :
            city_names.append(data)
            first_iteration = False
        else :
            temperatures.append(float(data))

for j in range(n) :
    above_limit = 0
    total_sum = 0
    current_average = 0

    for k in range(7*j, 7*j + 7) :

        if temperatures[k] > limit :
            above_limit += 1
        
        total_sum += temperatures[k]

    current_average = total_sum / 7
    
    if current_average > greatest_average :
        greatest_average = current_average
        indice_name = j
    
    print(f'{city_names[j]} teve {above_limit} dias com temperatura acima de {limit:.1f}°C.')

print(f'A cidade com a maior média foi {city_names[indice_name]} com {greatest_average:.2f}°C')

# Rio de Janeiro teve 5 dias com temperatura acima de 30.0°C.
# Curitiba teve 0 dias com temperatura acima de 30.0°C.
# A cidade com a maior média foi Rio de Janeiro com 31.44°C.






