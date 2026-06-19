n = int(input())
values = []
operations = []

i = 0
current_result = 0

for _ in range(n) :
    value, operation = input().split()

    values.append(int(value))
    operations.append(operation)

for i in range(len(values)) :

    if i == 0 :
        if operations[i] == '*' :
            current_result += 1*values[i]
            continue
        else :
            current_result += 1/values[i]
            continue
    
    if operations[i] == '*' :
        current_result *= values[i]
    else :
        current_result /= values[i]
       
print(f'{current_result:.0f}')



