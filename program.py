x = 0
turns = 0
rawlife = raw_input('How much life did he have?(Even #\'s only!) ')
life = int(rawlife)

while True:
    x = x + (2+x)
    turns = turns + 1
    
    if x > 2:
        life = life - (x*2)
    
    if life <= 0 or turns > 47:
        if life <= 0:
            print "You win! Your opponent will be at {:,} life. It will take {:,} turns and you'll have {:,} zombies.".format(life - 4, turns + 1, x)
            break
        elif turns > 47:
            print "You ran out of time! Your opponent will be at {:,} life and you'll have {:,} zombies.".format(life - 4, x)
            break
        else:
            print 'ya goofed'
            break
    else: 
        continue
