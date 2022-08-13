thisdict={1:"sun",2:"moon"}
thisdict[3]='sunshine'
(type(thisdict))

print(len(thisdict))

thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
print(thisdict)

#update dictionary
thisdict.update({"year": 2020})
print(thisdict)

#access the dictionary
print(thisdict["brand"])

#add items
thisdict["sunshine"]="sun"
print(thisdict)

#removeitems:

thisdict.pop("brand")
print(thisdict)

#The popitem() method removes the last inserted item 
thisdict.popitem()
print(thisdict)

#The del keyword removes the item with the specified key name:
del thisdict['year']
print(thisdict)

#The clear() method empties the dictionary:

thisdict.clear()
print(thisdict)

thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
if "model" in thisdict:
  print("Yes, 'model' is one of the keys in the thisdict dictionary")

print(thisdict.get("model",10))