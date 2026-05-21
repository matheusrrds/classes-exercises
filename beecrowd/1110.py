while True :
    n = int(input())

    if n == 0 :
        break

    deck = []
    discarteds = []

    remaining_cards = 0
    counter = 0

    for card in range(1, n+1) :
        deck.append(card)
    
    deck.sort()

    while len(deck) > 1 :
        discarteds.append(deck.pop(0))
        deck.insert(len(deck), deck[0])
        deck.pop(0)


    counter = len(discarteds)

    print(f'Discarded cards: ', end='')

    for card in discarteds :

        counter -= 1

        if counter > 0 :
            print(f'{card}', end=', ')
        else :
            print(f'{card}', end='\n')

    print(f'Remaining card: ', end='')
    print(f'{deck[0]}')

    



