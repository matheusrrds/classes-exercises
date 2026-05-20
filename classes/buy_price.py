def buy_price(total_price, ship_tax=15.99, discount=0) :
    """ 
    the function receives a ship tax value and a discount and computes
    the total price of the buy.
           
    parameters :
    - ship_tax (float): the price of the ship tax
    - discount (float): the discount in float

    return : total buy price (float).
        
    """

    buy_price = (total_price + ship_tax) - discount*total_price
    return print(f'{buy_price:.2f}')

buy_price(100)
buy_price(100, discount=0.1)
buy_price(399.90, ship_tax=0)
buy_price(990.01, 0, 0.15)
