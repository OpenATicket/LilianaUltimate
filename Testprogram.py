turns = 0
rawlife = raw_input('How much life did he have? (Integers only!) ')
rawdcount = raw_input('Cards in deck at end of turn? (Integers only!) ')
try:
    life = int(rawlife)
except:
    print "That's not an integer... is it?"
    quit()

try:    
    dcount = int(rawdcount)
except:
    print "That's not an integer... is ita?"
    quit()

while True:
    x = x + (2+x)
    turns = turns + 1
    
    if x > 2:
        life = life - (x*2)
    
    if life <= 0 or turns > dcount:
        if life <= 0:
            print "You win! Your opponent will be at {:,} life. It will take {:,} turns and you'll have {:,} zombies.".format(life - 4, turns + 1, x)
            break
        elif turns > dcount:
            print "You ran out of time! Your opponent will be at {:,} life and you'll have {:,} zombies.".format(life - 4, x)
            break
        else:
            print 'error'
            break
    else: 
        continue
