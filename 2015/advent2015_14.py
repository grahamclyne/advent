import time
import random
import copy

start_time = time.time()
input_raw =  open('input14.txt', 'r').read().split('\n')[:-1]
data = []
for index in range(len(input_raw)):
    tmp = input_raw[index].split(' ')
    name = tmp[0]
    speed = int(tmp[3])
    burst = int(tmp[6])
    rest = int(tmp[13])
    data.append([name,speed,burst,rest])
#data = [['Comet', 14,10,127],['Dancer',16,11,162]]
print(data)

tmp_data = copy.deepcopy(data)
scores = [0 for i in range(9)]
distances = [0 for i in range(9)]
for second in range(2503):

    for i in range(len(tmp_data)):
        if(tmp_data[i][2] <= 0 and tmp_data[i][3] <= 0): 
            tmp_data[i][2] = data[i][2]
            tmp_data[i][3] = data[i][3]
            tmp_data[i][2] -= 1
            distances[i] += int(tmp_data[i][1])
        elif(tmp_data[i][2] == 0):
            tmp_data[i][3] -= 1
        else:
            tmp_data[i][2] -= 1
            distances[i] += int(tmp_data[i][1])
    winner = distances.index(max(distances))
    scores[winner] += 1
    print(second+1, winner, scores, distances, tmp_data )
print(scores)
