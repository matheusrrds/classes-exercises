scores = [int(input()) for _ in range(5)]
scores.sort()

trofeus = 1
placas = 0

while len(scores) >= 2 and scores[-1] == scores[-2] :

    trofeus += 1

    scores.pop()

scores.pop()

if scores :
    placas += 1

while len(scores) >= 2 and scores[-1] == scores[-2] :

    placas += 1

    scores.pop()

print(trofeus, placas)





