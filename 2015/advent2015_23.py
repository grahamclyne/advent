import math

input = '''inc a
jio a, +2
tpl a
inc a'''
vars = {'a':1,'b':0}
input = input.replace(',','').split('\n')

input=  open('input23.txt', 'r').read().replace(',','').split('\n')[:-1]

cmds = []
for i in input:
    cmds.append(i.split(' '))
i = 0
while(i < len(cmds)):
    print(i,cmds[i],vars)

    if(cmds[i][0] == 'hlf'):
        vars[cmds[i][1]] = math.floor(vars[cmds[i][1]] / 2) 
        i += 1
    elif(cmds[i][0] == 'tpl'):
        vars[cmds[i][1]] = vars[cmds[i][1]] * 3
        i += 1
    elif(cmds[i][0] == 'inc'):
        vars[cmds[i][1]] = vars[cmds[i][1]] + 1
        i += 1
    elif(cmds[i][0] == 'jmp'):
        i = i + int(cmds[i][1])
    elif(cmds[i][0] == 'jie'):
        if(vars[cmds[i][1]] % 2 == 0):
            i = i + int(cmds[i][2])
        else:
            i += 1
    elif(cmds[i][0] == 'jio'):  
        print(int(vars[cmds[i][1]]) == 1, int(cmds[i][2]))
        if(int(vars[cmds[i][1]]) == 1):
            i = i + int(cmds[i][2])
        else:
            i += 1

print(vars)

#part 1, 1 is wrong answer, 0 is wrong answer

#part 2, 52 is wrong answer