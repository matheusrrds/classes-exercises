hours = int(input())
speed = int(input())
distance = hours * speed
fuel_needed = distance / 12 
print(f'{fuel_needed:.3f}')