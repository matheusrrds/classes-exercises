phrase = input()
vowel = 0

for caracter in phrase :
    counter = caracter.lower()

    if counter == 'a' or counter == 'e' or counter == 'i' or counter == 'o' or counter == 'u':
        vowel += 1

print(vowel)