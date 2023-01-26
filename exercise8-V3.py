
def addList(li1, li2, default=0):
    """
    Parameters
    ----------
    li1 : a list of numbers
        
    li2 : a list of numbers
    default : a value to be added in cas the 2 lists are
    not of the same size. The default is 0.

    Returns
    -------
    res : a list (the addition of the 2 lists elements by elements)

    """
    res=[]
    if len(li1) < len(li2):
        for i in range(len(li1)):
            res.append(li1[i]+li2[i])   
        for i in range(len(li1), len(li2)):
            res.append(default+li2[i]) 
    else:
        for i in range(len(li2)):
            res.append(li1[i]+li2[i])   
        for i in range(len(li2), len(li1)):
            res.append(default+li1[i]) 
    return res


l1=[1,2,3,10,23]
l2=[3,4,5]

print ("l1",l1)
print ("l2",l2)
l3=addList(l1,l2)

print ("l3",l3) # [4,6,8,10,23]

l3=addList(l1,l2,10)

print ("l3",l3) # [4,6,8,20,33]

l2=[1,2,3,10,23]
l1=[3,4,5]
l3=addList(l1,l2)

print ("l3",l3)


