import random
swingTimer = float(input ('Swing Timer: '))
resetPS = float(input ('Resets per Second: '))
milliAttSpd = int(swingTimer*1000)
resetTime = float(1/resetPS)
milliReset = int(resetTime*1000)
t=0 #time, in milliseconds
nextAttack=0 #when's the next autoattack
nextReset=1 #when's the next reset
swingCount=0
while t < 999999999: #27.77 hours
    if t == nextAttack:
        nextAttack = nextAttack + milliAttSpd
        swingCount = swingCount+1
    if t == nextReset:
		nextAttack = nextReset + milliAttSpd
		nextReset = nextReset + milliReset
    t=t+1
print float(999999999/milliAttSpd)
print swingCount