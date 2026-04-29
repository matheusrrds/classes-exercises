test_cases = int(input())
roots = []
indices_roots = []

left_subtree = ''
left_root_i = 9999
right_subtree = ''
right_root_i = 9999
subtree_final = ''

elements, pre_order, in_order = input().split()
elements = int(elements)

roots.append(pre_order[0])

for i in range(elements) :

    if in_order[i] == roots[0] :
        indices_roots.append(i) 

for l in range(elements) :

    if indices_roots[0] > l :
        left_subtree += in_order[l]

    elif indices_roots[0] < l :
        right_subtree += in_order[l]

for k in range(len(left_subtree)) :
    if pre_order.index(left_subtree[k]) < left_root_i :
        left_root_i = pre_order.index(left_subtree[k])

for w in range(len(right_subtree)) :
    if pre_order.index(right_subtree[w]) < right_root_i :
        right_root_i = pre_order.index(right_subtree[w])

i = left_subtree.find(pre_order[left_root_i])

if i != -1 :
    left_subtree = left_subtree[:i] + left_subtree[1+i:] + pre_order[left_root_i]

j = right_subtree.find(pre_order[right_root_i])

if j != -1 :
    right_subtree = right_subtree[:j] + right_subtree[1+j:] + pre_order[right_root_i]

subtree_final = left_subtree + right_subtree + pre_order[0]
print(subtree_final)

# FAILED - Não consegui ainda..
