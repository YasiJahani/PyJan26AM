def add(*arguments): # the header of the function
    print(arguments, type(arguments))
    total=0
    for e in arguments:
        total += e
    return total

# result=add() # positional arguments
# print(result)
# result=add(23) # positional arguments
# print(result)
# result=add(23,67) # positional arguments
# print(result)
# result=add(23,67,78,90,56,45) # positional arguments
# print(result)

# data=[56,78,89,89]
# result=add(*data) # positional arguments
# print(result)



