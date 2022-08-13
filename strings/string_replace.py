def string_replace(str_var):
   
    my_list=[]
    for x in range(0,len(str_var)):
        y=str_var[x]
        for s in (x+1,len(str_var)):
            if(s==len(str_var)):
                my_list.append(y)
                break
            y=y+str_var[s]
            if (str_var[s]==" "):
              my_list.append(y)
              break
    return my_list
print(string_replace("I am deepika verma"))

        






