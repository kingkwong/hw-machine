def algebra(expr):
    #splitting input string into list
    list_expr = expr.split()
    num_list = []
    #finding positions of operators
    for i, item in enumerate(list_expr):
        if (item == '*' or item == '/'):
            num_list.extend(str(i))
    for i, item in enumerate(list_expr):
        if (item == '+' or item == '-'):
            num_list.extend(str(i))
    print(num_list) #bugtest: print out indexes of operators
    #defining numbers to operate
    a = int(list_expr[int(num_list[0]) - 1])
    b = int(list_expr[int(num_list[0]) + 1])
    c = -b
    #first operation
    if ((list_expr[int(num_list[0])] == '*') | (list_expr[int(num_list[0])] == '/')):
        if (list_expr[int(num_list[0])] == '*'):
            x = a * b
            print(x)
        if (list_expr[int(num_list[0])] == '/'):
            x = a / b
            print(x)
    if ((list_expr[int(num_list[0])] == '+') | (list_expr[int(num_list[0])] == '-')):
        if (list_expr[int(num_list[0])] == '+'):
            x = a + b
            print(x)
        if (list_expr[int(num_list[0])] == '-'):
            x = a + c
            print(x)
    else:
        pass
    
