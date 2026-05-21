n = int(input())

even_numbers = []
odd_numbers = []

for _ in range(n) :
    number = int(input())

    if number % 2 == 0 :
        even_numbers.append(number)
    else :
        odd_numbers.append(number)

even_numbers.sort()
odd_numbers.sort()

for number in even_numbers :
    print(number)

for i in range(len(odd_numbers) - 1, -1, -1) :
    print(odd_numbers[i])



