a = int(input())
b = int(input())
if a < b :
    a = b
    b = int(input())
    if a < b and b % 2 == 0 :
        print(f'O maior número entre os 3 é: {b} e ele é par')
    if a < b and b % 2 != 0 :
        print(f'O maior número entre os 3 é: {b} e ele é ímpar')
    if a > b and a % 2 == 0 :
        print(f'O maior número entre os 3 é: {a} e ele é par')
    if a > b and a % 2 != 0 :
        print(f'O maior número entre os 3 é: {a} e ele é ímpar')
else :
    b = a
    a = int(input())
    if b < a and a % 2 == 0 :
        print(f'O maior número entre os 3 é: {a} e ele é par')
    if b < a and a % 2 != 0 :
        print(f'O maior número entre os 3 é: {a} e ele é ímpar')
    if b > a and b % 2 == 0 :
        print(f'O maior número entre os 3 é: {b} e ele é ímpar')
    if b > a and b % 2 != 0 :
        print(f'O maior número entre os 3 é: {b} e ele é par')

        ## errado
