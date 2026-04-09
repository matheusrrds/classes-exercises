alcohol = 0
gasoline = 0
diesel = 0

while True :
    vote = int(input())

    if vote == 1 :
        alcohol += 1

    elif vote == 2 :
        gasoline += 1
    
    elif vote == 3 :
        diesel += 1
    
    elif vote == 4 :
        break

print("MUITO OBRIGADO")
print(f'Alcool: {alcohol}')
print(f'Gasolina: {gasoline}')
print(f'Diesel: {diesel}')
