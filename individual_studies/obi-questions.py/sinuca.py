n = int(input())
firstln = list(map(int, input().split()))

actual_line = firstln

for _ in range(n-1) :

    new_line = []

    for i in range(len(actual_line)-1) :

        if actual_line[i] != actual_line[i+1] :

            new_line.append(-1)

        else :

            new_line.append(1)
    
    actual_line = new_line

if actual_line[0] == -1 :
    print('branca')
else :
    print('preta')
    










