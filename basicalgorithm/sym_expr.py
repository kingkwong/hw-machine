def algebra(expr):
    list_expr = expr.split()
    a = int(list_expr[0])
    b = int(list_expr[2])
    c = -b
    if ((list_expr[1] == '*') | (list_expr[1] == '/')):
        if (list_expr[1] == '*'):
            x = a * b
            print(x)
        if (list_expr[1] == '/'):
            x = a / b
            print(x)
    if ((list_expr[1] == '+') | (list_expr[1] == '-')):
        if (list_expr[1] == '+'):
            x = a + b
            print(x)
        if (list_expr[1] == '-'):
            x = a + c
            print(x)
    else:
        pass
