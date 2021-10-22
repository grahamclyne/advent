from functools import reduce
def tuplize(h):
    if isinstance(h, tuple):
        return h
    if h == '<':
        return (-1,0)
    elif h == '>':
        return (1,0)
    elif h == 'v':
        return (0,-1)
    elif h == '^':
        return (0,1)  

def tupleAdd(x,y):
    return (x[0] + y[0], x[1] + y[1])    

#this function will cumulatively add up each position up to the position... pretty cool!
def accum(lst):
    return set(reduce(lambda x, y: x + [tupleAdd(y,((0,0) if len(x) == 0 else x[-1]))], lst, [])) 




file = open("input3")
l = file.readlines()
ll = list(l[0])
result = list(map(lambda x: tuplize(x), ll))
accumulator = accum(result)
s = set(accumulator)
print(len(s))

santa = result[0::2]
robo = result[1::2]
santa_route = accum(santa)
robo_route = accum(robo)
print(len(robo_route.union(santa_route)))
