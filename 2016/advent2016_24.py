import time
import sys
import random
import itertools
def findMove(position, maze_map):
    if(len(maze_map[position[0]]) > position[1] and maze_map[position[0]][position[1]] != '#'):
        return (position[0],position[1])
    else:
        return -1

def findMove1(position, maze_map):
    dirs = [
        findMove((position[0], position[1] + 1), maze_map),
        findMove((position[0] + 1, position[1]), maze_map),
        findMove((position[0] - 1, position[1]), maze_map), 
        findMove((position[0], position[1] - 1), maze_map)]
    dirs = [x for x in dirs if x != -1]
    return dirs




def BFS(goal, maze_map, start_position):
    history = []
    queue = []
    queue.append(start_position)
    history.append(start_position)
    parents = {}
    steps = 0
    while(len(queue) > 0):
        #if this was queue.pop(), we would have DFS, and would not find shortest path necessarily
        current = queue[0]
        queue = queue[1:]
        children = findMove1(current,maze_map)
        for child in children:     
            if(child not in history):
                parents[child] = current
                history.append(child)
                if(goal == child):
                    x = child
                    #get history
                    while(x != start_position):
                        x = parents[x]
                        steps = steps + 1
                    return steps
                queue.append(child)






if __name__ == '__main__':
    start = time.time()
    input = open('input2016_24.txt', 'r').read().split('\n')[:-1]
   # input = ['###########','#0.1.....2#','#.#######.#','#4.......3#','###########']
   
    maze_map = []
    for row in input:
        row_list = []
        for brick in row:
            row_list.append(brick)
        maze_map.append(row_list)
    starting_position = None
    nodes = {}
    for row in range(len(maze_map)):
        for col in range(len(maze_map[0])):
            if(maze_map[row][col] == '0'):
                starting_position = (row, col)
            if(maze_map[row][col] not in ['0','.','#']):
                nodes[maze_map[row][col]] = (row,col)
    total = 0
    to_delete = None
    # while(len(nodes) > 0):
    #     #check each node for the shortest path
    #     closest_node = None
    #     closest_node_distance = sys.maxsize
    #     for i in nodes:
    #         goal = nodes[i]
    #         if(goal == starting_position):
    #             continue
    #         path_length = BFS(goal,maze_map,starting_position)
    #         if path_length <= closest_node_distance:
    #             closest_node = goal
    #             to_delete = i
    #             closest_node_distance = path_length  
    #     starting_position = closest_node
    #     total = closest_node_distance + total
    #     del nodes[to_delete]
    #     print(total, starting_position)


    #PART 2 
    perms = list(itertools.permutations(list(nodes.keys())))
    min_path = sys.maxsize
    x = 0
    memoization = {}
    for perm in perms:
        zero_added = False
        node_keys = list(nodes.keys())
        random.shuffle(node_keys)
        node_keys = list(perm)
        total = 0
        n = nodes.copy()
        while(len(n) > 0):
            num = node_keys.pop()
            node = n.pop(num)
            path_length = 0
            if((node,starting_position) in memoization):
                path_length = memoization[(node,starting_position)]
            elif((starting_position, node) in memoization):
                path_length = memoization[(starting_position,node)]
            else:
                path_length = BFS(node,maze_map,starting_position)
                memoization[(node,starting_position)] = path_length
            total = total + path_length
            starting_position = node
            if(len(n) == 0 and not zero_added):
                node_keys.append('0')
                n['0'] = (29,27)
                zero_added = True
        if(total < min_path):
            min_path = total
        x = x + 1
    print(min_path)
    print('runtime: %f seconds' % (time.time() - start))


#PART 1: 8381 too high
#PART 2: 708 too high