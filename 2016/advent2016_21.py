import time
import math

def rotate(input, steps, dir):
    if(dir == 'left'):
        return input[steps:] + input[:steps]
    elif(dir == 'right'):
        return input[-steps:] + input[:-steps] 
    return rotated

def rotate2(input, steps):
    temp = ''
    for j in range(steps):
        temp_list = input.copy()
        for i in range(len(input)):
            if(i == 0):
                temp = input[i]
                input[i] = temp_list[len(input)-1]
            else:
                temp = input[i]          
                input[i] = temp_list[i-1] 
    return input
                
if __name__ == '__main__':
    start_time = time.time()
    input = open('input2016_21.txt', 'r').read().split('\n')[:-1]
    start_list = ['a','b','c','d','e','f','g','h']
    start_list = ['f','b','g','d','c','e','a','h']
  #  start_list = ['a','b','c','d','e']
    input.reverse()
    test = ['swap position 4 with position 0', 
    'swap letter d with letter b',
    'reverse positions 0 through 4',
    'rotate left 1 step',
    'move position 1 to position 4',
    'move position 3 to position 0',
    'rotate based on position of letter b',
    'rotate based on position of letter d']

    for cmd in input:
        cmd = cmd.split(' ')
        if('swap' in cmd and 'position' in cmd):
            swap_1 = int(cmd[2])
            swap_2 = int(cmd[5])
            temp = start_list[swap_1]
            start_list[swap_1] = start_list[swap_2]
            start_list[swap_2] = temp

        elif('swap' in cmd and 'letter' in cmd):
            index_1 = start_list.index(cmd[2])
            index_2 = start_list.index(cmd[5])
            temp = start_list[index_2]
            start_list[index_2] = start_list[index_1]
            start_list[index_1] = temp

        elif('rotate' in cmd and 'based' in cmd):
            letter = cmd[6]
            index = start_list.index(letter)
            if(index >= 4): 
                index = index + 1
            print(index)
            start_list = rotate2(start_list, index + 1)

        elif('rotate' in cmd):
            start_list = rotate(start_list, int(cmd[2]), cmd[1])

        elif('move' in cmd):
            temp = start_list[int(cmd[2])]
            start_list.remove(start_list[int(cmd[2])])
            start_list.insert(int(cmd[5]), temp)

        elif('reverse' in cmd):
            temp = start_list[int(cmd[2]):int(cmd[4])+1][::-1]
            start_list = start_list[:int(cmd[2])] + temp + start_list[int(cmd[4])+1:]      
        print(cmd)
        print(start_list)
    print('runtime: %f seconds' % (time.time() - start_time))





#ghcdfbea not the right answer for part 2