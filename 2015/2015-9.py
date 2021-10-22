from functools import reduce
import time

def load(x, graph):
    x[0] = x[0].split(' to ')
    graph[x[0][0]] = 


start = time.time()
graph = {}
file = open('input9')
input = file.readlines()
parsed = list(map(lambda x: x.split(' = '), input))
loaded = list(map(lambda x: load(x, graph), parsed))
print(graph)
print('Running time of ',(time.time() - start), ' seconds.')