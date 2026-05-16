def print_right(string) :
    missing = 40 - len(string)

    if missing > 0 :
        string = ' ' * missing + string

    print(string)

print_right('Monty')
print_right("Python's")
print_right('Flying circus')