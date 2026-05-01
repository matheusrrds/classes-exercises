# Iccanobif sequences are sequences where each term is always equal to the sum of the next two subsequent to it. Except for the last two terms which are always equal to 1

# Example of an Iccanobif sequence with 10 terms: 55, 34, 21, 13, 8, 5, 3, 2, 1, 1.

# Your task is, given an integer value, print the corresponding size Iccanobif sequence.

# Input
# The entry consists of a single integer N (1 ≤ N ≤ 40) representing the size of the desired Iccanobif sequence.

# Output
# The output consists of a single line containing the terms of the Iccanobif sequence of N size separated by a single space.

n = int(input())
fibonacci = [1,1]

if n == 1 :
    fibonacci.pop()

while n >= 3 :

    num_1 = fibonacci[0]
    num_2 = fibonacci[1]

    fibonacci.insert(0, num_1 + num_2)
    n -= 1
    
print(*fibonacci)

