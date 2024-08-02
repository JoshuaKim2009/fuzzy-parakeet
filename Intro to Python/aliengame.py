#pressure washing function
def pressurewasher(listOfOptions,Turns1):
    counter = 0
    while(counter!=1):
        try:
            print(f'Turn: {Turns1}')
            Choice=input('Which option would you like to pick? (Pick one of the letters)')
            for i in range(0,len(listOfOptions)):
                if(Choice==listOfOptions[i]):
                    return Choice
            else:
                print('Beep Boop! Something went wrong!')
        except:
            print('try again')

def killdeath(MilesTraveled1,health1,Aliens1,killrando1):
    import time
    time.sleep(1)
    print('GAME OVER')
    import time
    time.sleep(1)
    print('Reason: Killed by boss')
    import time
    time.sleep(1)
    print(f'Final Score: {50+MilesTraveled1+health1-Aliens}')
    import time
    time.sleep(1)
    if(50+MilesTraveled1+health1-Aliens1>=90):
        print(f'You are better than {89+killrando1}% of players')
    if(50+MilesTraveled1+health1-Aliens1>=70 and 50+MilesTraveled1+health1-Aliens1<90):
        print('You had a decent run. The aliens are just an annoying hivemind.')
    elif(50+MilesTraveled1+health1-Aliens1>=50 and 50+MilesTraveled1+health1-Aliens1<70):
        print(f'You are better than {40+killrando1}% of players')
    elif(50+MilesTraveled1+health1-Aliens1>=25 and 50+MilesTraveled1+health1-Aliens1<50):
        print(f'You are better than {8+killrando1}% of players')
    elif(50+MilesTraveled1+health1-Aliens1>=0 and 50+MilesTraveled1+health1-Aliens1<25):
        print(f'You are better than {0+killrando1}% of players')
    print('You are a wimp')
    done=1



AlienStartingNumbers=[30,31,32,33,34,35,36,37,38]
AlienAdder=[0,1,2,2,3,3,4,5,6]
DistanceAdder=[10,11,12,13,14,15]
killrandom=[1,2,3,4,5,6,7,8,6,4,3,5,7,8,4,3,2,4]
repairrandomlist=[8,9,10,11]
fightlist=[10,30,50,70]


specialfeatures=[31,42,54,61]

import random
random.seed() #gravs a seed for the random stuff, ! only need once !
k=random.randint(0,len(specialfeatures)-1) # returns a random int from 0-4
special= specialfeatures[k]


import random
random.seed() #gravs a seed for the random stuff, ! only need once !
x=random.randint(0,len(AlienStartingNumbers)-1) # returns a random int from 0-4
Aliens= AlienStartingNumbers[x]

import random
random.seed() #gravs a seed for the random stuff, ! only need once !
y=random.randint(0,len(AlienAdder)-1) # returns a random int from 0-4
Adder= AlienAdder[y]

import random
random.seed() #gravs a seed for the random stuff, ! only need once !
b=random.randint(0,len(repairrandomlist)-1) # returns a random int from 0-4
repairRandom= repairrandomlist[b]
import random
random.seed() #gravs a seed for the random stuff, ! only need once !
z=random.randint(0,len(DistanceAdder)-1) # returns a random int from 0-4
DistanceRandom= DistanceAdder[z]




print(' ')
import time
time.sleep(0.5)
print('WELCOME TO...')
import time
time.sleep(1)
print(
    '''
 █████  █████ ███████████    ███████      
░░███  ░░███ ░░███░░░░░░█  ███░░░░░███    
 ░███   ░███  ░███   █ ░  ███     ░░███   
 ░███   ░███  ░███████   ░███      ░███   
 ░███   ░███  ░███░░░█   ░███      ░███   
 ░███   ░███  ░███  ░    ░░███     ███    
 ░░████████   █████       ░░░███████░     
  ░░░░░░░░   ░░░░░          ░░░░░░░       
'''
)
import time
time.sleep(1)
print(
   '''
 ███████████   █████  █████ ██████   █████
░░███░░░░░███ ░░███  ░░███ ░░██████ ░░███ 
 ░███    ░███  ░███   ░███  ░███░███ ░███ 
 ░██████████   ░███   ░███  ░███░░███░███ 
 ░███░░░░░███  ░███   ░███  ░███ ░░██████ 
 ░███    ░███  ░███   ░███  ░███  ░░█████ 
 █████   █████ ░░████████   █████  ░░█████
░░░░░   ░░░░░   ░░░░░░░░   ░░░░░    ░░░░░ 
'''
)                             

import time
time.sleep(1)
print('You have stolen a UFO to make your way across outer space. the aliens want their UFO back and are chasing you down! Survive and out run the Aliens!')
import time
time.sleep(1)
code=input('Type in a sequence of digits or letters (or both) and remember it for later')
done=0
Turns=0
MilesTraveled=0.0
fuel=15.0
waterlist=[]
Hydration1=60.0
health=0
listOptions=['A','B','C','D','E','Q','a','b','c','d','e','q']
upgrade=1
fuelbooster=0.0
killnumber1=0
killrando=0
DistancefromAliens=MilesTraveled+DistanceRandom-Turns
AmountWater=0.0
killnumber=0
harvestedFuel=0
upgradekiller=1
result=0
alienkillbooster=0
listoshite=[20,30,40,50,60,70,80,90,100,110,120,130,140,150,160,170,180,190,200]

while(done!=1):
    

    

    if(Turns!=5 or Turns!=repairRandom-1):
        print('--------------------------------------------------------------')
        print(' ')
        import time
        time.sleep(0.5)
        print('These are your options:')
        print('A. Drink from your water bottle')
        print('B. Speed boost at moderate speed')
        print('C. Speed boost at full speed')
        print('D. Fuel Refill')
        print('E. Kill Aliens')

        print('SPECIAL OFFERS:')
        #Harvest fuel
        if(killnumber1+killnumber>=10 and killnumber1+killnumber<=19):
            listOptions.append('1')
            print('1. Harvest alien fuel')
        elif(killnumber1+killnumber>=50 and killnumber1+killnumber<=60):
            listOptions.append('1')
            print('1. Harvest alien fuel')
        elif(killnumber1+killnumber>=100 and killnumber1+killnumber<=110):
            listOptions.append('1')
            print('1. Harvest alien fuel')
        else:
            print('None')
        print(' ')
        print('Q. Quit')
        print(' ')
    import time
    time.sleep(0.5)
    print(' ')
    print('STATS:')
    print(' ')
    print(f'Overall Score: {50+MilesTraveled+health-Aliens}')
    print(f'Aliens chasing you: {Aliens}')
    print(f'Aliens killed: {((killnumber1+killnumber)*upgradekiller)+alienkillbooster}')
    print(f'Distance from Aliens: {MilesTraveled+DistanceRandom-Turns+3} miles')
    print(f'Miles traveled: {(MilesTraveled*upgrade//2)*2}')
    print(f'Fuel: {(fuel-MilesTraveled)+fuelbooster+harvestedFuel+0.0}')
    if(Hydration1>=60 and Hydration1<=79):
        print(f'Hydration level: Good')
    elif(Hydration1<50):
        print(f'Hydration level: Poor')
    elif(Hydration1>=80):
        print(f'Hydration level: Over hydrated')
    elif(Hydration1>=50 and Hydration1<=59):
        print(f'Hydration level: Moderate')
    else:
        print(f'Hydration level: Moderate')
    print(Hydration1)
    print(' ')
    if(Aliens<=0):
            print('20 MORE ALIENS HAVE ARRIVED')
            Aliens=20
    for i in range(0,len(listoshite)):
        if(Turns==listoshite[i]):
            print('18 OF MORE ALIENS HAVE ARRIVED')
            Aliens=18
    print('ACHIEVEMENTS:')
    if((MilesTraveled*upgrade//2)*2>=40):
        print('- Long distance runner')
    elif((MilesTraveled*upgrade//2)*2>=60):
        print('- Surviver')
    elif(MilesTraveled+DistanceRandom-Turns+3>=30):
        print('- Keeping distance')
    elif(50+MilesTraveled+health-Aliens>=80):
        print('- Sweat')
    elif(harvestedFuel!=0):
        print('- Fuel farmer')
    elif(Hydration1>=55 and Turns==5):
        print('- Hydrater')
    elif(((killnumber1+killnumber)*upgradekiller)+alienkillbooster>=20):
        print('- Alien Slayer')
    elif(((killnumber1+killnumber)*upgradekiller)+alienkillbooster>=30):
        print('- Aliens be gone!')
    elif(((killnumber1+killnumber)*upgradekiller)+alienkillbooster>=50):
        print('- No holding back!')
    print(' ')
    print('--------------------------------------------------------------')

    import time
    time.sleep(0.5)
    if(Turns==repairRandom-1):
        print('')
        print('SHIP BROKEN DOWN')
        print('')
        puzzle=input(f'In order to repair your ship, enter the code from earlier ') 
        if(puzzle==code):
            print('SHIP REPAIRED')
            pass
        elif(puzzle!=code):
            print('You got it wrong! The number of aliens has increased!')
            Aliens=Aliens+8
        print('--------------------------------------------------------------')


    if(Turns==killrando+11):
        import time
        time.sleep(0.5)
        print('')
        print('On your left there is a speed booster and on your right is a turret upgrade. You can only choose one')
        print('')
        counter = 0
        while(counter!=1):
            try:
                import time
                time.sleep(0.5)
                th=input('Do you want a speed booster or a turret upgrade?')
                if(th=='speed booster' or th=='SPEED BOOSTER' or th=='Speed booster' or th=='Speed Booster' or th=='speed' or th=='SPEED' or th=='Speed'):
                    print('')
                    print('SHIP UPGRADED')
                    print('Speed x3')
                    print('')
                    print('--------------------------------------------------------------')
                    upgrade=3.0
                    counter=1
                elif(th=='turret upgrade' or th=='TURRET UPGRADE' or th=='Turret upgrade' or th=='Turret Upgrade' or th=='turret' or th=='Turret' or th=='TURRET'):
                    print('')
                    print('SHIP UPGRADED')
                    print('Turret power x2')
                    print(' ')
                    print('')
                    print('--------------------------------------------------------------')
                    upgradekiller=2
                    counter=1
                else:
                    Aliens=Aliens+8
                    print('You are too indecisive! The aliens have had enough time to regroup and increase numbers!')
                    counter!=1
            except:
                print('try again')

    # if(Turns==special):
    #     print('')
    #     print('20 NEW ALIENS HAVE ARRIVED!')
    #     risk=input(f'Type "yes" if you want to shoot them and risk death or "no" if you do not want to risk it.')
    #     if((50+MilesTraveled+health-Aliens)/Turns>=6.5):
    #         result=1

    #     elif(risk=='yes' and result==1):
    #         print('')
    #         print('You killed the aliens')
    #         alienkillbooster=20
    #         print('')

    #     print('')

    

    if(Turns==4):
        counter = 0
        while(counter!=1):
            try:
                import time
                time.sleep(0.5)
                speedOrFuel=input('SPEED or FUEL upgrade?')
                print('--------------------------------------------------------------')
                if(speedOrFuel=='speed' or speedOrFuel=='Speed' or speedOrFuel=='SPEED'):
                    upgrade=1.5
                    print(' ')
                    print('ADVANCEMENT: Faster Ship!')
                    print('Speed x1.5')
                    print(' ')
                    counter=1
                elif(speedOrFuel=='fuel' or speedOrFuel=='Fuel' or speedOrFuel=='FUEL'):
                    fuelbooster=20.0
                    print(' ')
                    print('ADVANCEMENT: Oiled up')
                    print('Fuel +20')
                    print('(Fuel will fill completely in 2 turns)')
                    print(' ')
                    print('--------------------------------------------------------------')
                    counter=1
                else:
                    print('Beep Boop! Something went wrong!')
            except:
                print('try again')

    for i in range(0,len(fightlist)):
        bosshealth=50
        yourhealth=40


        if(fightlist[i]==Turns): #THIS IS WHERE I AM
            import time
            time.sleep(0.5)
            print('You have encountered a boss alien who blocks your way!')
            while(bosshealth>=0 or yourhealth>=0):
                chanceofhit=[1,1,2,2,2]
                import random
                random.seed()
                w=random.randint(0,len(chanceofhit)-1)
                randominteger=[0,1,2,3,4,5,6,7,8,9]
                import random
                random.seed() 
                y=random.randint(0,len(randominteger)-1) 
                addingthing= randominteger[y]
                hitornot= chanceofhit[w]
                ShootOrRun=input('Shoot or run?')
                if(ShootOrRun=='shoot' or ShootOrRun=='Shoot' or ShootOrRun=='SHOOT'):
                    print('You shot the boss and...')
                    if(hitornot==1):
                        import time
                        time.sleep(2)
                        print('it missed!')
                    elif(hitornot>=2):
                        import time
                        time.sleep(2)
                        print('it hit!')
                        print(f'-{12+addingthing} health')
                        bosshealth-12+addingthing
                print('Boss chooses to shoot and...')
                if(hitornot==1):
                        time.sleep(2)
                        print('it missed!')
                elif(hitornot>=2):
                    import time
                    time.sleep(2)
                    print('it hit!')
                    print(f'-10')
                    yourhealth-10

                if(bosshealth<=0):
                    print('You killed the boss!')
                elif(yourhealth<=0):
                    print('The boss killed you!')
                    killdeath(MilesTraveled,health,Aliens,killrando)
                elif(ShootOrRun=='run' or ShootOrRun=='Run' or ShootOrRun=='RUN'):
                    if((50+MilesTraveled+health-Aliens)/Turns>=6.5):
                        print('You escaped!')
            print('--------------------------------------------------------------')



    Turns=Turns+1
    ElChoice=pressurewasher(listOptions,Turns)
    if(Hydration1>=80):
        Hydration1=Hydration1-5
    else:
        Hydration1=Hydration1-1
    #Quit
    if(ElChoice=='Q' or ElChoice=='q'):
        done=1
    #Speed
    elif(ElChoice=='B' or ElChoice=='b'):
        MilesTraveled=MilesTraveled+2.0
    #Super speed
    elif(ElChoice=='C' or ElChoice=='c'):
        MilesTraveled=MilesTraveled+3.0
    #Fuel refill
    elif(ElChoice=='D' or ElChoice=='d'):
        fuel=fuel+1.0
        Aliens=Aliens+Adder
    #Kill Aliens
    elif(ElChoice=='E' or ElChoice=='e'):
        if(Aliens>=8):
            import random
            random.seed() #gravs a seed for the random stuff, ! only need once !
            g=random.randint(0,len(killrandom)-1) # returns a random int from 0-4
            killrando=killrandom[g]
            Aliens=Aliens-killrando
            killnumber=killnumber+killrando
        elif(Aliens<8):
            import random
            random.seed() #gravs a seed for the random stuff, ! only need once !
            g=random.randint(0,len(killrandom)-1) # returns a random int from 0-4
            killrando=killrandom[g]
            Aliens=Aliens-killrando+8
            killnumber=killnumber+killrando
    #Drink water
    elif(ElChoice=='A' or ElChoice=='a'):
        MilesTraveled=MilesTraveled+1.0
        waterlist.append('A')
        AmountWater=waterlist.count('A')
        if(Turns>=8 and AmountWater>=Turns/8 and AmountWater<Turns/2):
            Hydration1=Hydration1+10.0
        elif(Turns>=8 and AmountWater>Turns/2):
            Hydration1=Hydration1+10.0
        elif(Turns<=8 and AmountWater>=2):
            Hydration1=Hydration1+10.0
        elif(Turns>=8 and AmountWater<Turns/8):
            Hydration1=Hydration1-10.0
        elif(Turns<=8 and AmountWater==1):
            Hydration1=Hydration1=Hydration1-5.0
        elif(Turns<=8 and AmountWater==0):
            Hydration1=Hydration1-10.0
    #Ship upgrade
    elif(ElChoice=='F'):
        print('')
        print('Ship repaired!')
        print('')
    elif(ElChoice=='1'):
        alreadyplayed=[]
        alreadyplayed.append('1')
        numberOfOnes=alreadyplayed.count('1')
        if(numberOfOnes==1):
            harvestedFuel=killnumber1+killnumber+0.0
        elif(numberOfOnes>1):
            harvestedFuel=killnumber1+killnumber+0.0-harvestedFuel
            if(harvestedFuel==0):
                print(' ')
                print('You have already harvested all the alien fuel for now')
                print(' ')


    elif(Turns==35):
        Aliens=50
        print('AN ALIEN ARMY HAS ARRIVED!')



#Water health
    if(Turns<=30):
        if(Hydration1>=55):
            health=10
        elif(Hydration1<50 or Hydration1>=80):
            health=-10
        else:
            health=2


#DEATHS AND NOTIFICATIONS
    if(MilesTraveled+DistanceRandom-Turns==0):
        import time
        time.sleep(1)
        print('GAME OVER')
        import time
        time.sleep(1)
        print('Reason: Caught by aliens')
        import time
        time.sleep(1)
        print('Distance from aliens: 0 miles')
        import time
        time.sleep(1)
        print(f'Final Score: {50+MilesTraveled+health-Aliens}')
        #stats
        import time
        time.sleep(1)
        if(50+MilesTraveled+health-Aliens>=90):
            print(f'You are better than {89+killrando}% of players')
            print('You survived for a long time but the aliens caught up and reclaimed their UFO.')
        if(50+MilesTraveled+health-Aliens>=70 and 50+MilesTraveled+health-Aliens<90):
            print(f'You are better than {60+killrando}% of players')
            print('You had a decent run but the aliens caught up and reclaimed their UFO.')
        elif(50+MilesTraveled+health-Aliens>=50 and 50+MilesTraveled+health-Aliens<70):
            print(f'You are better than {40+killrando}% of players')
            print('You had an average UFO robbery attempt but the aliens managed to get you.')
        elif(50+MilesTraveled+health-Aliens>=25 and 50+MilesTraveled+health-Aliens<50):
            print(f'You are better than {8+killrando}% of players')
            print('You died too early.')
        elif(50+MilesTraveled+health-Aliens>=0 and 50+MilesTraveled+health-Aliens<25):
            print(f'You are better than {0+killrando}% of players')
            print('You blew it!')
        
        done=1
    elif((fuel-MilesTraveled)+fuelbooster+harvestedFuel+0.0<4.0 and (fuel-MilesTraveled)+fuelbooster+harvestedFuel+0.0!=0.0):
        print('Warning: Fuel is almost out')
    elif((fuel-MilesTraveled)+fuelbooster+harvestedFuel+0.0<=0.0):
        import time
        time.sleep(1)
        print('GAME OVER')
        import time
        time.sleep(1)
        print('Reason: Out of fuel')
        import time
        time.sleep(1)
        print('Fuel: 0 miles')
        import time
        time.sleep(1)
        print(f'Final Score: {50+MilesTraveled+health-Aliens}')
        #stats
        import time
        time.sleep(1)
        if(50+MilesTraveled+health-Aliens>=90):
            print(f'You are better than {89+killrando}% of players')
            print('You survived for a long time but your fuel ran out.')
        if(50+MilesTraveled+health-Aliens>=70 and 50+MilesTraveled+health-Aliens<90):
            print(f'You are better than {60+killrando}% of players')
            print('You had a decent run but your fuel gave out. Make sure to keep track of fuel.')
        elif(50+MilesTraveled+health-Aliens>=50 and 50+MilesTraveled+health-Aliens<70):
            print(f'You are better than {40+killrando}% of players')
            print('You did alright in stealing the UFO but you need to keep better track of your fuel.')
        elif(50+MilesTraveled+health-Aliens>=25 and 50+MilesTraveled+health-Aliens<50):
            print(f'You are better than {8+killrando}% of players')
            print('You died too early. I guess you do not like to feed your UFO oil.')
        elif(50+MilesTraveled+health-Aliens>=0 and 50+MilesTraveled+health-Aliens<25):
            print(f'You are better than {0+killrando}% of players')
            print('You screwed up!')
        done=1
    elif(Hydration1==1):
        print('Warning: You are thirsty')
    elif(Turns>=8 and AmountWater==0):
        import time
        time.sleep(1)
        print('GAME OVER')
        import time
        time.sleep(1)
        print('Reason: Not enough water')
        import time
        time.sleep(1)
        print('Hydration level: Poor')
        import time
        time.sleep(1)
        print(f'Final Score: {50+MilesTraveled+health-Aliens}')
        import time
        time.sleep(1)
        #stats
        if(50+MilesTraveled+health-Aliens>=90):
            print(f'You are better than {89+killrando}% of players')
            print('You did everything right except hydrating yourself.')
        if(50+MilesTraveled+health-Aliens>=70 and 50+MilesTraveled+health-Aliens<90):
            print(f'You are better than {60+killrando}% of players')
            print('You had a good go at it but make sure to hydrate.')
        elif(50+MilesTraveled+health-Aliens>=50 and 50+MilesTraveled+health-Aliens<70):
            print(f'You are better than {40+killrando}% of players')
            print('My guy drink water.')
        elif(50+MilesTraveled+health-Aliens>=25 and 50+MilesTraveled+health-Aliens<50):
            print(f'You are better than {8+killrando}% of players')
            print('You were so thirsty! Drink water!')
        elif(50+MilesTraveled+health-Aliens>=0 and 50+MilesTraveled+health-Aliens<25):
            print(f'You are better than {0+killrando}% of players')
            print('You are selling!')
        done=1
    elif(MilesTraveled+DistanceRandom-Turns==1):
        print('Warning: Aliens close!')
    elif(Aliens>=50):
        import time
        time.sleep(1)
        print('GAME OVER')
        import time
        time.sleep(1)
        print('Reason: Too many aliens')
        import time
        time.sleep(1)
        print(f'Aliens chasing you: {Aliens}')
        import time
        time.sleep(1)
        print(f'Final Score: {50+MilesTraveled+health-Aliens}')
        import time
        time.sleep(1)
        if(50+MilesTraveled+health-Aliens>=90):
            print(f'You are better than {89+killrando}% of players')
            print('You had an amazing run. The aliens just got to you!')
        if(50+MilesTraveled+health-Aliens>=70 and 50+MilesTraveled+health-Aliens<90):
            print(f'You are better than {60+killrando}% of players')
            print('You had a decent run. The aliens are just an annoying hivemind.')
        elif(50+MilesTraveled+health-Aliens>=50 and 50+MilesTraveled+health-Aliens<70):
            print(f'You are better than {40+killrando}% of players')
            print('You had an average attempt. Use your turrets next time.')
        elif(50+MilesTraveled+health-Aliens>=25 and 50+MilesTraveled+health-Aliens<50):
            print(f'You are better than {8+killrando}% of players')
            print('You have turrets you know?!')
        elif(50+MilesTraveled+health-Aliens>=0 and 50+MilesTraveled+health-Aliens<25):
            print(f'You are better than {0+killrando}% of players')
            print('USE YOUR TURRETS!')
        done=1
    elif(Turns>=30 and Hydration1<=40):
        import time
        time.sleep(1)
        print('GAME OVER')
        import time
        time.sleep(1)
        print('Reason: Poor health')
        import time
        time.sleep(1)
        print('Hydration level: Poor')
        import time
        time.sleep(1)
        print(f'Final Score: {50+MilesTraveled+health-Aliens}')
        import time
        time.sleep(1)
        #stats
        if(50+MilesTraveled+health-Aliens>=90):
            print(f'You are better than {89+killrando}% of players')
            print('You did everything right except hydrating yourself.')
        if(50+MilesTraveled+health-Aliens>=70 and 50+MilesTraveled+health-Aliens<90):
            print(f'You are better than {60+killrando}% of players')
            print('You had a good go at it but make sure to hydrate.')
        elif(50+MilesTraveled+health-Aliens>=50 and 50+MilesTraveled+health-Aliens<70):
            print(f'You are better than {40+killrando}% of players')
            print('My guy drink water.')
        elif(50+MilesTraveled+health-Aliens>=25 and 50+MilesTraveled+health-Aliens<50):
            print(f'You are better than {8+killrando}% of players')
            print('You were so thirsty! Drink water!')
        elif(50+MilesTraveled+health-Aliens>=0 and 50+MilesTraveled+health-Aliens<25):
            print(f'You are better than {0+killrando}% of players')
            print('You are selling!')
        done=1
    
    if(done==1):
        import time
        time.sleep(1)
        print('ACHIEVEMENTS:')
        import time
        time.sleep(0.1)
        if(speedOrFuel=='speed' or speedOrFuel=='Speed' or speedOrFuel=='SPEED'):
            print('- Faster Ship!')
        elif(speedOrFuel=='fuel' or speedOrFuel=='Fuel' or speedOrFuel=='FUEL'):    
            import time
            time.sleep(0.1)
            print('- Oiled up')
        elif((MilesTraveled*upgrade//2)*2>=40):
            import time
            time.sleep(0.1)
            print('- Long distance runner')
        elif((MilesTraveled*upgrade//2)*2>=60):
            import time
            time.sleep(0.1)
            print('- Surviver')
        elif(MilesTraveled+DistanceRandom-Turns+3>=30):
            import time
            time.sleep(0.1)
            print('- Keeping distance')
        elif(50+MilesTraveled+health-Aliens>=80):
            import time
            time.sleep(0.1)
            print('- Sweat')
        elif(harvestedFuel!=0):
            import time
            time.sleep(0.1)
            print('- Fuel farmer')
        elif(Hydration1==2 and Turns==5):
            import time
            time.sleep(0.1)
            print('- Hydrater')
        elif(((killnumber1+killnumber)*upgradekiller)+alienkillbooster>=20):
            import time
            time.sleep(0.1)
            print('- Alien Slayer')
        elif(((killnumber1+killnumber)*upgradekiller)+alienkillbooster>=30):
            import time
            time.sleep(0.1)
            print('- Aliens be gone!')
        elif(((killnumber1+killnumber)*upgradekiller)+alienkillbooster>=50):
            import time
            time.sleep(0.1)
            print('- No holding back!')


