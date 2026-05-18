from time import time 

now = time()
days = now // (3600 * 24)

print(f'{days:.0f}')