
# map() filter() reduce()
import functools

data=[5,7,6,-2,1,-5]

res=[]
for e in data:
    res.append(e**2)
print(res)

def fct(nb):
    return nb**2

res=list(map(fct, data))
print(res)

def isEven(nb):
    return nb % 2 == 0

res=list(filter(isEven, data))
print(res)

def fct2(a,b):
    return a+b

res=functools.reduce(fct2, data)
print(res)




