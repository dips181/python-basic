
  #two sum      
def two_sum(list1,target):
    my_list=[]
    for i in range(0,len(list1)):
        for j in range(i+1,len(list1)):
            if(list1[i]+list1[j]==target):
                my_list.append((i,j))
    return my_list

x=two_sum([1,2,3,4],5)
print(x)

x=5
y=8


list_3=[12,3,4,6,7]
list_3.s
y=list_3[2]
z=list_3[4]
list_3[2],list_3[4]=list_3[4],list_3[2]
print(list_3)


