import sys

def countSection(line,total):
    char = 0
    while(char < len(line)):
        if(ord(line[char]) > 64 and ord(line[char]) < 91):
            total = total + 1
        elif(ord(line[char]) == 40):
            tempchar = char
            while(ord(line[char]) != 41):
                char += 1
            temp = line[tempchar+1:char].split('x')
            temp = [int(x) for x in temp]
            total = total + (countSection(line[char+1:char+temp[0]+1],0)) * temp[1] 
            char = char + temp[0]
        char = char + 1
    return total


if __name__ == '__main__':
#solution to part 1
# while(char < len(line)):
#     if(ord(line[char]) > 64 and ord(line[char]) < 91):
#         total = total + 1
#         char += 1
#     elif(ord(line[char]) == 40):
#         tempchar = char
#         while(ord(line[char]) != 41):
#             char += 1
#         print(char)
#         temp = line[tempchar+1:char].split('x')
#         print(temp)
#         total = total + (int(temp[0]) * int(temp[1]))
#         char = char + int(temp[0]) + 1
#     else:
#         char += 1
# print('TOTAL:',total)
    line =  open('input2016_9.txt', 'r').read().split('\n')[0]
   # line = '(25x3)(3x3)ABC(2x3)XY(5x2)PQRSTX(18x9)(3x2)TWO(5x7)SEVEN'
    #line = 'X(8x2)(3x3)ABCY'
#    line = '(27x12)(20x12)(13x14)(7x10)(1x12)A'
    print(countSection(line,0))

#785871 too high
#690320 too high
#74834
#this code has been teed up