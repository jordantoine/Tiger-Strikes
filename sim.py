import random
baseHaste = float(input ('Unbuffed Haste Rating: '))
baseMs = float(input ('Unbuffed Multistrike Rating: '))
baseAttSpd = float(input ('Attack Speed on Weapon: '))
twoHand = input ('Enter 1 if 2h, 0 if 1h/oh: ')
msPct_base = (baseMs+200)/66+5 #add in buffs
msPct_cur = msPct_base #just setting this up
hastePct = (baseHaste/90)*1.05+5+(55*twoHand) #add in buffs
attSpd = (baseAttSpd/(1+(hastePct/100)))
milliAttSpd = int(attSpd*1000)
t=0 #time, in milliseconds
nextAttack=0 #when's the next autoattack
prevProc=0 #previous tiger strikes proc
tsOff=0 #when tiger strikes will next wear off
tsUt=0 #tiger strikes uptime
tsChance=0.1
while t < 999999999: #27.77 hours
    if t == nextAttack:
        nextAttack = nextAttack + milliAttSpd
        if random.random() <= tsChance:
            msPct_cur = msPct_base + 25
            tsOff = t+8000
            if prevProc == 0 and t != 0:
                prevProc = t #the first proc is annoying
            tsUt = tsUt+min((t-prevProc), 8000)
            prevProc = t
        if random.random() < (msPct_cur/100):    #check 1st multistrike
            if random.random() <= tsChance:
                msPct_cur = msPct_base + 25
                tsOff = t+8000
                if prevProc == 0 and t != 0:
                    prevProc = t #the first proc is annoying
				tsUt = tsUt+min((t-prevProc), 8000)
                prevProc = t
        if random.random() < (msPct_cur/100):    #check 2nd multistrike
            if random.random() <= tsChance:
                msPct_cur = msPct_base + 25
                tsOff = t+8000
                if prevProc == 0 and t != 0:
                    prevProc = t #the first proc is annoying
                tsUt = tsUt+min((t-prevProc), 8000)
                prevProc = t
    if t == tsOff:                                       #turn tiger strikes off
        msPct_cur = msPct_base
    if t == 999999998:
        tsUt = tsUt+min((t-prevProc), 8000)
    t=t+1
print tsUt/999999999.0