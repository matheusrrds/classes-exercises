n = int(input())

teams_total_scores = {}
teams_averages = {}
teams_quantity_above_average = {}
matches = []

average_total = 0
greatest_average = 0

first_iteration = True

for _ in range(n) :

    team, p1,p2,p3,p4,p5,p6 = input().split(',')

    teams_total_scores[team] = float(p1) + float(p2) + float(p3) + float(p4) + float(p5) + float(p6)
    teams_averages[team] = teams_total_scores[team] / 6

    if first_iteration :
        lowest_average = teams_averages[team]
        first_iteration = False

    if teams_averages[team] > greatest_average :
        winner = team
        greatest_average = teams_averages[team]

    elif teams_averages[team] < lowest_average :
        loser = team
        lowest_average = teams_averages[team]


    matches.append([team, float(p1),float(p2),float(p3),float(p4),float(p5),float(p6)])

for team in teams_averages :
    average_total += teams_averages[team]

average_total /= len(teams_averages)

for teams_scores in matches :

    above_average = 0

    for i in range(len(teams_scores)) :
        if i != 0 :
            if teams_scores[i] > average_total :
                above_average += 1
                teams_quantity_above_average[teams_scores[0]] = above_average
            else : 
                teams_quantity_above_average[teams_scores[0]] = 0

for name in teams_total_scores :
    print(f'Equipe: {name}')
    print(f'Total: {teams_total_scores[name]:.1f}')
    print(f'Média: {teams_averages[name]:.2f}')

    if name in teams_quantity_above_average :
        print(f'Partidas acima da média geral: {teams_quantity_above_average[name]}')

print(f'Equipe campeã: {winner}')
print(f'Pior equipe: {loser}')
print(f'Média geral das equipes: {average_total:.2f}')


