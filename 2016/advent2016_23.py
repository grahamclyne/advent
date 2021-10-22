import time

if __name__ == '__main__':
    start = time.time()
    input = open('input2016_23.txt', 'r').read().split('\n')[:-1]
    registers = {'a':12,'b':0,'c':0,'d':0}
    #input = ['cpy 2 a','tgl a','tgl a','tgl a','cpy 1 a', 'dec a', 'dec a']
    row = 0
    count = 0
  #  input = ['cpy a b', 'dec b', 'cpy a d', 'cpy 0 a', 'cpy b c', 'inc a', 'dec c', 'jnz c -2', 'dec d', 'jnz d -5', 'dec b', 'cpy b c', 'cpy c d', 'dec d', 'inc c', 'jnz d -2', 'tgl c', 'cpy -16 c', 'cpy 1 c', 'cpy 96 c', 'cpy 95 d', 'inc a', 'dec d', 'jnz d -2', 'dec c', 'jnz c -5']

    while row < len(input):     
        parsed = input[row].split(" ")
        if(parsed[0] == 'cpy' and parsed[1] == 'b' and parsed[2] == 'c' and 'inc' in input[row + 1] and 'dec' in input[row + 2] and 'jnz' in input[row + 3] and 'dec' in input[row + 4] and 'jnz' in input[row + 5]):
            print('here', row)
            registers['a'] = registers['a'] + (registers['b'] * registers['d'])
            row = row + 5
            registers['d'] = 0
            registers['c'] = 0
        elif(parsed[0] == "cpy"):
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
            if(not parsed[2].isdigit() and '-' not in parsed[2]):
                row = row + registers[parsed[2]]
            elif((parsed[1].isdigit() and int(parsed[1]) != 0) or registers[parsed[1]] != 0):
                row = row + int(parsed[2])
            else:
                row = row + 1
        elif(parsed[0] == 'tgl'):

            temprow = row + registers[parsed[1]]
            print(parsed,temprow)
            if(temprow >= len(input)):
                row = row + 1
                continue
            tempinput = input[temprow].split(" ")
            if(tempinput[0] == 'inc'):
                tempinput[0] = 'dec'
            elif(len(tempinput) == 2):
                tempinput[0] = 'inc'
            elif(tempinput[0] == 'jnz'):
                tempinput[0] = 'cpy'
            elif(len(tempinput) == 3):
                tempinput[0] = 'jnz'
            input[temprow] = ' '.join(tempinput)
            row = row + 1
        print(parsed)
        count = count + 1
        print(registers)
        # if(count == 70):
        #     break
    print(input)
    print('runtime: %f seconds' % (time.time() - start))

# 479001600 too low
