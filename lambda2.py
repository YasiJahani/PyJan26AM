
# map() filter() reduce()
import functools

data=[5,7,6,-2,1,-5]

res=[]
for e in data:
    res.append(e**2)
print(res)

res=list(map(lambda a: a**2, data))
print(res)

# def isEven(nb):
#     return nb % 2 == 0

res=list(filter(lambda nb: nb % 2 == 0, data))
print(res)

# def fct2(a,b):
#     return a+b

res=functools.reduce(lambda a,b: a+b, data)
print(res)




