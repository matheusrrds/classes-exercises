n, k = map(int, input().split())
notas = list(map(int, input().split()))
notas.sort()

aprovados = []

for i in range(len(notas) -1, len(notas)-k-1, -1) :
    aprovados.append(notas[i])

print(min(aprovados))


