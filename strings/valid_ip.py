# input '192.168.1.1'  --- True
# "192.266.1.1"
#178.34
#255.255.255.255

def valid_ip(ipaddress):
    s=ipaddress.split('.')
    if(len(s)!=4):
        return False
    for x in s:
        x=int(x)
        if(x>256):
            return False
    return True       
        

print(valid_ip('192.123.3'))


#password matching  