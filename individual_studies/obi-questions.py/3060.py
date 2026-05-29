v = int(input())
p = int(input())

if v % p == 0 :
    for _ in range(p) :
        print(v//p)
else :
    r = v % p

    for _ in range(r) :

        print((v//p) + 1)
    
    for _ in range(p-r) :
        print((v//p))
        