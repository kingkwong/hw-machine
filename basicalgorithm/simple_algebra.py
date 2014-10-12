def algebra(operation, a, b):
    if (str(operation) == 'ADD'):
        x = a + b
    if (str(operation) == 'SUB'):
        c = -b
        x = a + c
    if (str(operation) == 'MULT'):
        x = a * b
    if (str(operation) == 'DIV'):
        x = a / b
    print (x)
