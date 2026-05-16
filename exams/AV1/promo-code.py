string = input()
price = float(input())

final_price = price
promo_activated = False
continue_program = True
ultimo_numero_par = False
word = ''

for i in range(5) :

    word += string[i]

for character in string :
    
    if ' ' == character :
        continue_program = False

if continue_program: 

    try: 
        ultimo_numero_par = (int(string[-1]) % 2 == 0)
    except :
        continue_program = False

if continue_program and ultimo_numero_par and word == 'PROMO' :
    promo_activated = True

if promo_activated :
    final_price *= 0.8
    print(f'Código válido! O valor final com desconto é R$ {final_price:.2f}')
else :
    print(f'Código inválido! O valor final é R$ {final_price:.2f}')