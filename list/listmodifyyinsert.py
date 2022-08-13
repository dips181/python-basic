thislist = ["apple", "banana", "cherry"]

#Change the second item:
thislist[2]='watermelon'
print(thislist)


#Change a Range of Item Values
my_list = ["apple", "banana", "cherry", "orange", "kiwi", "mango"]
my_list[2:5]=["carrot","beetroot","pineapple"]
print(my_list)

#To add an item to the end of the list, use the append() method:
my_list.append("watermelon")
print(my_list)

#The insert() method inserts an item at the specified index:  Insert Items

my_list.insert(2,"pumpkin")
print(my_list)

#Extend List------> To append elements from another list to the current list, use the extend() method.
nature_var=["air","plants","flower"]
my_list.extend(nature_var)
print(my_list)


