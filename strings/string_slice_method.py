name= "Ram"
class_var= 8

student= "{Name} is studing in {classM} ".format(classM=class_var,Name=name)
student= "{} is studing in {} ".format(class_var,name)
student= "{1} is studing in {0} ".format(class_var,name)

sentence= "I graduated from \"RGPV\" "
print(sentence)

#string methods:
#1.find()
sstr="steben has complted ms from paris"
print(sstr.find('t'))

#2.index()
print(sstr.index('b'))

#3 isalnum()
print(sstr.isalnum())

#4.isalpha()
print(sstr.isalpha())

#5.islower()
print(sstr.islower())

#6.isspace() #returns if string hAS whitespace
print(sstr.isspace())

#isupper()
print(sstr.isupper())

#join()
#print('dipi'.join(sstr))


#split()            --------Splits the string at the specified separator, and returns a list
print(sstr.split())

#startswith()        
#print(sstr.startswith('s'))

#strip()             <--Returns a trimmed version of the string
print(sstr.strip())

#swapcase() ----upper to lower vice-versa
print(sstr.swapcase())

#title()--Converts the first character of each word to upper case
print(sstr.title())

#translate()--Returns a translated string
print(sstr.translate('paris'))

#upper()------Converts a string into upper case
print(sstr.upper())


