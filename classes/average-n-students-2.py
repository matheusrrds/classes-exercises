grades = list(map(float, input().split()))
approveds = []
n = len(grades)

for i in range(n) :

    if grades[i] >= 6.0 :

        approveds.append(grades[i])

print('As notas dos aprovados foram:')

for aproved_grade in approveds :

    print(aproved_grade, end=' ')