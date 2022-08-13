#Remove Specified Item
this_list = ["apple", "banana", "cherry"]
this_list.remove("apple")
print(this_list)

#Remove Specified Index---->pop()---->If you do not specify the index, the pop() method removes the last item.
this_list.pop(0)

#The del keyword also removes the specified index:
del this_list[0]

#Clear the List
nature_var=["air","plants","flower"]
nature_var.clear()
print(nature_var)
