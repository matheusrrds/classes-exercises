# Due to the continuous drought that happened recently in some regions of Brazil, the Federal Government created an agency to assess the consumption of these regions in order to verify the behavior of the population at the time of rationing. This agency will take some cities (for sampling) and it will verify the consumption of each of the townspeople and the average consumption per inhabitant of each town.

# Input
# The input contains a number of test's cases. The first line of each case of test contains an integer N (1 ≤ N ≤ 1 * 10 6), indicating the amount of properties. The following N lines contains a pair of values X (1 ≤ X ≤ 10) and Y ( 1 ≤ Y ≤ 200) indicating the number of residents of each property and its total consumption (m3). Surely, no residence consumes more than 200 m3 per month. The input's end is represented by zero.

# Output
# For each case of test you must present the message “Cidade# n:”, where n is the number of the city in the sequence (1, 2, 3, ...), and then you must list in ascending order of consumption, the people's amount followed by a hyphen and the consumption of these people, rounding the value down. In the third line of output you should present the consumption per person in that town, with two decimal places without rounding, considering the total real consumption. Print a blank line between two consecutives test's cases. There is no blank line at the end of output.      

# STILL UNDER DEVELOPMENT, NOT DONE YET

city = 0
times_execution = 0
amount_people = 0
consumption = 0
teams = 0
pares_list = []
pares = []


while True :

    n = int(input())
    teams += n

    if not n == 0 :
        city += 1
        times_execution += 1

    if n == 0 :
        for number in range(1, city + 1) :
        
            print(f'Cidade# {number}:')

            for j in range(len(pares_list)) :

                for k in range(times_execution) :

                    print(f'{pares_list[j][k][0]}-{pares_list[j][k][1] // pares_list[j][k][0]}', end=' ')
                    
                    consumption += (pares_list[j][k][1])
                    amount_people += (pares_list[j][k][0])
            
                    print(f'\nConsumo medio: {consumption / amount_people:.2f} m3.\n')

    for i in range(n) :
        x, y = map(int, input().split())
        pares.append((x,y))

    pares_list.append(pares) 
    pares = []



