from functools import reduce
import operator


def f(l):
    l.remove(min(l))
    return l
file = open("input2")
l = file.readlines()
ll = list(map(lambda x: x.strip('\n'), l))
lll = list(map(lambda x: x.split('x'), ll))
#2*l*w + 2*w*h + 2*h*l. 
lll = list(map(lambda x: list(map(lambda y: int(y), x)), lll))
m = list(map(lambda x: (2 * x[0] * x[1]) + (2 * x[1] * x[2]) + (2 * x[2] * x[0]) + min((x[0] * x[1]), x[1] * x[2], x[2] * x[0]),lll))
print(reduce(lambda x,y: x + y, m))
bow = list(map(lambda x: x[0] * x[1] * x[2], lll))
ribbon1 = list(map(lambda x: min(x) * 2, lll))
llll = list(map(lambda x: f(x),lll))
print(llll)
ribbon2 = list(map(lambda x: min(x) * 2, lll))
bow = reduce(lambda x,y: x + y, bow)
ribbon1 = reduce(lambda x,y: x + y, ribbon1)
ribbon2 = reduce(lambda x,y: x + y, ribbon2)

print(bow + ribbon1 + ribbon2)


