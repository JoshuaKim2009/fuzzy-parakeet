#~~~ Wordle Outline ~~~#
#Generate a word Create a list of m character words, generate a rand. index, thats your word.
#Generate the grid(board)
#get input
#Compare stuff
#Display somehow (For in word Caps for right spot)
#Wincheck
#   Otherwise display some sort of "not yet" message
#Pressure wash
#Doesn't need to be a real word




secretwordlist=['globe', 'piece', 'piano', 'grand','range', 'resin', 'sushi', 'scope', 'tawny', 'solid',  'guide', 'throw',  'queen',  'pixel', 'candy', 'queue', 'think', 'tardy', 'trust', 'sight', 'sassy', 'green', 'meant', 'actor', 'leash', 'glaze', 'ninja', 'limit', 'trade', 'flare''mania', 'until', 'noise' 'image', 'devil', 'sense', 'often', 'smith', 'piper', 'apart', 'heavy', 'build', 'match', 'ridge', 'stash', 'ascot', 'talon', 'scram', 'pasta', 'never', 'fried', 'stiff', 'place', 'after', 'which', 'repel', 'verge', 'micro', 'cleft', 'alive',]
import random
random.seed() #gravs a seed for the random stuff, ! only need once !
x=random.randint(0,len(secretwordlist)) # returns a random int from 0-4

#print(secretwordlist[x])


gameBoard=[
    ['_ ','_ ','_ ','_ ','_ '],
    ['_ ','_ ','_ ','_ ','_ '],
    ['_ ','_ ','_ ','_ ','_ '],
    ['_ ','_ ','_ ','_ ','_ '],
    ['_ ','_ ','_ ','_ ','_ '],
    ['_ ','_ ','_ ','_ ','_ ']
]

attemptNumber=0



for i in range(0,6):
    for k in range(0,5):
        print(f'{gameBoard[i][k]}',end='')
    print(' ')

SecretWord= secretwordlist[x]
#print(SecretWord)

attemptNumber=0
while(attemptNumber!=6):
    counter=0
    while(counter!=1):
        guessedWord = input('Guess the five letter word')
        try:
            if(len(guessedWord)!=5):
                print(f'{guessedWord} is not a valid word. Try again')
            elif(len(guessedWord)==5):
                print(f'{guessedWord} is a valid word')
                counter+1
                break
            else:
                print(f'{guessedWord} is not a valid word. Try again')
        except:
            print('try again')


    for i in range(0,len(guessedWord)):
        for k in range(0,len(SecretWord)):
            if(guessedWord[i]==SecretWord[k] and i==k):
                print(f'{guessedWord[i]} is in the right spot')
                gameBoard[attemptNumber][i] = guessedWord[i].upper()+' '
                break
            elif(guessedWord[i]==SecretWord[k]):
                print(f'{guessedWord[i]} is somewhere in the word')
                gameBoard[attemptNumber][guessedWord.index(guessedWord[i])] = guessedWord[i].lower()+' '
                break
    attemptNumber=attemptNumber+1           
                
    for i in range(0,6):
        for k in range(0,5):
            print(f'{gameBoard[i][k]}',end='')
        print(' ')

    if(guessedWord==SecretWord):
        attemptNumber=6
        print(f'{guessedWord} is the CORRECT word! You win')




            # We know if the letter is in there somewhere?
            # We also know if the letter is in the correct index. 
