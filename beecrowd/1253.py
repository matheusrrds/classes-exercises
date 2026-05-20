n = int(input())

for _ in range(n) :
    codified_str = input()
    deslocation = int(input())
    word = ''

    for character in codified_str :

        if 65 > ord(character) - deslocation :

            word += chr(ord(character) - deslocation + 26)
        
        elif 90 < ord(character) - deslocation :

            word += chr(ord(character) - deslocation - 26)

        else :
            word += chr(ord(character) - deslocation)
    
    print(word)

