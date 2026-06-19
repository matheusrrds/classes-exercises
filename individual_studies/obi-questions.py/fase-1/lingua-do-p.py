entrance = input()
counter = 1
    
for letter in entrance :

    if letter != ' ' :
        counter += 1

    if letter == 'p' and counter % 2 == 0 :
        continue

    print(letter, end='')   

print()