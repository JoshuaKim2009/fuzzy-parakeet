#turn function
def turnstuff(turn):
    turn+=1
    Turnthing=turn%2
    if(Turnthing==0):
        character='[x]'
    else:
        character='[o]'
    return Turnthing,character

#pressure washing function
def pressurewasherX(currentPlayerTurn):
    counter = 0
    while(counter!=1):
        try:
            coordinate=int(input(f'Player {currentPlayerTurn+1}, which space would you like to play?'))
            listOfColumns=[1,2,3,4,5,6,7,8,9]
            for i in range(0,len(listOfColumns)):
                if(coordinate==listOfColumns[i]):
                    return coordinate
            else:
                print('Beep Boop! Something went wrong!')
        except:
            print('try again')

def gravityAndMove(BoardofGame,thecoordinate,thecharacter,timescolumnplayed):
    for i in range(len(BoardofGame)-2,-1,-1):
        if (BoardofGame[i][thecoordinate-1]!='[ ]' or BoardofGame[i][thecoordinate-1]=='[x]' or BoardofGame[i][thecoordinate-1]=='[o]'):
            pass # Dont do move
        else:
            BoardofGame[i][thecoordinate-1]=f'{thecharacter}' # Execute Move
            return BoardofGame
    return BoardofGame

def winchecker(BoardofGame,thewinner):
    counter=0
    while(counter!=1):
        #horizontally
        for i in range(0,len(BoardofGame)):
            for k in range(0,len(BoardofGame[i])):
                if(BoardofGame[i][k]=='[x]' and BoardofGame[i][k+1]=='[x]' and BoardofGame[i][k+2]=='[x]' and BoardofGame[i][k+3]=='[x]' or BoardofGame[i][k]=='[o]' and BoardofGame[i][k+1]=='[o]' and BoardofGame[i][k+2]=='[o]' and BoardofGame[i][k+3]=='[o]'):
                    counter=1
                    thewinner=1
                    return thewinner
        #vertically
                elif(BoardofGame[i][k]=='[x]' and BoardofGame[i+1][k]=='[x]' and BoardofGame[i+2][k]=='[x]' and BoardofGame[i+3][k]=='[x]' or BoardofGame[i][k]=='[o]' and BoardofGame[i+1][k]=='[o]' and BoardofGame[i+2][k]=='[o]' and BoardofGame[i+3][k]=='[o]'):
                    counter=1
                    thewinner=1
                    return thewinner
        #diagonally to the right
                elif(BoardofGame[i][k]=='[x]' and BoardofGame[i+1][k+1]=='[x]' and BoardofGame[i+2][k+2]=='[x]' and BoardofGame[i+3][k+3]=='[x]' or BoardofGame[i][k]=='[o]' and BoardofGame[i+1][k+1]=='[o]' and BoardofGame[i+2][k+2]=='[o]' and BoardofGame[i+3][k+3]=='[o]'):
                    counter=1
                    thewinner=1
                    return thewinner
                    
        #diagonally to the left
                elif(BoardofGame[i][k]=='[x]' and BoardofGame[i-1][k-1]=='[x]' and BoardofGame[i-2][k-2]=='[x]' and BoardofGame[i-3][k-3]=='[x]' or BoardofGame[i][k]=='[o]' and BoardofGame[i-1][k-1]=='[o]' and BoardofGame[i-2][k-2]=='[o]' and BoardofGame[i-3][k-3]=='[o]'):
                    counter=1
                    thewinner=1
                    return thewinner
                else:
                    pass


            




gameBoard=[
    ['[ ]','[ ]','[ ]','[ ]','[ ]','[ ]','[ ]'],
    ['[ ]','[ ]','[ ]','[ ]','[ ]','[ ]','[ ]'],
    ['[ ]','[ ]','[ ]','[ ]','[ ]','[ ]','[ ]'],
    ['[ ]','[ ]','[ ]','[ ]','[ ]','[ ]','[ ]'],
    ['[ ]','[ ]','[ ]','[ ]','[ ]','[ ]','[ ]'],
    ['[ ]','[ ]','[ ]','[ ]','[ ]','[ ]','[ ]'],
    [' 1 ',' 2 ',' 3 ',' 4 ',' 5 ',' 6 ',' 7 '],
]

# moveLocation={
#     '1' : [?,1],
#     '2' : [?,2],
#     '3' : [?,3],
#     '4' : [?,4],
#     '5' : [?,5],
#     '6' : [?,6],
#     '7' : [?,7],
# }

#board printer
for i in range(0,7):
    for k in range(0,7):
        print(f'{gameBoard[i][k]}',end='')
    print(' ')

#MAIN
listofamount=[]
winner=0
currentturn=0

while(winner!=1):
    currentturn,character=turnstuff(currentturn)
    #print(f'T:{currentturn} C:{character}')
    coordinate=IntendedMoveSpot=pressurewasherX(currentturn)
    print(f'The column you chose is {coordinate}')
    listofamount.append(coordinate)
    gameBoard=gravityAndMove(gameBoard,coordinate,character,listofamount)
    elWinner=winchecker(gameBoard,elWinner)
    if(elWinner==1):
        print('WE HAVE A WINNER!')
    for i in range(0,7):
        for k in range(0,7):
            print(f'{gameBoard[i][k]}',end='')
        print(' ')