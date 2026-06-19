sides = list(map(float, input().split()))
a,b,c = sides[0], sides[1], sides[2]
sides.sort()

for i in range(len(sides)-2) :

    if sides[i+2] < sides[i+1] + sides[i] :
        print(f'Perimetro = {sides[i+2]+sides[i+1]+sides[0]:.1f}')
        break
else :

    print(f'Area = {((a+b)*c)/2:.1f}')

    