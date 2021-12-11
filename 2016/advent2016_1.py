import time

if __name__ == '__main__':
    start = time.time()
    input = open('input2016_1.txt', 'r').read().split('\n')[:-1]
    input = input[0].split(', ')
    print(input)
    x = 0
    y = 0
  #  input = ['R8', 'R4', 'R4', 'R8']
    orientation = 0
    history = []
    for dir in input:
        print(dir)
        if(dir[0] == 'R'):
            orientation = (orientation + 1) % 4
        if(dir[0] == 'L'):
            orientation = (orientation - 1) % 4
        print('orientation',orientation)
        if(orientation == 0):
            for step in range(int(dir[1:])):
                y = y + 1
                if((x,y) in history):
                    print((x,y))
                    break
                history.append((x,y))

        if(orientation == 1):
            for step in range(int(dir[1:])):
                x = x + 1
                if((x,y) in history):
                    print((x,y))
                    break
                history.append((x,y))

        if(orientation == 2):
            for step in range(int(dir[1:])):
                y = y - 1
                if((x,y) in history):
                    print((x,y))
                    break
                history.append((x,y))

        if(orientation == 3):
            for step in range(int(dir[1:])):
                x = x - 1
                if((x,y) in history):
                    print((x,y))
                    break
                history.append((x,y))
    
    print('runtime: %f seconds' % (time.time() - start))

#PART 2, 176 too high,150 not correct
