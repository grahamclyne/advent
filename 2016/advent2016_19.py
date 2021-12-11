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
    if(index > 0):
        elves_length = len(elves) - (index - 1)
    else:
        elves_length = len(elves)
    i = (index + math.floor(elves_length / 2)) 
    if(i >= elves_length):
        i = i % (elves_length)
        i = i - 1
        return i
    else:
        i = i % elves_length
        return i + index

def stealGifts(elves):
    for index in range(len(elves)):
        if(elves[index][0] == 0):
            continue
        if(index+1 == len(elves)):
            elves[index] = (elves[index][0] + elves[0][0], elves[index][1])
            elves[0] = (0, elves[0][1])
        else:
            elves[index] = (elves[index][0] + elves[index+1][0], elves[index][1])
            elves[index+1] = (0, elves[index+1][1])
    return elves

def stealGiftAcross(elf_list,elf,list_length):
    across = (elf + math.floor(list_length/2)) % list_length
  #  print(elf, across,elf_list[across])
    elf_list.pop(across)
    return elf_list

def stealGiftAcrossNoPop(elf_list,elf,list_length,elves,):
    across = (elf + math.floor(list_length / 2) + elves-list_length) % elves
   # print(elf,across,elf_list,list_length, elves)
    elf_list[across] = 0
    return elf_list

if __name__ == '__main__':
    start = time.time()
    length_list = 3014387
  #  length_list = 5 #test
    elf_list = [x+1 for x in range(length_list)]
    elf_index = 0
    while(length_list > 1):
    #    print(elf_list, elf_index)

        elf_list = stealGiftAcross(elf_list,elf_index, length_list)
        length_list = length_list - 1

        if(elf_index == length_list):
            elf_index = 0
        elif(elf_index <= (length_list/2)):
            elf_index = elf_index + 1            
        if(length_list % 1000 == 0):
            print(length_list)
    print(elf_list)
    print('runtime: %f seconds' % (time.time() - start))
#for part 2, if list is 10, answer = 2. if list is 9, answer is 9
#1004799 too low for part 2, 3014364 too high, 905263 too low, 1777336 incorrect