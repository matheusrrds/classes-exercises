price = float(input())
cents = int(round(price * 100))

hundreds = cents // 10 ** 4
cents -= hundreds * 10 ** 4

fifties = cents // 5000
cents -= fifties * 5000

twenties = cents // 2000
cents -= twenties * 2000

tens = cents // 1000
cents -= tens * 1000

fives = cents // 500
cents -= fives * 500

twos = cents // 200
cents -= twos * 200

one_coins = cents // 100
cents -= one_coins * 100

half_coins = cents // 50
cents -= half_coins * 50

quarter_coins = cents // 25
cents -= quarter_coins * 25

decimal_coins = cents // 10
cents -= decimal_coins * 10

five_coins = cents // 5
cents -= five_coins * 5

one_cent = cents // 1


print('NOTAS:')
print(f'{hundreds:.0f} nota(s) de R$ 100.00')
print(f'{fifties:.0f} nota(s) de R$ 50.00')
print(f'{twenties:.0f} nota(s) de R$ 20.00')
print(f'{tens:.0f} nota(s) de R$ 10.00')
print(f'{fives:.0f} nota(s) de R$ 5.00')
print(f'{twos:.0f} nota(s) de R$ 2.00')

print('MOEDAS:')
print(f'{one_coins:.0f} moeda(s) de R$ 1.00')
print(f'{half_coins:.0f} moeda(s) de R$ 0.50')
print(f'{quarter_coins:.0f} moeda(s) de R$ 0.25')
print(f'{decimal_coins:.0f} moeda(s) de R$ 0.10')
print(f'{five_coins:.0f} moeda(s) de R$ 0.05')
print(f'{one_cent:.0f} moeda(s) de R$ 0.01')






