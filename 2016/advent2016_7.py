def containsABBA(line):
    return (line[0] == line[3] and line[1] == line[2] and line[1] != line [0])
def containsABA(line):
    if(line[0] == line[2] and line[1] != line[0]):
        return (line[0], line[1])
    else:
        return False

input_raw =  open('input2016_7.txt', 'r').read().split('\n')
hyper_sequence = False
hyper_sequence2 = False
count = 0
ssl = False
for line in input_raw:
    for index in range(len(line)):
        if(index+3 > len(line)):
            break
        if(line[index] == '['):
            hyper_sequence = True
        if(line[index] == ']'):
            hyper_sequence = False
        # if(containsABBA(line[index:index+4]) and hyper_sequence == True):
        #     break
        # if(containsABBA(line[index:index+4]) and hyper_sequence == False):
        #     count = count + 1
        #     print(line[index:index+4])
        #     print(line)
        #     break
        string1 = line[index:index+3]
        tuple = containsABA(line[index:index+3])
        if(tuple != False and hyper_sequence == False):
            for index2 in range(len(line)):
                if(line[index2] == '['):
                    hyper_sequence2 = True
                if(line[index2] == ']'):
                    hyper_sequence2 = False
                if(index2+3 > len(line)):
                    break
                string2 = line[index2:index2+3]
                tuple2 = containsABA(line[index2:index2+3])

                if(tuple2 != False and string1 != string2):

                    if(tuple2[0] == tuple[1] and tuple2[1] == tuple[0] and hyper_sequence2 == True and (index2 >= index + 4 or index2 <= index - 4)):
                        ssl = True
                  #      print(string1,string2)
                        print(string1,string2,line.replace(string1,'___').replace(line[index2:index2+3],'   '))
                        break
        if(ssl):
            ssl = False
            count = count + 1
            break

print(count)

#127 too high 124 too high 118 too high
#part 2 1930 too high, 340 too high, 236 too high,235 too high,234 incorrect, 230 incorrect, 132 incorrect, 232 incorrect, 231 correct answer