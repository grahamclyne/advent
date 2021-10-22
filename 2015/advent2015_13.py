import time
import random
start_time = time.time()
input_raw =  open('input13.txt', 'r').read().split('\n')[:-1]
tt = []
names = []
for index in range(len(input_raw)):
    tmp = input_raw[index].split(' ')
    name1 = tmp[0]
    name3 = int(tmp[3])
    if(tmp[2] == 'lose'):
         name3 = name3 * -1
    name4 = tmp[-1].replace('.','')
    names.append(name1)
    tt.append([name1, name3, name4])

names = list(set(names))
random.shuffle(names)
for i in names:
    tt.append(['self', 0,i])
    tt.append([i,0,'self'])
names.append('self')
cost = 0
maxx = 0
for i in range(100000):
    cost = 0
    random.shuffle(names)
    for i in range(len(names)):
        next_to = ''
        if(i+1 == len(names)):
            next_to = names[0]
        else:
            next_to = names[i+1]
        for j in tt:
            if(j[0] == names[i] and j[2] == next_to):
                cost = cost + j[1]
    for i in reversed(range(len(names))):
        next_to = ''
        if(i-1 < 0):
            next_to = names[-1]
        else:
            next_to = names[i-1]
        for j in tt:
            if(j[0] == names[i] and j[2] == next_to):
                cost = cost + j[1]   
    if(cost > maxx):
        maxx = cost
print(maxx)