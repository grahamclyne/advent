import time
import sys
import math


MAGIC_NUM = 1358



def CountOnes(x):
    count = 0
    while x > 0:
        temp = x % 2
        if(temp == 1):
            count = count + 1
        x = math.floor(x / 2)
    return count

def WallOrOpen(x,y):
    temp = x*x + 3*x + 2*x*y + y + y*y
    temp = temp + MAGIC_NUM
    if(CountOnes(temp) % 2 == 1):
        #is wall
        return 1
    else:
        #is open space
        return 0

def PrintMap(map):
    for i in range(50):
        for j in range(50):
            print(map[i][j], end="")
        print('\n')


if __name__ == '__main__':
    map = [["" for y in range(50)] for x in range(50)]
    start = time.time()
    for i in range(50):
        for j in range(50):
            if(WallOrOpen(j,i) == 1):
                map[i][j] = "#"
            else:
                map[i][j] = "."
    moves = [lambda x,y: (x,y-1), lambda x,y: (x-1,y),lambda x,y: (x,y+1), lambda x,y: (x+1,y)]
    tries = 1
    highest = 0
    fifty_set = set([])
    cur_map = []
    PrintMap(map)
    while(tries > 0):
        step_count = 0
        x = 1
        y = 1
        cur_map = map.copy()
        history = []
        while(True):
            print(x,y, step_count,history)

            for move in moves:
                temp_x,temp_y = move(x,y)
                if(temp_y >= 0 and temp_y < 50 and temp_x >= 0 and temp_x < 50 and cur_map[temp_y][temp_x] == "." and (temp_x,temp_y) not in history):
                    history.append((x,y))
                    step_count = step_count + 1
                    cur_map[y][x] = '0'
                    made_move = True
                    x = temp_x
                    y = temp_y
                    break
            fifty_set.add((x,y))
            if(step_count <= 0):
                break 
            if(not(made_move) or step_count == 50):
                cur_map[y][x] = "0"
                previous = history.pop()
                x = previous[0]
                y = previous[1]
                step_count = step_count - 1
            made_move = False    
        if(len(fifty_set) > highest):
            highest = len(fifty_set)
            print(highest)
        tries = tries - 1
    print(highest)
    x = list(fifty_set)
    x.sort()
    print(x)
    PrintMap(cur_map)
    print('runtime: %f seconds' % (time.time() - start))


    #guesses: 502, 504, 110 (too high) ,104 (not right answer), 102(not right answer)


    #part two, 135 and 136 are too low, 146 too high, 145,144 incorrect,153 incorrect, 108 incorrect