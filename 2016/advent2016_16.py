import time


def modifiedDragonCurve(a):
    b = a
    b = list(map(lambda x: '1' if (x == '0') else '0', b))
    b = b[::-1]
    b = ''.join(b)
    return a + '0' + b

def checkPairs(word):
    checksum = []
    word = list(word)
    index = 0
    while(index < len(word)-1):
        if(word[index] == word[index + 1]):
            checksum.append('1')
        else:
            checksum.append('0')
        index = index + 2
    return checksum

def generateCheckSum(input):
    checksum = checkPairs(input)
    while(len(checksum) % 2 == 0):
        checksum = checkPairs(checksum)
    return ''.join(checksum)
        

if __name__ == '__main__':
    start = time.time()
    input = '10001001100000001'
    disk_length = 35651584
    string_length = 0
    while(string_length < disk_length):
        input = modifiedDragonCurve(input)
        string_length = len(input)
    output = input[0:disk_length]
    checksum = generateCheckSum(output)
    print(checksum)
    print('runtime: %f seconds' % (time.time() - start))
