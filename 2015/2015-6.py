from functools import reduce


lights = [[0 for j in range(1000)] for i in range(1000)]


def prepareString(instruction):
    instruction = instruction.replace('\n', '')
    instruction = instruction.replace('turn on', '1')
    instruction = instruction.replace('turn off', '0')
    instruction = instruction.replace('toggle', '2')
    instruction = instruction.replace('through ','')
    instruction = instruction.split(' ')
    instruction[1] = instruction[1].split(',')
    instruction[2] = instruction[2].split(',')
    instruction[0] = int(instruction[0])
    return instruction

def interpret(inst):
    global lights
    x_beg = int(inst[1][0])
    x_end = int(inst[2][0])
    y_beg = int(inst[1][1])
    y_end = int(inst[2][1])
    for i in range(x_beg, x_end+1):
        for j in range(y_beg, y_end+1):
            if inst[0] == 0:
                if lights[i][j] > 0:
                    lights[i][j] = lights[i][j] - 1
            else:
                lights[i][j] = lights[i][j] + inst[0]
    return True

file = open('input6')
input = file.readlines()
#input = ['turn on 499,499 through 500,500']
prepared = list(map(lambda x : prepareString(x), input))
interpreted = list(map(lambda x: interpret(x), prepared))
total = 0
for i in lights:
    total = total + len(list(filter(lambda x: x == 1, i)))
flat_lights = [item for sub in lights for item in sub]
print(reduce(lambda x,y: x + y, flat_lights))