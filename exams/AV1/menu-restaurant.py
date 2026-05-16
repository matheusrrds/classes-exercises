menu = {}
wishlist = []
missing_products = []

total_sum = 0

n = int(input())

for _ in range(n) :
    
    product, price = input().split(',')
    price = float(price)

    menu[product] = price

p = int(input())

for _ in range(p) :
    wishlist.append(input())

for wish_product in wishlist :

    try :
        total_sum += menu[wish_product]
    except :
        missing_products.append(wish_product)

for missing in missing_products :
    print(f"Aviso: '{missing}' não encontrado no cardápio")

print(f'Total a pagar: R$ {total_sum:.2f}')