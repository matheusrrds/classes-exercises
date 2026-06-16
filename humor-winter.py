a,b,c = map(int, input().split())

if a > b and b <= c :
    print(':)')
elif a < b and b >= c :
    print(':(')
elif a < b < c and abs(c-b) < abs(b-a) :
    print(':(')
elif a < b < c and abs(c-b) >= abs(b-a) :
    print(':)')
elif a > b > c and abs(b-a) > abs(b-c) :
    print(':)')
elif a > b > c and abs(b-a) <= abs(b-c) :
    print(':(')
elif a == b and b < c :
    print(':)')
else :
    print(':(')