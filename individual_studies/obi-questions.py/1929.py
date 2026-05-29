h = list(map(int, input().split()))

case1 = [int(h[0]), int(h[1]), int(h[2])]
case2 = [int(h[1]), int(h[2]), int(h[3])]
case3 = [int(h[0]), int(h[2]), int(h[3])]
case4 = [int(h[0]), int(h[1]), int(h[3])]

max1 = max(case1)
max2 = max(case2)
max3 = max(case3)
max4 = max(case4)

case1.remove(max1)
case2.remove(max2)
case3.remove(max3)
case4.remove(max4)

if max1 < sum(case1) or max2 < sum(case2) or max3 < sum(case3) or max4 < sum(case4):
    print('S')
else :
    print('N')




