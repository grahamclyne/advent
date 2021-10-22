#Hit Points: 71
#Damage: 10
import random
def chooseSpell(spells,p,s,r,mana,b_health,p_health):
    if(b_health < 5):
        return ('mm',53)
    if((r == 0 and mana > 228 and mana < 390) and b_health > 24):
        return ('recharge', 229)
    elif(s == 0 and mana > 112 and p_health > 4):
        return ('shield',113)
    elif(p == 0 and mana > 173):
        return ('poison', 173)
    elif(len(spells) == 0):
        return None
    else:
        return ('mm',53)

    choice = random.choice(spells)
    

    if((choice[0] == 'poison' and p != 0) or (choice[0] == 'shield' and s != 0) or (choice[0] == 'recharge' and r != 0) or (mana - choice[1] < 0)):
        spells.remove(choice)
        return chooseSpell(spells,p,s,r,mana,b_health,p_health)        
    else:
        return choice

def fight(boss_health,player_health,p_armor,p_mana):
    p_timer = 0
    s_timer = 0
    r_timer = 0
    turn_number = 0
    spells = [('mm',53), ('drain',73), ('shield',113),('poison',173),('recharge',229)]
    mana_spent = 0
    spell_order = []
    while(boss_health > 0 and player_health > 0):

        p_armor = 0
        if(p_timer > 0):
            p_timer -= 1
            boss_health -= 3
        if(s_timer > 0):
            s_timer -= 1
            p_armor = 7
        if(r_timer > 0):
            r_timer -= 1
            p_mana += 101
        if(turn_number % 2 == 0):
            player_health -= 1
            if(player_health <= 0):
                return False
            p_spell = chooseSpell(spells,p_timer,s_timer,r_timer,p_mana,boss_health, player_health)
            print('playerturn',boss_health,player_health,p_timer,s_timer,r_timer,p_mana)
            spell_order.append(p_spell)
            print(p_spell)
            if(p_spell == None): #out of mana
                return False
            if(p_spell[0] == 'mm'):
                boss_health -= 4
                mana_spent += 53
            elif(p_spell[0] == 'drain'):
                boss_health -= 2
                player_health +=2
                mana_spent += 73
            elif(p_spell[0] == 'shield'):
                s_timer = 6
                mana_spent +=113
            elif(p_spell[0] == 'poison'):
                p_timer = 6
                mana_spent +=173
            elif(p_spell[0] == 'recharge'):
                r_timer = 5
                mana_spent +=229
            p_mana -= p_spell[1]
        if(boss_health <= 0):
            if(mana_spent < 2050):
                print(spell_order, mana_spent)
            return mana_spent
        if(turn_number % 2 == 1):
            print('bossturn',boss_health,player_health,p_timer,s_timer,r_timer,p_mana)
            player_health -= (10 - p_armor) 
        turn_number += 1
    print('finished', boss_health,player_health)
    return False

mini = 10000
for i in range(10):
    print('\n\n\n')
    result = fight(71,50,0,500) 
    if(result != False):
        if(result < mini):
            print(result)
            mini = result
print(mini)

#2010 is too high for part 1, 1864 too high for part 1