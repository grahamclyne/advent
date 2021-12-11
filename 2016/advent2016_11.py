import time
import sys
import copy
import itertools
import collections 

def checkForConflicts(floor):
    for item in floor:
        if(item[3:] == 'CHIP'):
            if(item[:3] + 'GEN' not in floor):
                for item in floor:
                    if('GEN' in item and item is not item[:3] + "GEN"):
                        return False
    return True 

# def getDirections(elevator_position):
#     directions = []
#     for direction in [-1,1]:
#         if(0 <= (direction + elevator_position) <= 3):
#             directions.append(direction)
#     return directions
        

def getLoads(floortemp):
    floor = copy.deepcopy(floortemp)
    return set(itertools.combinations(floor,2)) | set(itertools.combinations(floor,1))
   

def getStates(elevator_position,in_range, direction, floor_plan):
    states = []
    if(in_range):
        loads = getLoads(floor_plan[elevator_position])
        for load in loads:
            floor_copy = copy.deepcopy(floor_plan)
            for item in load:
                floor_copy[elevator_position].remove(item)
                floor_copy[elevator_position + direction].add(item)
                states.append((floor_copy,elevator_position + direction))
    states = [x for x in states if all(checkForConflicts(y) for y in x[0])]
    return states


def getNewStates(floor_plan, elevator_position):
    states = getStates(elevator_position,elevator_position < 3, 1, floor_plan)
    states = states + getStates(elevator_position,elevator_position > 0, -1, floor_plan)

    return states

def BFSOfStateSpace(elevator_position,floor_plan):
    history = set()
    q = [(floor_plan,0,0)]
    memo = {}
    obj_count = sum([len(floor) for floor in floor_plan])
    master_floor_plan = copy.deepcopy(floor_plan)
    while(len(q) > 0):
        floor_plan,elevator_position,cur_steps = q[0]
        print(cur_steps)
        print(floor_plan,elevator_position)
        # print(q[0])
        # print(next)
        q.remove(q[0])
        # print('floor_plan', len(floor_plan[3]), obj_count)
        
        if(len(floor_plan[3]) == obj_count):
            x = floor_plan
            while(x != master_floor_plan):
                print(x)
                x = memo[id(x)]
            print(x)
            return cur_steps
        states = getNewStates(copy.deepcopy(floor_plan),elevator_position)
        for i in states:
            # print(i)
            if((j := (i[1], count_floor_objects(i[0]))) not in history):
            # print(i)
            # if(i not in history):
                # print('j', j)
                history.add(j)
                q.append((i[0],i[1],cur_steps+1))
                memo[id(i[0])] = floor_plan
    return sys.maxsize


def count_floor_objects(floors):
    return tuple(tuple(collections.Counter(item[3:] for item in floor).most_common()) for floor in floors)

# https://eddmann.com/posts/advent-of-code-2016-day-11-radioisotope-thermoelectric-generators/

if __name__ == '__main__':
    start = time.time()
    #part 1
    input = [set(['PROGEN','PROCHIP']),set(['COLGEN', 'CURGEN','RUTGEN','PLUGEN']),set(['COLCHIP','CURCHIP','RUTCHIP','PLUCHIP']),set()]
    #test
   # input = [set(['HYDCHIP', 'LITCHIP']),set(['HYDGEN']),set(['LITGEN']),set()]
    #part 2
    input = [set(['PROGEN','PROCHIP','ELEGEN','ELECHIP','DILGEN','DILCHIP']),set(['COLGEN', 'CURGEN','RUTGEN','PLUGEN']),set(['COLCHIP','CURCHIP','RUTCHIP','PLUCHIP']),set()]
    test = [set(), {'COLGEN', 'PLUGEN', 'RUTGEN', 'PLUCHIP'}, {'RUTCHIP', 'CURGEN', 'PROGEN', 'PROCHIP'}, {'COLCHIP', 'CURCHIP'}]
    print(checkForConflicts(test[2]))
    steps = BFSOfStateSpace(0,input)
    print('steps',steps)
    # input[0].add("COLCHIP")

    print('runtime: %f seconds' % (time.time() - start))

# 113 too high, 29 incorrect, 37 incorrect, 33 correct
#part 2, 53 not correct
