# MATHEUS RAMOS RODRIGUES DE SOUZA

price = float(input())
cents = price * 100

coin_50 = cents // 50
cents -= (coin_50 * 50)
          

coin_25 = cents // 25
cents -= (coin_25 * 25)

coin_10 = cents // 10
cents -= (coin_10 * 10)

coin_5 = cents // 5
cents -= (coin_5 * 5)

coin_1 = cents // 1

print(f'Dado o valor: {price} devemos retornar {coin_50:.0f} moeda(s) de 50 centavos, {coin_25:.0f} moeda(s) de 25 centavos, {coin_10:.0f} moeda(s) de 10 centavos, {coin_5:.0f} moeda(s) de 5 centavos e {coin_1:.0f} moeda(s) de 1 centavo.')
