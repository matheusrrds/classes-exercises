e = int(input())
s = int(input())
l = int(input())

total_distance = abs(e-s) + abs(s-l) + abs(e-l)
print(total_distance)