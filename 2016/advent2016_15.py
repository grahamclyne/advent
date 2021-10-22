import time

if __name__ == '__main__':
    start = time.time()
    input = open('input2016_15.txt', 'r').read().split('\n')[:-1]
    num_positions = []
    current_positions = []
    for line in input: 
        positions = int(line.split(' ')[3])
        cur_position = int(line.split(' ')[-1].strip('.'))
        num_positions.append(positions)
        current_positions.append(cur_position)
    
    #TEST DATA
    # num_positions = [5,2]
    # current_positions = [4,1]
    num_positions.append(11)
    current_positions.append(0)
    print(num_positions, current_positions)
    for t in range(10000000):
        for index in range(len(current_positions)):
            eq = (t + (index + 1) + current_positions[index]) % num_positions[index] 
           # print(t, index + 1, current_positions[index], eq)
            if(eq != 0):
                break
            if(index + 1 == len(current_positions)):
                print(t)
                print("FOUND")
        
    print('runtime: %f seconds' % (time.time() - start))
