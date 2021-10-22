import time
import math
import hashlib
import random
def isOpen(letter):
    if(letter in ['b','c','d','e','f']):
        return True
    else:
        return False

def findDirections(passcode, position,history):
    hash = hashlib.md5(passcode.encode("utf-8")).hexdigest()
    directions = []
    hash = hash[0:4]
    #check which directions are open
    if(isOpen(hash[0]) and position > 3 and passcode + 'U' not in history):
        directions.append('U')
    if(isOpen(hash[1]) and position < 12) and passcode + 'D' not in history:
        directions.append('D')
    if(isOpen(hash[2]) and position % 4 != 0 and passcode + 'L' not in history):
        directions.append('L')
    if(isOpen(hash[3]) and (position + 1) % 4 != 0 and passcode + 'R' not in history):
        directions.append('R')
    return directions
        
def applyDirectionToPosition(position, direction):
    if(direction == 'U'):
        position = position - 4
    if(direction == 'D'):
        position = position + 4
    if(direction == 'L'):
        position = position - 1
    if(direction == 'R'):
        position = position + 1
    return position

def unapplyDirectionToPosition(position, direction):
    if(direction == 'U'):
        position = position + 4
    if(direction == 'D'):
        position = position - 4
    if(direction == 'L'):
        position = position + 1
    if(direction == 'R'):
        position = position - 1
    return position

def findPath(passcode,position,history,length):
    if(position == 15):
        return length
    directions = findDirections(passcode,position,history)
    if(directions == []):
        dir = passcode[-1]
        passcode = passcode[0:-1]
        length = length - 1
        position = unapplyDirectionToPosition(position,dir)
        directions = findDirections(passcode,position,history)
    max = 0
    for i in directions:
        history.append(passcode+i)
        l = findPath(passcode+i,applyDirectionToPosition(position,i),history,length+1)
        if(l > max):
            max = l 
    return max

if __name__ == '__main__':
    start = time.time()
    print('max is ', findPath('qljzarfv',0,[],0))
    print('runtime: %f seconds' % (time.time() - start))
