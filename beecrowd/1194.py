test_cases = int(input())

for n in range(test_cases) :
    n, tree_1, tree_2 = input().split()
    n = int(n)

    root = tree_1[0]

    left_most = tree_2[0]
    right_most = tree_1[-1]

print()