def algebra(expr):
    #splitting input string into list
    list_expr = expr.split()
    #finding positions of operators
    for j in list_expr:
        num_list = []
        for i, item in enumerate(list_expr):
            if (item == '*' or item == '/'):
                num_list.extend(str(i))
        for i, item in enumerate(list_expr):
            if (item == '+' or item == '-'):
                num_list.extend(str(i))
        print(num_list) #bugtest: print out indexes of operators
        try:
            int(j)
        except ValueError:
            #defining numbers to operate
            a = int(list_expr[int(num_list[0]) - 1])
            b = int(list_expr[int(num_list[0]) + 1])
            c = -b
            #first operation
            if ((list_expr[int(num_list[0])] == '*') | (list_expr[int(num_list[0])] == '/')):
                if (list_expr[int(num_list[0])] == '*'):
                    x = a * b
                if (list_expr[int(num_list[0])] == '/'):
                    x = a / b
            if ((list_expr[int(num_list[0])] == '+') | (list_expr[int(num_list[0])] == '-')):
                if (list_expr[int(num_list[0])] == '+'):
                    x = a + b
                if (list_expr[int(num_list[0])] == '-'):
                    x = a + c
            else:
                pass
            print(x) #bugtest: print out result of first operator
            list_expr.pop(int(num_list[0]) - 1)
            list_expr.pop(int(num_list[0]))
            list_expr[int(num_list[0]) - 1] = str(x)
            print(list_expr)
    for j in list_expr:
        num_list = []
        for i, item in enumerate(list_expr):
            if (item == '*' or item == '/'):
                num_list.extend(str(i))
        for i, item in enumerate(list_expr):
            if (item == '+' or item == '-'):
                num_list.extend(str(i))
        print(num_list) #bugtest: print out indexes of operators
        try:
            int(j)
        except ValueError:
            #defining numbers to operate
            a = int(list_expr[int(num_list[0]) - 1])
            b = int(list_expr[int(num_list[0]) + 1])
            c = -b
            #first operation
            if ((list_expr[int(num_list[0])] == '*') | (list_expr[int(num_list[0])] == '/')):
                if (list_expr[int(num_list[0])] == '*'):
                    x = a * b
                if (list_expr[int(num_list[0])] == '/'):
                    x = a / b
            if ((list_expr[int(num_list[0])] == '+') | (list_expr[int(num_list[0])] == '-')):
                if (list_expr[int(num_list[0])] == '+'):
                    x = a + b
                if (list_expr[int(num_list[0])] == '-'):
                    x = a + c
            else:
                pass
            print(x) #bugtest: print out result of first operator
            list_expr.pop(int(num_list[0]) - 1)
            list_expr.pop(int(num_list[0]))
            list_expr[int(num_list[0]) - 1] = str(x)
            print(list_expr)          
