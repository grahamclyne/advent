import time

if __name__ == '__main__':
    start = time.time()
    input = open('input2016_18.txt', 'r').read().split('\n')[:-1]
    input = input[0]
    total = [input]
    #input = '.^^.^.^^^^'
    for row in range(399999):
        next_row = []
        for i in range(len(input)):
            
            if(i == 0):
                if((input[0] == '^' and input[1] == '^') or (input[0] == '.' and input[1] == '^')):
                    next_row.append('^')
                else:
                    next_row.append('.')
            elif(i == len(input) - 1):
                if((input[i-1] == '^' and input[i] == '^') or (input[i-1] == '^' and input[i] == '.')):
                    next_row.append('^')
                else:
                    next_row.append('.')
            else:
                if(
                    (input[i-1] == '^' and input[i] == '^' and input[i+1] == '.') or 
                    (input[i-1] == '.' and input[i] == '^' and input[i+1] == '^') or
                    (input[i-1] == '^' and input[i] == '.' and input[i+1] == '.') or
                    (input[i-1] == '.' and input[i] == '.' and input[i+1] == '^')):
                    next_row.append('^')
                else:
                    next_row.append('.')
        input = ''.join(next_row)
        total.append(input)
    count = 0
    for row in total:
        for c in row:
            if(c == '.'):
                count = count + 1
    print(count)

    #545 too low

    print('runtime: %f seconds' % (time.time() - start))
