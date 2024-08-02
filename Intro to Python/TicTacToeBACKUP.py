def pressurewasherX(_paramDictMoveLocations,currentPlayerTurn):
    counter = 0
    while(counter!=1):
        try:
            coordinate=input(f'Player {currentPlayerTurn+1}, which space would you like to play?')
            #check if space has already been played
            coordinate =_paramDictMoveLocations.get(coordinate)
            x=coordinate[0]
            y=coordinate[1]
            if(gameBoardpretty[x][y]== 'x' or gameBoardpretty[x][y]== 'o'):
                print('You cannot play there')
            else:
                return coordinate
        except:
            print('try again')

def executeMoveX(character, location, gameboard):
    x=location[0]
    y=location[1]
    gameboard[x][y]=character
    return gameboard


gameBoard=[
    ['','',''],
    ['','',''],
    ['','','']
]

gameBoardpretty=[
    [' ','|',' ','|',' '],
    ['-','+','-','+','-'],
    [' ','|',' ','|',' '],
    ['-','+','-','+','-'],
    [' ','|',' ','|',' '],
]
moveLocation={
    'top left' : [0,0],
    'top middle' : [0,2],
    'top right' : [0,4],
    'middle left' : [2,0],
    'middle' : [2,2],
    'middle right' : [2,4],
    'bottom left' : [4,0],
    'bottom middle' : [4,2],
    'bottom right' : [4,4]
}



for i in range(0,5):
    for k in range(0,5):
        print(f'{gameBoardpretty[i][k]}',end='')
    print(' ')

turn=1
winner=0
while(winner!=1):
    turn+=1
    Turnthing=turn%2
    if(Turnthing==0):
        character='x'
    else:
        character='o'
    IntendedMoveSpot=pressurewasherX(moveLocation,Turnthing) # Cleaned the Values
    print(f'Youre gonna move: {IntendedMoveSpot}')
    gameBoardpretty=executeMoveX(character, IntendedMoveSpot, gameBoardpretty)
    for i in range(0,5):
        for k in range(0,5):
            print(f'{gameBoardpretty[i][k]}',end='')
        print(' ')
    #row win
    if(gameBoardpretty[0][0] == 'x' and gameBoardpretty[0][2] == 'x' and gameBoardpretty [0][4] == 'x' or gameBoardpretty[0][0] == 'o' and gameBoardpretty[0][2] == 'o' and gameBoardpretty [0][4] == 'o' or gameBoardpretty[2][0] == 'x' and gameBoardpretty[2][2] == 'x' and gameBoardpretty [2][4] == 'x' or gameBoardpretty[2][0] == 'o' and gameBoardpretty[2][2] == 'o' and gameBoardpretty [2][4] == 'o' or gameBoardpretty[4][0] == 'x' and gameBoardpretty[4][2] == 'x' and gameBoardpretty [4][4] == 'x' or gameBoardpretty[4][0] == 'o' and gameBoardpretty[4][2] == 'o' and gameBoardpretty [4][4] == 'o'):
        winner=1
        print(f'Player {Turnthing+1} is winner')
    #column win
    if(gameBoardpretty[0][0] == 'x' and gameBoardpretty[2][0] == 'x' and gameBoardpretty [4][0] == 'x' or gameBoardpretty[0][0] == 'o' and gameBoardpretty[2][0] == 'o' and gameBoardpretty [4][0] == 'o' or gameBoardpretty[0][2] == 'x' and gameBoardpretty[2][2] == 'x' and gameBoardpretty [4][2] == 'x' or gameBoardpretty[0][2] == 'o' and gameBoardpretty[2][2] == 'o' and gameBoardpretty [4][2] == 'o' or gameBoardpretty[0][2] == 'x' and gameBoardpretty[2][2] == 'x' and gameBoardpretty [4][2] == 'x' or gameBoardpretty[0][2] == 'o' and gameBoardpretty[2][2] == 'o' and gameBoardpretty [4][2] == 'o'):
        winner=1
        print(f'Player {Turnthing+1} is winner')
    #diagonal win
    if(gameBoardpretty[0][0] == 'x' and gameBoardpretty[2][2] == 'x' and gameBoardpretty[4][4] == 'x' or gameBoardpretty[0][0] == 'o' and gameBoardpretty[2][2] == 'o' and gameBoardpretty[4][4] == 'o' or gameBoardpretty[0][4] == 'x' and gameBoardpretty[2][2] == 'x' and gameBoardpretty[4][0] == 'x' or gameBoardpretty[0][4] == 'o' and gameBoardpretty[2][2] == 'o' and gameBoardpretty[4][0] == 'o'):
        winner=1
        print(f'Player {Turnthing+1} is winner')
    #no winner(draw)
    if(gameBoardpretty[0][0]!=' ' and gameBoardpretty[0][2]!=' ' and gameBoardpretty[0][4]!=' ' and gameBoardpretty[2][0]!=' ' and gameBoardpretty[2][2]!=' ' and gameBoardpretty[2][4]!=' ' and gameBoardpretty[4][0]!=' ' and gameBoardpretty[4][2]!=' ' and gameBoardpretty[4][4]!=' '):
        print('GAME OVER')
        winner=1