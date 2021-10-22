from functools import reduce
import re
import time

#for part 1
def getStringLength(string):
    mem_value = string
    print(string)
    string = string.replace('\\\\', '/')
    string = string.replace('\\"', '"')
    string = re.sub('\\\\[x][0-9a-z]{2}', 'H', string)
    print(string, len(string) - 2)
    return len(mem_value) - (len(string) - 2)

def size_in_memory(string):
    assert string[0] == '"'
    assert string[-1] == '"'
    in_mem = string[1:-1]
    in_mem = in_mem.replace("\\\\", "x")
    in_mem = in_mem.replace("\\\"", "x")
    in_mem, _ = re.subn('\\\\x..', 'x', in_mem)
    return len(in_mem)

def size_escaped(string):
    escaped = string
    escaped = escaped.replace("\\", "\\\\")
    escaped = escaped.replace('"', '\\"')
    escaped = '"' + escaped + '"'
    return len(escaped)
#for part 2
def getEncodedLength(string):
    mem_value = string
    print(string)
    string = string.replace('\\\\', '\\\\\\\\')
    string = re.sub('\\\\x', '\\\\\\\\x', string)
    string = string.replace('\\"', '\\\\\\"')
    print(string, len(string) + 4, len(mem_value))
    return (len(string) + 4) - len(mem_value)
#guesses 1824,2099,1877,1499,1277,2085,3435

start = time.time()
file = open('input8')
input = file.readlines()
#input = ['""', '"abc"', '"aaa\\"aaa"', '"\\x27"']
input = list(map(lambda x: x.strip('\n'), input))
str_value = list(map(lambda x: size_escaped(x), input))
mem_value = list(map(lambda x: size_in_memory(x), input))
mem_value = list(map(lambda x: (-x), mem_value))
merged = mem_value + str_value
print(reduce(lambda x,y: x + y, merged))

print('Running time of ',(time.time() - start), ' seconds.')