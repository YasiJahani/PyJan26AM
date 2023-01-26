def add(op1=0, op2=0): # the header of the function
    if isinstance(op1, (int,float)) and isinstance(op2, (int,float)):
        temp=op1+op2
        return temp
    else:
        print("Wrong kind of arguments received")
        return None
    

result=add() # positional arguments
print(result)
result=add(23) # positional arguments
print(result)
result=add(23,67) # positional arguments
print(result)
