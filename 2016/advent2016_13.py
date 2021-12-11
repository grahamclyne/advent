import time
import math

MAGIC_NUM = 1358

def countOnes(x):
    count = 0
    while x > 0:
        temp = x % 2
        if(temp == 1):
            count = count + 1
        x = math.floor(x / 2)
    return count

def wallOrOpen(x,y):
    temp = x*x + 3*x + 2*x*y + y + y*y
    temp = temp + MAGIC_NUM
    if(countOnes(temp) % 2 == 1):
        #is wall
        return 1
    else:
        #is open space
        return 0

def printMap(map):
    for i in range(50):
        for j in range(50):
            print(map[i][j], end="")
        print('\n')

def makeMap():
    map = [["" for y in range(50)] for x in range(50)]
    for i in range(50):
        for j in range(50):
            if(wallOrOpen(j,i) == 1):
                map[i][j] = "#"
            else:
                map[i][j] = "."
    return map

def getAdjacentMoves(pos,map):
    x = pos[0]
    y = pos[1]
    adj_list = []
    if(x-1 >= 0 and map[x-1][y] != '#'):
        adj_list.append((x-1,y))
    if(y-1 >= 0 and map[x][y-1] != '#'):
        adj_list.append((x,y-1))
    if(y+1 < 50 and map[x][y+1] != '#'):
        adj_list.append((x,y+1))
    if(x+1 < 50 and map[x+1][y] != '#'):
        adj_list.append((x+1,y))
    return adj_list

def BFS(maze_map):
    history = []
    queue = []
    start_position = (1,1)
    queue.append(start_position)
    history.append(start_position)
    parents = {}
    steps = 0
    total = 0
    while(len(queue) > 0):
        #if this was queue.pop(), we would have DFS, and would not find shortest path necessarily
        current = queue[0]
        queue = queue[1:]
        children = getAdjacentMoves(current,maze_map)
        for child in children:    
            if(child not in history):
                print(queue,child)
                parents[child] = current
                history.append(child)
                queue.append(child)
                #get history
                steps = 0
                while(child != start_position):
                    child = parents[child]
                    steps = steps + 1
                if(steps <= 50):
                    total = total + 1
                    print(total)
    return total

    return
if __name__ == '__main__':
    start = time.time()    
    moves = [lambda x,y: (x,y-1), lambda x,y: (x-1,y),lambda x,y: (x,y+1), lambda x,y: (x+1,y)]
    map = makeMap()
    total = BFS(map)
    print(total)
    print('runtime: %f seconds' % (time.time() - start))

    #guesses: 502, 504, 110 (too high) ,104 (not right answer), 102(not right answer)
    #part two, 135 and 136 are too low, 146 too high, 145,144 incorrect,153 incorrect, 108 incorrect, 140 incorrect