n = int(input())
heights = list(map(int, input().split()))
highest_student = heights[-1]
cheating = 0

for i in range(len(heights) - 2, -1, -1) :

    if heights[i] > highest_student :
        highest_student = heights[i]
    else :
        cheating += 1

print(cheating)


    

