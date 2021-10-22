import time
import hashlib
start_time = time.time()
index = 0
pwd = [0,0,0,0,0,0,0,0]
while(True):
    input = 'ojvtpuvg' + str(index)
    index += 1
    hashed = hashlib.md5(input.encode())
    if(hashed.hexdigest()[:5] == '00000'):
        print(input)
        print(hashed.hexdigest())
        print(hashed.hexdigest()[:5])
        print('FOUND')
        pos = hashed.hexdigest()[5:6]
        if(ord(pos) > 57):
            continue
        if(int(pos) > 7 or int(pos) < 0):
            continue
        char = hashed.hexdigest()[6:7]
        if(pwd[int(pos)] == 0):
            pwd[int(pos)] = char
        print(pwd)
    if(len(pwd) > 8):
        break
print("--- %s seconds ---" % (time.time() - start_time))