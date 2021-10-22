import time
import math

if __name__ == '__main__':
    start_time = time.time()
    input = open('input2016_20.txt', 'r').read().split('\n')[:-1]
    print(input)
    globals = []
    for i in input: 
        splitted = i.split('-')
        start = int(splitted[0])
        end = int(splitted[1])
        globals.append((start,end))
    print(globals)
    ip_address = 0
    allowed = 0
   # globals = [(5,8), (0,2), (4,7)]
    while(ip_address <= 4294967295):
        is_banned = False
        for i in globals:
            if(ip_address >= i[0] and ip_address <=i[1]):
                ip_address = i[1]
                is_banned = True
            if(is_banned):
                break
        if(not is_banned):
            allowed = allowed + 1
        ip_address = ip_address + 1
        print(ip_address, allowed)
    print(allowed)
    print('runtime: %f seconds' % (time.time() - start_time))
 #4294968325 too high