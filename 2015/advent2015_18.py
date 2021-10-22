import time
import math
import copy 
from functools import reduce
def neighbours(row,col,input,dim):
    count = 0
    lst = []

    indices = [(row+1,col),(row-1,col)]
    if(row + 1 < dim):
        lst.append(input[row+1][col])
    if(row - 1 >= 0):
        lst.append(input[row-1][col])
    if(col + 1 < dim):
        lst.append(input[row][col+1])
    if(col - 1 >= 0 ):
        lst.append(input[row][col-1])
    if(row + 1 < dim and col + 1 < dim):
        lst.append(input[row+1][col+1])
    if(row + 1 < dim and col - 1 >= 0 ):
        lst.append(input[row+1][col-1])
    if(row - 1 >= 0  and col + 1 < dim):
        lst.append(input[row-1][col+1])
    if(row - 1 >= 0 and col - 1 >= 0):
        lst.append(input[row-1][col-1])
    for i in lst:
        if i == '#':
            count += 1

    return count

start_time = time.time()
input_raw =  open('input18.txt', 'r').read()
dim = 100
input_raw = input_raw.replace('\n','')
#input_raw = '##.#.#...##.#....#..#...#.#..#####.#'
x = [input_raw[start:start+dim] for start in range(0, len(input_raw), dim)]
x = [[char for char in word] for word in x]
output = copy.deepcopy(x)
x[99][0] = '#'
for j in range(100):
    for i in range(dim*dim):
        col = (i) % dim
        row = math.floor(i / dim)
        c = neighbours(row,col,x,dim)

       # print(x[0][0], x[0][dim-1], x[dim-1][dim-1], x[dim-1][0])
        if((row == 0 and col == 0) or ((row == (dim-1)) and (col == 0)) or (row == (dim-1) and (col == (dim-1))) 
            or (row == 0 and col == (dim-1))):
            output[row][col] = '#'

        elif(x[row][col] == '#' and (c == 2 or c == 3)):
            output[row][col] = '#'
        elif(x[row][col] == '.' and c == 3):
            output[row][col] = '#'
        else:
            output[row][col] = '.'  
    light_count = 0
    for k in output:
        for l in k:
            if(l == '#'):
                light_count += 1
    print(light_count)
    
    x = copy.deepcopy(output)
print('time = ', time.time() - start_time)

#900 too high
#865 too low for part2, 911 too high 