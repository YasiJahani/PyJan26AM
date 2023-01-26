def add(op1, op2): # the header of the function
    """
        This function returns the addition of its arguments
    parameter:
        op1: an int or a float
        op2: an int or a float
    returned value:
        an int or a float
    """
    if isinstance(op1, (int,float)) and isinstance(op2, (int,float)):
        temp=op1+op2
        return temp
    else:
        print("Wrong kind of arguments received")
        return None
    

result=add(23, 67)
print(result)

result=add("abc", "def")
print(result)