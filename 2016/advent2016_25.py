import time

if __name__ == '__main__':
    start = time.time()
    input = open('/home/graham/code/advent/2016/input2016_25.txt', 'r').read().split('\n')[:-1]
    
    tries = 0
    while(tries < 1000):
        registers = {'a':tries,'b':0,'c':0,'d':0}
        row = 0
        out_string = ''
        out_signal = ''
        print("here", row)
        while row < len(input): 
            parsed = input[row].split(" ")
            # print(registers, parsed)
            if(parsed[0] == "cpy"):
                if(parsed[1].isdigit() or '-' in parsed[1]):
                    registers[parsed[2]] = int(parsed[1])
                else:
                    registers[parsed[2]] = registers[parsed[1]]
                row = row + 1
            elif(parsed[0] == "inc"):
                registers[parsed[1]] = registers[parsed[1]] + 1
                row = row + 1
            elif(parsed[0] == "dec"):
                registers[parsed[1]] = registers[parsed[1]] - 1
                row = row + 1
            elif(parsed[0] == "jnz"):
                if(parsed[1].isdigit() and int(parsed[1]) != 0):
                    row = row + int(parsed[2])
                elif(parsed[1].isdigit() and int(parsed[1]) == 0):
                    row = row + 1
                elif(registers[parsed[1]] != 0):
                    row = row + int(parsed[2])
                else:
                    row = row + 1
            elif(parsed[0] == 'out'):
                if(parsed[1].isdigit()):
                    out_sigal = parsed[1]
                else:
                    out_signal = str(registers[parsed[1]])
                out_string = out_string + out_signal
                row = row + 1
            if(len(out_string) > 10 and not (out_string[:10] == '0101010101' or out_string[:10] == '1010101010')):
                 print(tries, out_string)
                 break
            print(out_string, tries)
            #print(out_signal,end='')
        tries = tries + 1
        print(out_string[:5])
    print('runtime: %f seconds' % (time.time() - start))

