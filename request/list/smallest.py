def smallest_func(list1):
    y=99999999
    for x in list1:
        if(x<y):
            y=x

    return y

print(smallest_func([11,22,33,44,55]))
        
def largest_func(list1):
    y=0
    for x in list1:
        if(x>y):
            y=x

    return y


print(largest_func([11,22,33,44,55]))

       #secondlargest 
def second_large(Mylist):
    max=0
    Secondmax=max
    for x in Mylist:
        if (x>max):
            Secondmax=max
            max=x
    return Secondmax
s=second_large([11,22,33,44,55])
print(s)


#positive and negative number count

def count_func(list4):
    ncount=0
    pcount=0
    for x in list4:
        if(x<0):
            ncount=ncount+1
        elif(x>0):
            pcount=pcount+1
    return ncount,pcount
s=count_func([-1,-2,-3,-4,55,77,88,99])
print(s)




        