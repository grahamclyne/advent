import time
import sys
import math
import hashlib

def threeInARow(input):
    count = 0
    for index in range(1,len(input)):
        if(input[index-1] == input[index]):
            count = count + 1
        else:
            count = 0
        if(count == 2):
            return input[index]
    return None

def fiveInARow(input,char):
    count = 0
    for index in range(1,len(input)):
        if(input[index-1] == input[index] and input[index] == char):
            count = count + 1
        else:
            count = 0
        if(count == 4):
            return True
    return False

if __name__ == '__main__':
    start = time.time()
    key_count = 0
    salt = 'ihaygndm'
    pre_hashed = []

    for i in range(51000):
        hash_1 = salt + str(i)
        for x in range(2017):
            hash_1 = hashlib.md5(hash_1.encode("utf-8")).hexdigest()
        pre_hashed.append(hash_1)
        print(i, hash_1)



    for i in range(50000):
        char = threeInARow(pre_hashed[i])
        if(char is not None):
           # print(i, hash,char)
            for j in range(i+1, i+1000):
                hash = pre_hashed[j]
                if(fiveInARow(hash,char)):
                    key_count = key_count + 1
                    print(key_count, hash, i, j, char)
                    break
        if(key_count == 64):
            print(i)
            break

    #guessed 137511, too high, 14709 too low
    # print(hasThreeInARow("aalsdkajsldkj444jalskdjasf"))
    # print(hasThreeInARow("sdjfslakdjwoiru230598uvnd,smd"))
    # print(hasThreeInARow("sfj333jlasdkfjsdfnclkjsdf2"))
    # print(hasThreeInARow("aaajdi24091248fjlkdfjsdf"))
    print('runtime: %f seconds' % (time.time() - start))
