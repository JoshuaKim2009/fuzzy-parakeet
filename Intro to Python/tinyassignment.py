counter=0
while(counter!=1):
    try:
        input=int(input('input here'))
        factorial=input
        if(input<=0):
            print('try again')
        else:
            for i in range(1,input):
                factorial=factorial*i
            counter=1
            print(factorial)
    except:
        print('try again')

