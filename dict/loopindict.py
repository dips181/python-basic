my_dict={1:"sun",2:"moon",3:"flower"}
for x in my_dict :  #for keys
  print(x)

for y in my_dict.items():  #for value
    print(y)  

#Loop through both keys and values, by using the items() method
for x,y in my_dict.items():
    print(x,y)

#Copy a Dictionary
list2=my_dict.copy()
print(list2)

#Make a copy of a dictionary with the dict() function:

list3=dict(my_dict)
print(list3)