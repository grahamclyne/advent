circuits = {}
import time


def parse(ins):
    global circuits
    ins = ins.strip('\n')
    ins = ins.split(' -> ')
    return ins
def load(instructions):
    global circuits
    for i in instructions:
        circuits[i[1]] = i[0]

def replace(key, val):
    global circuits
    for i in circuits.keys():
        ins = circuits[i]
        #if only points to a variable
        if(ins == key):
            circuits[i] = val
            break
        un_op = 'NOT '
        if(un_op in ins):
            ins = ins.strip(un_op)
            if(ins == key):
                ins = val
                circuits[i] = un_op + ins
        bin_ops = [' AND ', ' OR ', ' LSHIFT ', ' RSHIFT ']
        for op in bin_ops:
            if(op in ins):
                ins = ins.split(op)
                if(ins[0] == key):
                    ins[0] = val
                if(ins[1] == key):
                    ins[1] = val
                circuits[i] = ins[0] + op + ins[1]
                break


def evaluate(ins):
    eval = ins
    if('AND' in ins):
        copy = ins.split(' AND ')
        if(copy[0].isdigit() and copy[1].isdigit()):
            eval = str(int(copy[0]) & int(copy[1]))
        else: 
            eval = ins
    elif('NOT' in ins):
        copy = ins.strip('NOT ')
        if(copy.isdigit()):
            eval = str(~int(copy) & 0xFFFF)
        else:
            eval = ins
    elif('OR' in ins):
        copy = ins.split(' OR ')
        if(copy[0].isdigit() and copy[1].isdigit()):
            eval = str(int(copy[0]) | int(copy[1]))
        else: 
            eval = ins
    elif('LSHIFT' in ins):
        copy = ins.split(' LSHIFT ')
        if(copy[0].isdigit() and copy[1].isdigit()):
            eval = str(int(copy[0]) << int(copy[1]))
        else: 
            eval = ins
    elif('RSHIFT' in ins):       
        copy = ins.split(' RSHIFT ')
        if(copy[0].isdigit() and copy[1].isdigit()):
            eval = str(int(copy[0]) >> int(copy[1]))
        else: 
            eval = ins
    return eval




start = time.time()    
file = open('input7b')
input = file.readlines()
# input = ['123 -> x',
# '456 -> y',
# 'x AND y -> d',
# 'x OR y -> e',
# 'x LSHIFT 2 -> f',
# 'y RSHIFT 2 -> g',
# 'NOT x -> h',
# 'NOT y -> i']
parsed = list(map(lambda x: parse(x), input))
load(parsed)
while(True):
    to_replace = {}
    for i in circuits.keys():
        if (circuits[i].isdigit()):
            to_replace[i] = circuits[i]
    if(len(to_replace.keys()) == len(circuits.keys())):
        break
    for i in to_replace.keys():
        replace(i, to_replace[i])
        continue
    for i in circuits.keys():
        circuits[i] = evaluate(circuits[i])
print(circuits)
print(circuits['a'])

print('Running time of ', time.time() - start, ' seconds.')