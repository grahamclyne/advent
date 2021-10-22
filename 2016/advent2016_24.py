import time
import sys

def findMove(position, map):
    if(len(map[position[0]]) > position[1] and map[position[0]][position[1]] != '#'):
        return (position[0],position[1])
    else:
        return -1

def findMove1(position, map,history):
    dirs = [
        findMove((position[0], position[1] + 1), map),
        findMove((position[0] + 1, position[1]), map),
        findMove((position[0] - 1, position[1]), map), 
        findMove((position[0], position[1] - 1), map)]
    dirs = [x for x in dirs if x != -1 and x not in history]
    if(len(dirs) == 0):
        return -1
    return dirs


def shortestPath(goal, map, position, path_length, paths, shortest_path,history): #position a tuple (x,y)
    if(map[position[0]][position[1]] == goal):
        return path_length
    else:
        dir = findMove1(position,map,history)
        if(dir != -1): #no move to be made
            for direction in dir:
                history.append(direction)
                x = shortestPath(goal, map.copy(), direction,path_length + 1, paths, shortest_path,history)
                history.remove(direction)
                if(x < shortest_path):
                    shortest_path = x
    return shortest_path

if __name__ == '__main__':
    start = time.time()
    input = open('input2016_24.txt', 'r').read().split('\n')[:-1]
    #read in map as 2d array
    test = ['###########','#0.1.....2#','#.#######.#','#4.......3#','###########']
    map = []

    for row in test:
        row_list = []
        for brick in row:
            row_list.append(brick)
        map.append(row_list)
    print(map)
    
    #find nodes and shortest?? distances to other nodes to make a graph
    starting_position = None
    nodes = []
    for row in range(len(map)):
        for col in range(len(map[0])):
            if(map[row][col] == '0'):
                starting_position = (row, col)
            if(map[row][col] not in ['0','.','#']):
                nodes.append(((row,col), map[row][col]))
    print(starting_position)
    print(nodes)

    shortest_route = sys.maxsize
    next_node = None
    for i in nodes:
        goal = i[1]
        path_length = shortestPath(goal, map, starting_position,0,[], sys.maxsize, [])
        if(path_length < shortest_route):
            next_node = i
            shortest_route = path_length
    print(next_node)
        
    print(shortestPath('4', map, starting_position,0,[], sys.maxsize, []))

    print('runtime: %f seconds' % (time.time() - start))
