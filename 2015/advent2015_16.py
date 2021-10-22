master = {'children':3, 'cats':7, 'samoyeds':2, 'pomeranians':3,'akitas':0, 'vizslas':0, 'goldfish':5, 'trees':3,'cars':2,'perfumes':1}
input_raw =  open('input16.txt', 'r').read().split('\n')[:-1]
input = [x.replace(':','').replace(',','').split(' ') for x in input_raw]
input = [i[2:] for i in input]


for sue in range(len(input)):
    for index in range(0, len(input[sue]) - 1, 2):
        key = input[sue][index]
        value = int(input[sue][index+1])
        if((key == 'cats' or key == 'trees') and master[key] >= value):
            break
        elif((key == 'pomeranians' or key == 'goldfish') and master[key] <= value):
            break
        elif(master[key] != value and key not in ('goldfish', 'pomeranians', 'cats','trees')):
            break
        print(key,value,master[key])
        if(index == len(input[sue])- 2):
            print(sue)

#315 too high