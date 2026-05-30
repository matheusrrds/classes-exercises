n, m = map(int, input().split()) 

postos = list(map(int, input().split()))
stop = False

for i in range(len(postos)-1) :

    if postos[i+1] - postos[i] > m :
        print('N')
        stop = True
        break

if not stop and 42195 - postos[-1] > m :
    print('N')
    stop = True

if not stop :
    print('S')





