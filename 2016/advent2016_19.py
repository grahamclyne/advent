import time
import math

def findNext(elves, index):
    neighbour = index+1
    if(neighbour == len(elves)):
        neighbour = 0
    while(elves[neighbour] == 0):
        neighbour = neighbour + 1
        if(neighbour == len(elves)):
            neighbour = 0
    return neighbour


def checkEnd(elves):
    count = 0
    for i in elves:
        if(i > 0):
            count = count + 1
        if(count > 1):
            return False
    return True


def calculateNeighbour(index,elves):
   # print('index, len(elves)', index,len(elves))
  #  index = math.floor((len(elves) - zero_count) / 2) + index
    if(index > 0):
        elves_length = len(elves) - (index - 1)
    else:
        elves_length = len(elves)
  #  print('elves_length, index', elves_length, index)
    i = (index + math.floor(elves_length / 2)) 
    if(i >= elves_length):
        i = i % (elves_length)
        i = i - 1
        return i
    else:
        i = i % elves_length
    # if(index >= len(elves) - zero_count):
    #     print('here')
    #     index = index - len(elves)
        return i + index

# def stealGifts(elves):
#     for index in range(len(elves)):
#         if(elves[index][0] == 0):
#             continue
#         if(index+1 == len(elves)):
#             elves[index] = (elves[index][0] + elves[0][0], elves[index][1])
#             elves[0] = (0, elves[0][1])
#         else:
#             elves[index] = (elves[index][0] + elves[index+1][0], elves[index][1])
#             elves[index+1] = (0, elves[index+1][1])
#     return elves

def stealGiftsAcross(index,elves):
    if(index >= len(elves)):
        return elves
    else:
        neighbour = calculateNeighbour(index,elves)
        print(index)
        elves[index] = (elves[index][0] + elves[neighbour][0], elves[index][1])
        elves[neighbour] = (0, elves[neighbour][1])

        print('index, neighbour, elves',index, neighbour,elves)
        # print('\n')

        elves.pop(neighbour)
        return stealGiftsAcross(index+1,elves)

def stealGiftsAcross1(index,elves):
    for index in range(len(elves[:])):
        if(elves[index][0] == 0):
            continue
        neighbour = calculateNeighbour(index,elves)
     #   print('neighbour', neighbour)
        print(index, neighbour)
        if(neighbour >= len(elves)):
            return elves
        elves[index] = (elves[index][0] + elves[neighbour][0], elves[index][1])
        elves[neighbour] = (0, elves[neighbour][1])
        print(index)
      #  print('index, neighbour, elves',index, neighbour,elves)
        #print('\n')
    return elves
if __name__ == '__main__':
    start = time.time()
    elves = 3014387
  #  elves = 5 #test
    count = [(1,x) for x in range(elves)]
    # while(len(count) > 1):
    #     count = stealGifts(count)
    #     count[:] = [x for x in count if x[0] != 0]
    # print(count)
    while(len(count) > 1):
        print('count', len(count))
        count = stealGiftsAcross1(0,count)
        count[:] = [x for x in count if x[0] != 0]
    print(count)        
    print('runtime: %f seconds' % (time.time() - start))
#1004799 too low for part 2, 3014364 too high