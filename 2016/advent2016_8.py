
def printScreen(screen):
    for row in range(len(screen)):
        for col in range(len(screen[0])):
            if(screen[row][col] == ''):
                print('.',end='')
            print(screen[row][col],end='')
        print('\n')


screen = [[''] * 50 for x in range(6)]
input_raw =  open('input2016_8.txt', 'r').read().split('\n')
csv_gen = (row for row in open('input2016_8.txt', 'r'))
NUM_ROWS = 6
NUM_COLS = 50
#test data
# screen = [[''] * 7 for x in range(3)]
# csv_gen = ['rect 3x2', 'rotate column x=1 by 1', 'rotate row y=0 by 4', 'rotate column x=1 by 1']
# NUM_ROWS = 3
# NUM_COLS = 7

for row in csv_gen:
    row = row.replace('\n','')
    if('rect' in row):
        dims = row.split(' ')[1].split('x')
        for row in range(int(dims[1])):
            for col in range(int(dims[0])):
                screen[row][col] = '#'
    elif('rotate' in row):
        info = row.split(' ')
        dim = info[1]
        dim_num = int(info[2].split('=')[1])
        distance = int(info[4])
        if('column' == dim):
            temp = ''
            for run in range(distance):
                for i in range(NUM_ROWS):
                    back_index = i - 1
                    if(i == 0):
                        back_index = NUM_ROWS-1 
                        temp = screen[i][dim_num]
                        screen[i][dim_num] = screen[back_index][dim_num]
                    else:
                        x = temp
                        temp = screen[i][dim_num]
                        screen[i][dim_num] = x
        else:
            for run in range(distance):
                temp = ''
                for i in range(NUM_COLS):
                    back_index = i - 1
                    if(i == 0):
                        temp = screen[dim_num][i]
                        screen[dim_num][i] = screen[dim_num][NUM_COLS-1]
                    else:
                        x = temp
                        temp = screen[dim_num][i]
                        screen[dim_num][i] = x
printScreen(screen)

# count = 0
# for row in range(len(screen)):
#     for col in range(len(screen[row])):
#         if(screen[row][col] == '#'):
#             count += 1
# print(count)

#43 is incorrect