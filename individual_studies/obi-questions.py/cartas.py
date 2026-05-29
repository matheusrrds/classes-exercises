cards = list(map(int, input().split()))
decreasing = 0
increasing = 0

for i in range(4) :
    if cards[i] < cards[i+1] :
        increasing += 1
    elif cards[i] > cards[i+1] :
        decreasing += 1 

if increasing == 4 :
    print('C')
elif decreasing == 4 :
    print('D')
else :
    print('N')