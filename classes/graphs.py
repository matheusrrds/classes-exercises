n = int(input())
vertices = []
arestas = []

for i in range(1, n + 1) :
    vertices.append(i)

print(vertices)

for j in range(len(vertices)) :

    arestas.append([vertices[j]])

for k in range(len(vertices)) :

    for l in range(len(vertices)) :

        if vertices[k] < vertices[l] :

            arestas.append([vertices[k], vertices[l]])

print(arestas)