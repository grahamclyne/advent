import time
import random
import copy
import numpy as np
from operator import mul
from functools import reduce
start_time = time.time()
input_raw =  open('input15.txt', 'r').read().split('\n')[:-1]
weights = []
for index in range(len(input_raw)):
    tmp = input_raw[index].replace(',','').split(' ')
    weights.append([int(tmp[2]),int(tmp[4]),int(tmp[6]),int(tmp[8])])

for epoch in range(10000):
    teaspoon_dist = [1,1,1,1]
    total = 0
    for index in range(len(weights)):
        score = 0
        for weight in weights[index]:
            score = score + (teaspoon_dist[index] * int(weight))
        total = score * total
weights_abs = []
for index in range(len(weights)):
    m = [sum([x * y for y in weights[index]]) for x in range(100)]
    weights_abs.append(m)
max = 0
print(weights)
#weights = [[-1,-2,6,3],[2,3,-2,-1]]
for i in range(100):
    for j in range(100):
        for k in range(100):
            for l in range(100):
                if(i + j + k + l == 100):
                    weight1 = [x * i for x in weights[0]]
                    weight2 = [x * j for x in weights[1]]
                    weight3 = [x * k for x in weights[2]]
                    weight4 = [x * l for x in weights[3]]
                    calories = 3 * i + 3 * j + 8 * k + (8 * l)
                    y = [sum(x) for x in zip(weight1, weight2, weight3, weight4)]
                    y = [(0 if x < 0 else x) for x in y]
                    total = reduce(mul, y, 1)
                    # print(total, i ,j)
                    if(total > max and calories == 500):
                        print(i,j,k,l)
                        max = total
                        print('MAX',max)

#ou guessed 125000000 too high