l = int(input())
c = int(input())

temperatures = []
total_sum = 0
above_average = 0

for i in range(l) :

    temperatures.append(input().split())

    for k in range(c) :

        temperatures[i][k] = float(temperatures[i][k])
        total_sum += temperatures[i][k] 

average = total_sum / (l*c)

for temperature_list in temperatures :
    
    for temperature in temperature_list :

        if temperature > average :

            above_average += 1

print(f'Temperatura média da fazenda: {average:.2f}°C')
print(f'Setores em risco (acima da média): {above_average}')