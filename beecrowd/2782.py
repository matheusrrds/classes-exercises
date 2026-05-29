n = int(input())
steps = input().split()
different_steps = []

for i in range(len(steps)-1) :

    difference = int(steps[i]) - int(steps[i+1])

    if i == 0 :
        different_steps.append(difference)
        continue
 
    if difference != different_steps[-1] :
        different_steps.append(difference)

if len(different_steps) != 0 :

    print(len(different_steps))

else :
    print(1)