#forloop
nature_var=["plants","flower","air"]
for x in nature_var:
   pass

#Loop Through the Index Numbers
for x in range(0,len(nature_var)):
    pass

#Using a While Loop

i=0
while(i>len(nature_var)):
    print(nature_var[i])
    i=i+1

#////Looping Using List Comprehension
[print(x) for x in nature_var]

[x for x in nature_var if "a" in x]
print(x)
