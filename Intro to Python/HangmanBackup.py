#Generate a random word
#Only allow one character at a time
#Compare to secret word
#Drawing the character

hangmanStages=[
'''
|------|
|      
|
|
|

''',
'''
|------|
|      O
|
|
|
''',
'''
|------|
|      O
|      |
|
|
''',
'''
|------|
|      O
|     /|
|      
|
''',
'''
|------|
|      O
|     /|\\
|      
|
''',
'''
|------|
|      O
|     /|\\
|     /
|
''',
'''
|------|
|      O
|     /|\\
|     / \\
|
''',
]

secretwordlist=['observer', 'hunting', 'chin', 'entertainment', 'shock', 'wound', 'lighter', 'bird', 'reader', 'atmosphere','benny']

alphabet=['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

doubleLetterList=[]

import random
random.seed() #gravs a seed for the random stuff, ! only need once !
x=random.randint(0,len(secretwordlist)-1) # returns a random int from 0-4
SecretWord= secretwordlist[x]


gameboard=[
]

theWord=[
]


print(SecretWord)
for i in range(0, len(SecretWord)):
    gameboard.append('_ ')
gameboard.append(' ')

for i in range(0, len(SecretWord)):
    theWord.append('_')


#for i in range(0,len(theWord)):
#    print(f'{theWord[i]}',end='')
#print(' ')


for i in range(0,len(gameboard)):
    print(f'{gameboard[i]}',end='')
print(' ')


wrongcounter=0
winchecka=0
while(wrongcounter!=6 or winchecka!=1):
    #winchecka
    guessedWord="".join(theWord)
    if(guessedWord==SecretWord):
        print(f'The word was {guessedWord}!')
        winchecka=1
        break

    #powerwasher
    
    counter=0
    while(counter!=1):
        print(hangmanStages[0+wrongcounter])
        guessedLetter = input('Type in a letter')
        try:
            if(len(guessedLetter)==1):
                if(guessedLetter==SecretWord[i]):
                    print(f'You guessed {guessedLetter}')
                    counter+=1
                    break
            elif(len(guessedLetter)!=1):
                print(f'{guessedLetter} 1 is not a valid input. Try again')
            elif(alphabet.index(guessedLetter)==0):
                print(f'{guessedLetter} 2 is not a valid input. Try again') 
            else:
                print(f'{guessedLetter} 3 is not a valid input. Try again')
        except:
            print('try again')

    #comparisons
        for i in range(0,len(SecretWord)):
            if(guessedLetter==SecretWord[i]):
                #indexOfGameboard=SecretWord.index(SecretWord[i]) #where the letter is in the gameboard
                gameboard[i]=guessedLetter+' '
                #gameboard[indexOfGameboard]=guessedLetter+' '
                theWord[i]=guessedLetter
        if(SecretWord.count(guessedLetter)==0):
            print('NotInHereMatey')
            wrongcounter+=1

        for i in range(0,len(gameboard)):
            print(f'{gameboard[i]}',end='')
        print(' ')

    

    