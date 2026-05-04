# After solving the IccanobiF case1, Fabiano decided to explore the Internet and find whether exists a real IccanobiF Sequence or not.

# During the exploration over Internet, he discovered the sequence but it's a little different: the result of each term suffers some kind of "mirror effect" if it has two or more digits. As long as the result would have the digits inverted, this would affect the sequence completed as long as it continues.

# Fabiano noticed that IccanobiF Sequence can grow even more than the ordinary Fibonacci Sequence and the number 1 doesn't repeat as expected. As long as this is a complex task for him, he decided to hire you to solve this case! It's up to you!

# Input
# This is one of End of File (EOF) cases. So many test cases, such wow.

# Input will have only one value X (X ∈ ℕ | X ≤ 60) which is the term of IccanobiF Sequence to be search.

# Output
# For each input, one output with the element of the term X informed of IccanobiF Sequence. After the exhibition of the value, a new line should be printed (as always).

n = int(input())
fibonacci = [1,1]
inverted_number_str = ''

if n == 1 :
    fibonacci.pop()

while n >= 3 :

    num_1 = fibonacci[0]
    num_2 = fibonacci[1]
    num_3 = str(num_1 + num_2)

    if len(num_3) > 1 :
        
        for i in range(-1, -len(num_3)) :
            inverted_number_str += num_3[i]

        num_3 = int(inverted_number_str)

    else :

        num_3 = int(num_3)

    fibonacci.insert(0, num_3)
    n -= 1

for k in range(len(fibonacci)) :
    print(fibonacci[k])

#ainda nao resolvido