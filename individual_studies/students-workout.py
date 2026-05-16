n = int(input())

students_total_exercises = {}
students_average_exercises = {}
students_goal_achieved = {}
numbers_exercises = {}

greatest_num_exercises = 0
greatest_average = 0
greatest_name = ''

for _ in range(n) :

    name, value1, value2, value3, value4, value5, value6, value7 = input().split(',')
    numbers_exercises[name] = [float(value1), float(value2), float(value3), float(value4), float(value5), float(value6), float(value7)]

    total_exercises = float(value1) + float(value2) + float(value3) + float(value4) + float(value5) + float(value6) + float(value7)

    students_total_exercises[name] = total_exercises
    students_average_exercises[name] = total_exercises / 7

    if students_total_exercises[name] > greatest_num_exercises :
        greatest_num_exercises = students_total_exercises[name]
        greatest_name = name
    
    if students_average_exercises[name] > greatest_average :
        greatest_average = students_average_exercises[name]
        greatest_average_name = name

daily_goal = int(input())

for name in numbers_exercises :
    
    goal_achieved = 0
    
    for i in range(len(numbers_exercises[name])) :

        if numbers_exercises[name][i] > daily_goal :

            goal_achieved += 1
    
    students_goal_achieved[name] = goal_achieved



    
for name in students_total_exercises :

    print(f'{name} realizou {students_total_exercises[name]:.0f} exercícios na semana.')
    print(f'Média semanal: {students_average_exercises[name]:.2f}')
    print(f'Dias acima da meta: {students_goal_achieved[name]}')
    print()
    
print(f'Maior total semanal: {greatest_name} com {greatest_num_exercises:.0f} exercícios')
print(f'Maior média semanal: {greatest_average_name} com média {greatest_average:.2f}.')


