a, b, c = list(map(int, input().split()))
maiorAB = int((a+b+abs(a-b)) / 2)
greatest = int((maiorAB + c + abs(maiorAB - c)) / 2)
print(f'{greatest} eh o maior')

