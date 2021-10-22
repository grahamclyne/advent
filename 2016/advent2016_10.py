import time
import sys

def takeStep(bots, instructions,outputs):
    for i in range(len(bots)):
        if(len(bots[i]) == 2):
            if(instructions[i][2] == 'O'):
                outputs[instructions[i][0]].append(min(bots[i]))
            else:
                bots[instructions[i][0]].append(min(bots[i]))
            if(instructions[i][3] == 'O'):
                outputs[instructions[i][1]].append(max(bots[i]))
            else:
                bots[instructions[i][1]].append(max(bots[i]))
            bots[i] = []
    return bots


if __name__ == '__main__':
    start = time.time()
    input = open('input2016_10.txt', 'r').read().split('\n')[:-1]
    bots = [[] for x in range(300)]
    outputs = [[] for x in range(100)]
    instructions = {}
    for row in input:
        row = row.split(' ')
        if(row[0] == 'bot'):
            low = ''
            high = ''
            if(row[5] == 'output'):
                low = 'O'
            else:
                low = 'B'
            if(row[9] == 'output'):
                high = 'O'
            else:
                high = 'B'
            instructions[int(row[1])] = (int(row[6]), int(row[11]), low, high)
            
        elif(row[0] == 'value'):
            bots[int(row[5])].append(int(row[1]))
    while(True):
        bots = takeStep(bots,instructions,outputs)
        for i in range(len(bots)):
            if(61 in bots[i] and 17 in bots[i]):
                print('ANSWER',i)
              #  sys.exit(0)
            print(outputs)
    print('runtime: %f seconds' % (time.time() - start))