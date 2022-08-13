
def concat_dict(dict1,dict2):
    Result_dict={}
    for x,y in dict2.items():
        Result_dict[x]=y
    for x,y in dict1.items():
        Result_dict[x]=y
    return Result_dict
s=concat_dict({1:'suman',2:'priya'},{2:'flower',4:'rain'})
print(s)





#dict3={'math':50,'science':120,'ss':124,'History':150,'geography':90}
def Avg_markdict(dict4):
    sum=0
    for x,y in dict4.items():
        sum=(sum+y)/5
    return sum
s=Avg_markdict({'math':50,'science':120,'ss':124,'History':150,'geography':90})
print(s)
    


str1="jan = january ; feb = february ; mar = march"
s=str1.split(';')
print(s)
dict5={}
for x in s:
    z=x.split('=')
    print(z)
    dict5[z[0]]=z[1]
print(dict5)



