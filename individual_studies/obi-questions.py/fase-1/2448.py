n, m = map(int, input().split())
time_spent = 0
current_place = 0

house_numbers = list(map(int, input().split()))
order_numbers = list(map(int, input().split()))

dicionario = {}

for i in range(len(house_numbers)) :

    dicionario[house_numbers[i]] = i

for order in order_numbers :
    index = dicionario[order]

    time_spent += abs((index) - current_place)
    current_place = index

print(time_spent)
