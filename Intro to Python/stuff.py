def pressurewasherX():
    counter = 0
    while(counter!=1):
        try:
            coordinate=input(f'Direction (use WASD)>> ')
            listOfmoves=['w','a','s','d','W','A','S','D']
            for i in range(0,len(listOfmoves)):
                if(coordinate==listOfmoves[i]):
                    return coordinate
            else:
                print('Beep Boop! Something went wrong!')
        except:
            print('try again')
    
def mover(BoardofGame,thecoordinate,character1):
    x=2
    y=1
    currentposition=BoardofGame[x][y]
    if(thecoordinate=='w' or thecoordinate=='W'):
        if(BoardofGame[x-1][y]=='0'):
            print('You cannot move there')
        elif(BoardofGame[x-1][y]!='0'):
            print('You can move there')
            BoardofGame[x-1][y]=currentposition
            currentposition=character1
            BoardofGame[x][y]=BoardofGame[x-1][y]
            return BoardofGame and currentposition
    if(thecoordinate=='a' or thecoordinate=='A'):
        if(BoardofGame[x][y-1]=='0'):
            print('You cannot move there')
        elif(BoardofGame[x][y-1]!='0'):
            print('You can move there')
            BoardofGame[x][y-1]=currentposition
            currentposition=character1
            BoardofGame[x][y]=BoardofGame[x][y-1]
            return BoardofGame and currentposition
    if(thecoordinate=='s' or thecoordinate=='S'):
        if(BoardofGame[x+1][y]=='0'):
            print('You cannot move there')
        elif(BoardofGame[x+1][y]!='0'):
            print('You can move there')
            BoardofGame[x+1][y]=currentposition
            currentposition=character1
            BoardofGame[x][y]=BoardofGame[x+1][y]
            return BoardofGame and currentposition
    if(thecoordinate=='d' or thecoordinate=='D'):
        if(BoardofGame[x][y+1]=='0'):
            print('You cannot move there')
        elif(BoardofGame[x][y+1]!='0'):
            print('You can move there')
            BoardofGame[x][y+1]=currentposition
            currentposition=character1
            BoardofGame[x][y]=BoardofGame[x][y+1]
            return BoardofGame and currentposition
    



gameboard=[
    [' ',' ','0','0','0','0','0',' '],
    ['0','0','0',' ',' ',' ','0',' '],
    ['0',' ',' ',' ',' ',' ','0',' '],
    ['0','0','0',' ',' ',' ','0','0'],
    ['0','*','0','0',' ',' ',' ','0'],
    ['0',' ','0',' ',' ',' ',' ','0'],
    ['0',' ',' ',' ','*',' ',' ','0'],
    ['0','0','0','0','0','0','0','0']
]


# for i in range(0,len(gameboard)):
#     for k in range(0,len(gameboard[k])):
character='&'
gameboard[2][1]=character

for i in range(0,8):
        for k in range(0,8):
            print(f'{gameboard[i][k]}',end='')
        print(' ')

win=0
while(win!=1):
    Move=pressurewasherX()
    ElCurrentPosition=mover(gameboard,Move,character)
    for i in range(0,8):
        for k in range(0,8):
            print(f'{gameboard[i][k]}',end='')
        print(' ')