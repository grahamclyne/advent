import hashlib 

#python does not support tail recursion - had to do this iteratively
def computeHash():
    i = 0
    while(True):
        s = 'bgvyzdsv' + str(i)
        result = hashlib.md5(s.encode()) 
        encoded = result.hexdigest()
        starts_with = encoded[:6]
        if(starts_with == '000000'):
            return i
        i = i + 1

print(computeHash())

