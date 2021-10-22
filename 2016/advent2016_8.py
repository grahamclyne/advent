import numpy as np
screen = [[''] * 50 for x in range(6)]
print(screen)
input_raw =  open('input2016_8.txt', 'r').read().split('\n')
csv_gen = (row for row in open('input2016_8.txt', 'r'))
for row in csv_gen:
    row = row.replace('\n','')
    print(row)
    if('rect' in row):
        dims = row.split(' ')[1].split('x')
        print(dims)
        for row in range(int(dims[1])):
            for col in range(int(dims[0])):
                screen[row][col] = '#'
    elif('rotate' in row):
        info = row.split(' ')
        dim = info[1]
        dim_num = int(info[2].split('=')[1])
        distance = int(info[4])
        print(dim,dim_num,distance)
        if('column' == dim):
            for i in range(6):
                temp = screen[i][dim_num]
                index = i + 1
                if(i + 1 > 5):
                    index = 0
                screen[i][dim_num] = screen[index][dim_num]
                screen[index][dim_num] = temp

        else:
            for i in range(50):
                temp = screen[dim_num][i]
                index = i + 1
                if(i + 1 > 49):
                    index = 0
                screen[dim_num][i] = screen[dim_num][index]
                screen[dim_num][index] = temp
print(screen)
count = 0
for row in range(len(screen)):
    for col in range(len(screen[row])):
        if(screen[row][col] == '#'):
            count += 1
print(count)

#43 is incorrect