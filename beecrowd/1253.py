n = int(input())

for _ in range(n) :
    codified_str = input()
    deslocation = int(input())
    word = ''

    for character in codified_str :

        if 64 < ord(character) - deslocation < 91 :

            word += chr(ord(character) - deslocation)

    
    print(word)