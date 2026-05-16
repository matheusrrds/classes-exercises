def printing_verses(num_bottles) :
    if num_bottles > 1 :
        print(f'{num_bottles} bottles of beer on the wall')
        print(f'{num_bottles} bottles of beer')
        print('Take one down, pass it around')
        if num_bottles > 2 :
            print(f'{num_bottles-1} bottles on the wall')
        else :
            print(f'{num_bottles-1} bottle on the wall')
        print()
    else :
        print(f'{num_bottles} bottle of beer on the wall')
        print(f'{num_bottles} bottle of beer')
        print('Take one down, pass it around')
        print(f'{num_bottles-1} bottles on the wall')
        print()

def bottles_verses(num_bottles) :

    for num_bottles in range(num_bottles, 0, -1) :

        printing_verses(num_bottles)
            
n = int(input())

bottles_verses(n)