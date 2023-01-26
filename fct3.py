def add(op1, op2): # the header of the function
    if isinstance(op1, (int,float)) and isinstance(op2, (int,float)):
        temp=op1+op2
        return temp
    else:
        print("Wrong kind of arguments received")
        return None
    

result=add(23, 67) # positional arguments
print(result)

result=add(op2=23, op1=67) # named arguments
print(result)