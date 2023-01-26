data=[12,56,78,12,10,20,22]

ix=2
while ix < len(data):
    print(ix, "->", data[ix])
    ix=ix+1
    
print("*" * 30)

for e in range(len(data)):
    print(e, "->", data[e])

print("*" * 30)

for ix,val in enumerate(data):
    print(ix,"->",val)
    
print("*" * 30)

for e in range(2, len(data)):
    print(e, "->", data[e])
    
data=list(range(5,10)) # [5, 6, 7, 8, 9]
print(data)

data=list(range(5,30,5)) # [5, 10, 15, 20, 25]
print(data)
