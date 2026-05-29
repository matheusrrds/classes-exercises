n, f = map(int, input().split())
cicles = list(map(int, input().split()))

capsulas_ciclos = {}
capsulas_num = {}

mmc = 1
summation = 0

# aproximação: 42f / 41 <= x

for i in range(1, n+1) :
    capsulas_ciclos[i] = cicles[i-1]
    mmc *= capsulas_ciclos[i]

for i in range(1, n+1) :
    capsulas_num[i] = round(mmc / capsulas_ciclos[i])

    summation += capsulas_num[i]

result_aproximado = int(mmc*f / summation)

while True :
    somatory = 0

    for i in range(1, n+1) :

        somatory += (result_aproximado // capsulas_ciclos[i])
    
    if somatory >= f :
        print(result_aproximado)
        break
    else :
        result_aproximado += 1
        continue

    
# num = mmc/3 + num2 = mmc/7  + num3 = mmc/ 2   

# x/3 + x/7 + x/2 >= f

# funciona mas TEMPO EXCEDIDO NESSA SOLUÇÃO :/