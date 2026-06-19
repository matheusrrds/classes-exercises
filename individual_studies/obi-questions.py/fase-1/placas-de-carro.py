placa = input()
answer_given = False
stop = False

while True :

    if len(placa) != 8 :
        break

    if placa[3] != '-' :
        break

    for i in range(3) :
        if not placa[i].isupper():
            stop = True
                
    for j in range(4, 8) :
        if not placa[j].isnumeric() :
            stop = True
    
    if stop :
        break

    answer_given = True
    print(1)
    break

if not answer_given :

    stop = False

    while True:

        if len(placa) != 7 :
            break

        if not placa[3].isnumeric() :
            break

        for l in range(len(placa)-1, len(placa)-3, -1) :
            if not placa[l].isnumeric() :
                stop = True

        if not placa[4].isupper() :
            break

        for k in range(3) :
            if not placa[k].isupper() :
                stop = True

        if stop :
            break
        
        answer_given = True
        print(2)
        break

if not answer_given :
    print(0)

