i = 0
while True :
    i += 1

    r = int(input())

    if r == 0 :
        break
    
    stickers_turneds = {
        'Aldo': 0,
        'Beto': 0,
    }

    for _ in range(r) :
        a, b = map(int, input().split())

        stickers_turneds['Aldo'] += a
        stickers_turneds['Beto'] += b
    
    print(f'Teste {i}')

    if stickers_turneds['Aldo'] > stickers_turneds['Beto'] :
        print('Aldo')
        print()
    else :
        print('Beto')
        print()

    


