
def fight(hhealth,bhealth,pdmg,parm):
    while(hhealth > 0 and bhealth > 0):
        print(bhealth,hhealth)
        bhealth -= (pdmg - 2)
        if(bhealth <= 0):
            return True
        hhealth -= (8 - parm)
    return False
weapons = [(8,4,0),(10,5,0),(25,6,0),(40,7,0),(74,8,0)]
armor = [(0,0,0),(13,0,1),(31,0,2),(53,0,3),(75,0,4),(102,0,5)]
o_rings = [(0,0,0),(25,1,0),(50,2,0),(100,3,0)]
d_rings = [(0,0,0),(20,0,1),(40,0,2),(80,0,3)]
output = []
for i in weapons:
    for j in armor:
        for k in o_rings:
            for l in d_rings:
                output.append((i,j,k,l))
min_cost = 0
for i in output:
    cost = i[0][0] + i[1][0] + i[2][0] + i[3][0]
    dmg = i[0][1] + i[1][1] + i[2][1] + i[3][1]
    amr = i[0][2] + i[1][2] + i[2][2] + i[3][2]

    print(i,cost,dmg,amr)
    result =fight(100,109,dmg,amr)
    if(result == False and cost > min_cost):
        min_cost = cost
print(min_cost)

#115 too high