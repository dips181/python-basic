# Minimum 8 characters.
# The alphabet must be between [a-z]
# At least one alphabet should be of Upper Case [A-Z]
# At least 1 number or digit between [0-9].
# At least 1 character from [ _ or @ or $ ].


def checking_password( password1):
    if(len(password1)<8):
        return False
    isUppercase=False
    isalpha=False
    isnum=False
    isspecial=False
    special_char=['!','@','#','$','%']
    for x in password1:
        if(x.isupper()):
            isUppercase=True
        if(x.isdigit()):
            isnum=True
        if(x in special_char):
            isspecial=True
        if(x.isalpha()):
            isalpha=True
    if(isUppercase and isalpha and isnum and isspecial):
        return True
    else:
        return False
s=checking_password("Deeiaaa?")
print(s)

