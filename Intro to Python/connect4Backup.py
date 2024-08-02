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


    thewinner=0
    #horizontally
    for i in range(0,len(gameBoard)):
        for k in range(0,len(gameBoard[i])-3):
            if(gameBoard[i][k]=='[x]' and gameBoard[i][k+1]=='[x]' and gameBoard[i][k+2]=='[x]' and gameBoard[i][k+3]=='[x]' or gameBoard[i][k]=='[o]' and gameBoard[i][k+1]=='[o]' and gameBoard[i][k+2]=='[o]' and gameBoard[i][k+3]=='[o]'):
                thewinner=1
    #vertically
    for i in range(0,len(gameBoard)-3):
        for k in range(0,len(gameBoard[i])):
            if(gameBoard[i][k]=='[x]' and gameBoard[i+1][k]=='[x]' and gameBoard[i+2][k]=='[x]' and gameBoard[i+3][k]=='[x]' or gameBoard[i][k]=='[o]' and gameBoard[i+1][k]=='[o]' and gameBoard[i+2][k]=='[o]' and gameBoard[i+3][k]=='[o]'):
                thewinner=1
    #diagonally to the right
    for i in range(3,6):
        for k in range(3,-1,-1):
            if(gameBoard[i][k]=='[x]' and gameBoard[i-1][k+1]=='[x]' and gameBoard[i-2][k+2]=='[x]' and gameBoard[i-3][k+3]=='[x]' or gameBoard[i][k]=='[o]' and gameBoard[i-1][k+1]=='[o]' and gameBoard[i-2][k+2]=='[o]' and gameBoard[i-3][k+3]=='[o]'):
                thewinner=1
                
    #diagonally to the left
    for i in range(3,6):
        for k in range(6,3,-1):
            if(gameBoard[i][k]=='[x]' and gameBoard[i-1][k-1]=='[x]' and gameBoard[i-2][k-2]=='[x]' and gameBoard[i-3][k-3]=='[x]' or gameBoard[i][k]=='[o]' and gameBoard[i-1][k-1]=='[o]' and gameBoard[i-2][k-2]=='[o]' and gameBoard[i-3][k-3]=='[o]'):
                thewinner=1
            else:
                pass

    for i in range(0,7):
        for k in range(0,7):
            print(f'{gameBoard[i][k]}',end='')
        print(' ')
        
    if(thewinner==1):
        print('WE HAVE A WINNER!')
        winner=1

