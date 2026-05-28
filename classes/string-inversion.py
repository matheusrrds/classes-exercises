def inverted_str(string, i=-1) :
    if len(string) == 0 :
        return ''
    
    return string[i] + inverted_str(string[:-1])

print(inverted_str('peido'))