
input =  open('input_triangle.txt', 'r').read()
input = list(map(lambda x:x.strip().split(' '),input.split('\n')[:-1]))
input = [list(map(lambda y: int(y),list(filter(lambda y: y != '', x)))) for x in input]
possible = 0
for tri in input: 
    if((tri[1] + tri[2]) > tri[0] and (tri[0] + tri[1]) > tri[2] and (tri[0] + tri[2]) > tri[1]):
        possible += 1
tri_col = []
print(possible)
for index in range(0,len(input),3):
    for i in range(3):
        tri_col.append([input[index][i], input[index+1][i], input[index+2][i]])  
    
possible = 0
for tri in tri_col: 
    if((tri[1] + tri[2]) > tri[0] and (tri[0] + tri[1]) > tri[2] and (tri[0] + tri[2]) > tri[1]):
        possible += 1
print(possible)