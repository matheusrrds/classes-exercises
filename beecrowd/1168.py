n = int(input())
summ = 0
dicionario = {'1': 2, '2': 5,'3': 5, '4': 4, '5': 5, '6': 6, '7': 3, '8': 7, '9': 6, '0': 6}


for i in range(n):
    leds_numero = input()
    
    for algarism in leds_numero :
        summ += dicionario[algarism]
        
    print(f'{summ} leds')
    summ = 0

