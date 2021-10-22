def updatePos(char, curpos):
    if char == 'L' and (curpos - 1 > 0) and (curpos % 3 != 1):
        curpos = curpos - 1
        print(char,curpos)
    if char == 'R' and (curpos + 1 < 10) and (curpos % 3 != 0): # ie not rhs
        curpos = curpos + 1
        print(char,curpos)
    if char == 'U' and (curpos - 3 > 0):
        curpos = curpos - 3
        print(char,curpos)
    if char == 'D' and (curpos + 3 < 10):
        curpos = curpos + 3
        print(char,curpos)
    return curpos
#GUESSED 41B59
def updatePosPart2(char, curpos):
    if char == 'L' and curpos in [3,4,6,7,8,9,11,12]:
        curpos = curpos - 1
        print(char,curpos)

    elif char == 'R' and curpos in [2,3,5,6,7,8,10,11]:
        curpos = curpos + 1
        print(char,curpos)

    elif char == 'U' and curpos in [10,11,12,6,7,8] and curpos - 4 > 0:
        curpos = curpos - 4
        print(char,curpos)
    elif char == 'U' and curpos in [3,13]:
        curpos = curpos - 2
        print(char,curpos)

    elif char == 'D' and curpos in [2,3,4,6,7,8] and curpos + 4 < 14:
        curpos = curpos + 4    
        print(char,curpos)
    elif char == 'D' and curpos in [11,1]:
        curpos = curpos + 2
        print(char,curpos)
    else:
        print("NO CHANGE", char, curpos)
    return curpos

f =  open('input.txt', 'r')
input = f.read()

input = input.split('\n')[:-1]
test = ['ULL',
'RRDDD',
'LURDL',
'UUUUD']
output = []
curpos = 5
for i in input:
    for char in i:
      # curpos = updatePos(char,curpos)
        curpos = updatePosPart2(char,curpos)
    output.append(curpos)
    print('\n')
for i in range(len(output)):
    toletter = {10:'A',11:'B',12:'C',13:'D'}
    if output[i] > 9:
        output[i] = toletter.get(output[i])
print(output)