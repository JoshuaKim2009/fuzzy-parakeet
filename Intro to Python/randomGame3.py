try:
    a=int(input('Guess the sequence of numbers (You have one guess :D):'))
    b=a+1
    if(a!=b):
        print(f'Your answer: {a}  Aw so close. The answer was {b}.')
    else:
        list.append(a)
except:
    print(f'Oops something went wrong')