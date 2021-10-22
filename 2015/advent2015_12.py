
def searchTree(i,total):
    if(isinstance(i,int)):
        return total + i
    if(isinstance(i,list)):
        for child in i:
            total = searchTree(child,total)
    if(isinstance(i,dict)):
        noGo = False
        for child in i.items():
            if('red' in child):
                noGo =  True
        if(not noGo):
            for child in i.items():    
                total = searchTree(child,total)
    if(isinstance(i,tuple)):
        for child in i:
            total = searchTree(child, total)
    return total
import time
import ast
start_time = time.time()
input_raw =  open('input12.txt', 'r').read()
#input_raw = '[1,"red",5]'
first = ast.literal_eval(input_raw)
total = searchTree(first, 0)
print(total)
print("--- %s seconds ---" % (time.time() - start_time))

#part 2: 94668 too high