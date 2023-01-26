
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
    
    li1_tmp=li1.copy() # li1_tmp=li1[:]
    li2_tmp=li2.copy()
    
    
    if len(li1) < len(li2):
        # [0] * 4 -> [0,0,0,0]
        li1_tmp.extend([default]*(len(li2)-len(li1)))
        
    elif len(li2) < len(li1):
        li2_tmp.extend([default]*(len(li1)-len(li2)))   
    
    #return [ li1_tmp[i] + li2_tmp[i] for i in range(len(li1_tmp)) ]

    res=[]
    for i in range(len(li1_tmp)):
        res.append(li1_tmp[i]+li2_tmp[i])
    return res


l1=[1,2,3,10,23]
l2=[3,4,5]

print ("l1",l1)
print ("l2",l2)
l3=addList(l1,l2)

print ("l3",l3) # [4,6,8,10,23]

l3=addList(l1,l2,10)

print ("l3",l3) # [4,6,8,20,33]


