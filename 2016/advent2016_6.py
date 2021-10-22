import time
start_time = time.time()
input_raw =  open('input6.txt', 'r').read().split('\n')
test = 'eedadn\n\
drvtee\n\
eandsr\n\
raavrd\n\
atevrs\n\
tsrnev\n\
sdttsa\n\
rasrtv\n\
nssdts\n\
ntnada\n\
svetve\n\
tesnvt\n\
vntsnd\n\
vrdear\n\
dvrsen\n\
enarar'.split('\n')
bucket = [{},{},{},{},{},{},{},{}]
for word in input_raw:
    for index in range(len(word)):
        if(word[index] in bucket[index].keys()):
            bucket[index][word[index]] += 1
        else:
            bucket[index][word[index]] = 1
    
print("--- %s seconds ---" % (time.time() - start_time))