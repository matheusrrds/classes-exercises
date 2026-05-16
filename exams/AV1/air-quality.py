medicao_valida = 0
niveis_criticos = 0
qualidades_ar = []

while True :
    num = float(input())

    if num < 0 :
        break
    else :
        medicao_valida += 1 
    
    if num > 50.0 :
        niveis_criticos += 1
    
    qualidades_ar.append(num)

verificacao = len(qualidades_ar)

try :
    average = sum(qualidades_ar) / len(qualidades_ar)
except :
    verificacao = 0

if verificacao > 0 :
    print(f'Foram registradas {medicao_valida} medições válidas')
    print(f'Média de poluição: {average:.2f}')
    print(f'Níveis críticos (> 50.0) detectados: {niveis_criticos} vezes')
else:
    print('Nenhuma medição registrada')