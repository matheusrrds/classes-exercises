n = int(input())
grades = list(map(int, input().split()))

grades_frequency = {}

most_frequent = 0

for grade in grades :
    grades_frequency[grade] = 0

for grade in grades :
    grades_frequency[grade] += 1

for grade in grades :

    if grades_frequency[grade] > most_frequent :
        most_frequent = grades_frequency[grade]
        answer = grade
    
    elif grades_frequency[grade] == most_frequent :
        most_frequent = grades_frequency[grade]

        if answer < grade :
            answer = grade

print(answer)

