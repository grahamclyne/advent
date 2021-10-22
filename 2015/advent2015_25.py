def triNum(num):
    return num * (num + 1)/2
first_row = [triNum(x) for x in range(1,10)]
output = [[] for x in range(10)]
output[0] = first_row
for i in range(1,10):
    output[i] = ([output[i-1][x] + (x + i) for x in range(0,len(output[i-1]))])


dim = 10000
output = [[0 for k in range(dim)] for x in range(dim)]
col = 1
row = 1
output[0][0] = 20151125
index = 20151125
max_row = 1
while(col < dim and row < dim):
    if(col + row % 1000 == 0):
        print(row,col)
    output[row][col] = index * 252533 % 33554393
    index = output[row][col]
    if(row == 0):
        max_row += 1
        row = max_row
        col = 0
    elif(row > 0):
        row -= 1
        col += 1
print(output[2979][3084])

print(output[2978][3083])
print(output[2977][3082])
(0,0),(1,0),(0,1),(2,0),(1,1),(0,2),(3,0),(2,1),(1,2),(0,3)
(1,1),(2,1),(1,2),(3,1),(2,2),(1,3),(4,1),(3,2),(2,3),(1,4)
#find row 2978, column 3083
#17136727 too high for part 1