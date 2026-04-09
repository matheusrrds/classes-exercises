number_first = int(input())

notas_de_100 = number_first // 100
number_second = number_first - (notas_de_100 * 100)

notas_de_50 = number_second // 50
number_third = number_second - (notas_de_50 * 50)

notas_de_20 = number_third // 20
number_fourth = number_third - (notas_de_20 * 20)

notas_de_10 = number_fourth // 10
number_fifth = number_fourth - (notas_de_10 * 10)

notas_de_5 = number_fifth // 5
number_sixth = number_fifth - (notas_de_5 * 5)

notas_de_2 = number_sixth // 2
number_seventh = number_sixth - (notas_de_2 * 2)

notas_de_1 = number_seventh // 1
number_eighth = number_seventh - (notas_de_1 * 1)

print(number_first)
print(f'{notas_de_100} nota(s) de R$ 100,00')
print(f'{notas_de_50} nota(s) de R$ 50,00')
print(f'{notas_de_20} nota(s) de R$ 20,00')
print(f'{notas_de_10} nota(s) de R$ 10,00')
print(f'{notas_de_5} nota(s) de R$ 5,00')
print(f'{notas_de_2} nota(s) de R$ 2,00')
print(f'{notas_de_1} nota(s) de R$ 1,00')

