n = int(input())
hortifrut_list = {}
price = 0

for test_case in range(n): 
    
    m = int(input())
    
    for product in range(m):
        fruit_name, fruit_price = input().split()
        hortifrut_list[fruit_name] = float(fruit_price)
    
    w = int(input())
    
    for wish_lists in range(w) :
        name_wish, quantity_wish = input().split()
        quantity_wish = int(quantity_wish)
        
        price += hortifrut_list[name_wish]  * quantity_wish

    print(f'R$ {price:.2f}')
    price = 0

