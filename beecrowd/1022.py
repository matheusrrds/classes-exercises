import math 

n = int(input())
phrase = []

for i in range(n) :

    sentence = input().split()
    n1, first_bar, d1, operator, n2, second_bar, d2 = sentence

    match operator :

        case '+' :
            sum_numerator = int(n1) * int(d2) + int(n2) * int(d1)
            sum_denominator = int(d1) * int(d2)

            if sum_denominator < 0 :

                sum_denominator *= -1
                sum_numerator *= -1

            sum_fraction = f'{sum_numerator}/{sum_denominator}'


            mdc_sum = math.gcd(sum_numerator, sum_denominator)

            sum_numerator //= mdc_sum
            sum_denominator //= mdc_sum

            sum_fraction_simplified = f'{sum_numerator}/{sum_denominator}'

            phrase.append(f'{sum_fraction} = {sum_fraction_simplified}')

        case '-' :
            sub_numerator = int(n1) * int(d2) - int(n2) * int(d1)
            sub_denominator = int(d1) * int(d2)

            if sub_denominator < 0 :

                sub_denominator *= -1
                sub_numerator *= -1

            sub_fraction = f'{sub_numerator}/{sub_denominator}'


            mdc_sub = math.gcd(sub_numerator, sub_denominator)

            sub_numerator //= mdc_sub
            sub_denominator //= mdc_sub

            sub_fraction_simplified = f'{sub_numerator}/{sub_denominator}'

            phrase.append(f'{sub_fraction} = {sub_fraction_simplified}')


        case '*' :
            multplic_numerator = int(n1) * int(n2)
            multplic_denominator = int(d1) * int(d2)

            if multplic_denominator < 0 :

                multplic_denominator *= -1
                multplic_numerator *= -1

            multplic_fraction = f'{multplic_numerator}/{multplic_denominator}'

            mdc_multplic = math.gcd(multplic_numerator, multplic_denominator)

            multplic_numerator //= mdc_multplic
            multplic_denominator //= mdc_multplic

            multplic_fraction_simplified = f'{multplic_numerator}/{multplic_denominator}'

            phrase.append(f'{multplic_fraction} = {multplic_fraction_simplified}')


        case '/' :
            division_numerator = int(n1) * int(d2)
            division_denominator = int(d1) * int(n2)

            if division_denominator < 0 :

                division_denominator *= -1
                division_numerator *= -1

            division_fraction = f'{division_numerator}/{division_denominator}'


            mdc_division = math.gcd(division_numerator, division_denominator)

            division_numerator //= mdc_division
            division_denominator //= mdc_division

            division_fraction_simplified = f'{division_numerator}/{division_denominator}'

            phrase.append(f'{division_fraction} = {division_fraction_simplified}')

    if i == (n-1) :
        for l in range(n) :
            print(phrase[l])


