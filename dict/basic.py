from msvcrt import kbhit
from re import S


dict_var= {'id':1,'name':"rakesh",'Marks':[34,56,76,54,56,65]}
print('id' in dict_var)
# sum=0
# for x in dict_var['Marks']:
#     sum=sum+x
# print(sum)
# for i,j in dict_var.items():
#     if(i=='Marks'):
#         sum=0
#         for s in j:
#             sum=sum+s
#         print(sum)


my_dict={'marks':{'ram':[45,65,67,43,56],'suresh':[76,54,64,32,43],'mohan':[65,54,64,64,43]}}

for i,j in my_dict.items():
    if(i=='marks'):
        for s,p in j.items():
            if(s=='suresh'):
                sum=0
                for k in p:
                    sum=sum+k
                print(sum)

