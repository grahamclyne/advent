from os import cpu_count
import sys

class node(object):
    def __init__(self, size=0, used=0, avail=0, used_percentage=0,location=(0,0),adj_list=[]):
        self.size = size
        self.used = used
        self.avail = avail
        self.used_percentage = used_percentage 
        self.location = location
        self.adj_list = adj_list
    def __str__(self):
        return 'size: ' + str(self.size) + ', used: ' + str(self.used) + ', avail: ' + str(self.avail) + ',location: (' + str(self.location[0]) + ',' + str(self.location[1]) + ')'

def getAdjList(location):
    l1 = (location[0] + 1, location[1])
    l2 = (location[0], location[1] + 1)
    l3 = (location[0] - 1, location[1])
    l4 = (location[0], location[1] - 1)
    l = [l1,l2,l3,l4]
    l = [x for x in l if (x[0] >= 0 and x[0] <= MAX_ROW  and x[1] >= 0 and x[1] <= MAX_COL)]
    return l

def getSteps(pos1, pos2):
    return abs(pos2[0] - pos1[0]) + abs(pos2[1] - pos1[1])

def findAllFreeNodes(nodes, position):
    output = []
    for node in nodes:
        if(nodes[node].avail >= nodes[position].used):
            output.append(node)
    return output

def getClosestFreeNode(avail_nodes,current_node,nodes,data_node):
    least_steps = sys.maxsize
    closest_node = None
    for target_node in avail_nodes:
        cur_steps = getShortestPath(data_node,target_node,current_node,nodes.copy(),0,[],sys.maxsize,False)
        if(cur_steps < least_steps):
            closest_node = target_node
            least_steps = cur_steps
    return (closest_node, least_steps)


def getNextShortestStep(adj_list,target_node):
    #sort nodes in terms of euclidian distance
    output = None
    min_steps = sys.maxsize
    for i in adj_list:
        cur_steps = getSteps(i,target_node)
        if(cur_steps < min_steps):
            min_steps = cur_steps
            output = i
    return output

    
def getShortestPath(data_node,target_node,current_node,nodes,steps,history,min_steps,path_blocked):
    # print('----',data_node,target_node,current_node,steps)
    # print(nodes[current_node].adj_list)
    if(current_node == data_node or current_node in history or nodes[current_node].used > 100):
        return -1
    elif(current_node == target_node):
        return steps
    else:
        history.append(current_node)
        adj_list = nodes[current_node].adj_list.copy()
        print(current_node)
        print(history)
        while(len(adj_list) > 0):
            node = getNextShortestStep(adj_list,target_node)
            adj_list.remove(node)
            path_blocked = False
            print(adj_list) 
            if(node == data_node): ###or nodes[node].used > 100):
                print(nodes[node])
                path_blocked = True
            elif(not path_blocked and getSteps(node,target_node) <= getSteps(current_node,target_node)):
                shortest = getShortestPath(data_node,target_node,node,nodes.copy(),steps+1,history,min_steps,path_blocked)
                if(shortest > 0  and shortest < min_steps):
                    min_steps = shortest
            elif(path_blocked):
                shortest = getShortestPath(data_node,target_node,node,nodes.copy(),steps+1,history,min_steps,path_blocked)
                if(shortest > 0  and shortest < min_steps):
                    min_steps = shortest
                path_blocked = False 

    return min_steps

def moveData(nodes, position_to_fill, position_to_empty):
    nodes[position_to_fill].avail = nodes[position_to_fill].avail - nodes[position_to_empty].used
    nodes[position_to_fill].used = nodes[position_to_fill].used + nodes[position_to_empty].used
    nodes[position_to_empty].avail = nodes[position_to_empty].size
    nodes[position_to_empty].used = 0
    return nodes


if __name__ == "__main__":
    input = list(open('input2016_22.txt').read().split('\n'))[2:-1]
    # input = [
    # '/dev/grid/node-x0-y0   10T    8T     2T   80%',
    # '/dev/grid/node-x0-y1   11T    6T     5T   54%',
    # '/dev/grid/node-x0-y2   32T   28T     4T   87%',
    # '/dev/grid/node-x1-y0    9T    7T     2T   77%',
    # '/dev/grid/node-x1-y1    8T    0T     8T    0%',
    # '/dev/grid/node-x1-y2   11T    7T     4T   63%',
    # '/dev/grid/node-x2-y0   10T    6T     4T   60%',
    # '/dev/grid/node-x2-y1    9T    8T     1T   88%',
    # '/dev/grid/node-x2-y2    9T    6T     3T   66%'
    # ]
    nodes = {}
    MAX_ROW = 31
    MAX_COL = 27
    for row in input:
        splitted = row.split(" ")  
        pruned = [x for x in splitted if x != '']
        size = int(pruned[1][:-1])
        used = int(pruned[2][:-1])
        avail = int(pruned[3][:-1])
        location = pruned[0].split('-')
        location = (int(location[1][1:]), int(location[2][1:]))
        used_percentage = int(pruned[4][:-1])
        adj_list = getAdjList(location)
        print(location)
        nodes[location] = node(size,used,avail,used_percentage,location,adj_list)
        print(nodes[location])



    steps = 0
    for x in range(MAX_ROW, 0, -1):
        data_node = (x,0)
        position = (x-1, 0)
        print('position',position, 'data_node', data_node)
        print(nodes[position])
        avail_nodes = findAllFreeNodes(nodes,position)
        result = getClosestFreeNode(avail_nodes,position,nodes,data_node)
        steps = steps + result[1]

        #   for i in range(len(history)-1):
        #     nodes = moveData(nodes, history[i+1], history[i])
        print(result)
        nodes = moveData(nodes, result[0],position)
        nodes = moveData(nodes, position, data_node)
        steps = steps + 1
        print(steps)
        print('\n')
    print(nodes[(0,0)])

  #6376 too high, 5503 too high, 678 too low
  #part 2, 11058 too high, 159 too low, 160 too low, 179 incorrect,180 incorrect,178 incorrect,209 incorrect
  #this code doesnt really work, but need to find a path around the WALL OF BIG DATA ie go from (30,0) to (8,12) to (24,22)
  #this could have been done by hand, such an annoying question!! took so long to do