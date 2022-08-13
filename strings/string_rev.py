# #rev string through function
def rev_string(string_var):
    rev=""
    for i in range(len(string_var)-1,-1,-1):
        rev=rev+string_var[i]
    return rev

# print(rev_string("Deepika"))
   
# #check pallindrom 
def is_pallindrom(strvar):
    x=strvar[: : -1]
    print(__name__)
    if(x==strvar):
        return True
    else:
        return False
# print("i am in stroing rev files")

# #string replace

def string_replace(stvar,replacingele,replacedwith):
    y=list(stvar)
    for s in range(0,len(y)):
        if(y[s]==replacingele):
            y[s]=replacedwith
    p=''
    p=p.join(y)
    return p
# print(string_replace('deepika','a','cpcp'))

# #string join

# def string_join(mylist2):
#     s=''
#     for x in mylist2:
#         s=s+x
#     return s
# print(string_join(['d','e','p']))


# def string_equal(strv1,strv2):
#     if(strv1==strv2):
#         print("equal")
#         return True
#     else:
#         return False

# print(string_equal('suman','deepika'))

def main():
    print(string_replace('deepika','a','cpcp'))




if(__name__=="__main__"):
    main()
    










