n = int(input())

for _ in range(n) :
    founds = input()
    symbols = []
    diamond = 0

    symbols.extend(founds)

    while '.' in symbols :
        symbols.remove('.')

    while '<' in symbols and '>' in symbols :
        symbols.remove('<')

        try :
            i = len(symbols) - 1 - symbols[::-1].index('>')
            symbols.pop(i)
        except :
            break

        diamond += 1

    print(diamond)