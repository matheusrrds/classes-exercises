def entrada_caixas(quantity) :
    boxes = []
    for i in range(quantity) :
        boxes.append(input().split())

    for j in range(quantity) :
        boxes[j].pop(0)
    
    for box in boxes :
        for i in range(len(box)) :
            box[i] = int(box[i])

    return boxes

def is_ordened_intern(boxes) :
    
    for box in boxes :
        for i in range(len(box) - 1) :
            if box[i] > box[i+1] :
                return False
    
    return True

def is_ordened_extern(boxes) :
    for i in range(len(boxes)-1) :
        if boxes[i][-1] > boxes[i+1][0] : 
            return False
    return True

n = int(input())
caixas = entrada_caixas(n)
caixas.sort()

if is_ordened_intern(caixas) :
    if is_ordened_extern(caixas) :
        print('YES')
    else :
        print('NO')
else :
    print('NO')

