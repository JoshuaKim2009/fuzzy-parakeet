print('Welcome to the guessing game! You shall guess a number from 1 - 100. The number will change every round.')
a=int(input('Type in any number: '))
b=a+1
try:
    if(a==b):
        print('CORRECT! You are so good at guessing!')
    elif(a>=100 or a<=0):
        print('I need a number between 1 and 100. You have 2 more attempts.')
    else:
        print(f'{a} was not the number. Try again.')
except:
    print(f'I need a whole number. You have 2 more attempts.')


t=int(input('Type in another number: '))
j=t+1
try:
    if(t==j):
        print('CORRECT! You are so good at guessing!')
    elif(t>=100 or t<=0):
        print('I need a number between 1 and 100. You have 1 more attempt.')
    else:
        print(f'{t} was not the number. Try again.')
except:
    print(f'I need a whole number. You have 1 more attempt.')


g=int(input('THIS IS YOUR LAST ATTEMPT! Type one last number: '))
l=g+1
try:
    if(g==l):
        print('CORRECT! You are so good at guessing!')
    elif(g>=100 or g<=0):
        print('I needed a number between 1 and 100. You have no more attempts.')
    else:
        print(f'Aw so close. Your guess was {g}. The REAL number was {l}. You have run out of attempts.')
except:
    print('I need a whole number. This was your last attempt.')


print('Thank you for playing the guessing game!')