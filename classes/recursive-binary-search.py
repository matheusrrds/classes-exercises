def rec_binarysearch(ordened_list, value, begin=0, end=None) :

    if end is None :
        end = len(ordened_list) - 1

    if begin > end :
        return -1

    m = (begin+end) // 2

    if ordened_list[m] == value :
        return m
    
    elif ordened_list[m] > value :
        return rec_binarysearch(ordened_list, value, begin, m-1)
    
    else :
        return rec_binarysearch(ordened_list, value, m+1, end)

print(rec_binarysearch([1, 2, 3, 4, 5], 4))




