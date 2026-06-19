n = int(input())
andares = input().split()

max_dist_i = 1
dist_i = 1

dist_total = 1
max_dist = 1

for i in range(len(andares)) :
    dist_i = int(andares[i]) - i
    
    if dist_i > max_dist_i :
        max_dist_i = dist_i

for j in range(len(andares)) :
    dist_total = int(andares[j]) + j + max_dist_i
    
    if dist_total > max_dist :
        max_dist = dist_total

print(max_dist)

