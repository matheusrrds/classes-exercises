n, k = map(int, input().split())
sequence = list(map(int, input().split()))
count = 0

left = 0
right = 0

while left < n and right < n :

    rectangle = sequence[left:right+1]
    soma = sum(rectangle)

    if soma < k :
        right += 1

    elif soma > k :

        left += 1
        right = left

    elif soma == k :
        
        count += 1

        try :

            if sequence[right+1] == 0:
                right += 1

            else :
                
                left += 1
                right = left
        
        except :

            left += 1
            right = left


print(count)