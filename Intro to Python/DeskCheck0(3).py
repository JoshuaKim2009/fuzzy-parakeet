def pressurewasher(_lowerbound, _upperbound):
    counter = 0
    while(counter!=1):
        try:
            number=int(input('Give number'))
            if(number<100 and number>0):
                print(f'{number} is between {_lowerbound} and {_upperbound}')
                counter = 1
            else:
                print(f'try again')
        except:
            print('try again')



pressurewasher(0,100)