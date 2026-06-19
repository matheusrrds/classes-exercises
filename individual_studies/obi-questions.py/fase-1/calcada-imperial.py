from itertools import combinations

n = int(input())
sequence = [int(input()) for _ in range(n)]

greatest = 1

for a,b in combinations(set(sequence), 2) :
    
    subseq = []

    for x in sequence :

        if x == a or x == b :

            if not subseq :
                subseq.append(x)
            else :
                if x != subseq[-1] :
                    subseq.append(x)
        
    greatest = max(greatest, len(subseq))

print(greatest)
            


    