import time
import sys

if __name__ == '__main__':
    start = time.time()
    input = open('input2016_12.txt', 'r').read().split('\n')[:-1]
    registers = {'a':0,'b':0,'c':1,'d':0}
    row = 0
    while row < len(input):
        # print(registers)
        # print(input[row])      
        parsed = input[row].split(" ")
        if(parsed[0] == "cpy"):
            if(parsed[1].isdigit()):
                registers[parsed[2]] = int(parsed[1])
            else:
                registers[parsed[2]] = registers[parsed[1]]
            row = row + 1
        if(parsed[0] == "inc"):
            registers[parsed[1]] = registers[parsed[1]] + 1
            row = row + 1
        if(parsed[0] == "dec"):
            registers[parsed[1]] = registers[parsed[1]] - 1
            row = row + 1
        if(parsed[0] == "jnz"):
            if((parsed[1].isdigit() and int(parsed[1]) != 0) or registers[parsed[1]] != 0):
                row = row + int(parsed[2])
            else:
                row = row + 1

    print(registers)
    print('runtime: %f seconds' % (time.time() - start))