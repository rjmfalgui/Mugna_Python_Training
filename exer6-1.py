def multiplicationTable(arg1, arg2=0): 
    if arg1 == 0:
        arg2 = arg1
    
    final_list = []
    for x in range(1, arg1 + 1):
        cont = []
        for y in range(1, arg2 + 1):
            cont.append(x * y)
        print(cont)

multiplicationTable(5, 5)