counter = 1

while True:
    n = int(input())

    if n == 0 :
        break

    total_j = 0
    total_z = 0

    differences = []

    for _ in range(n) :
        j, z = map(int, input().split())

        total_j += j
        total_z += z

        differences.append(total_j-total_z)

    print(f'Teste {counter}')
    for diff in differences :
        print(diff)
    
    print()
    counter += 1
    
