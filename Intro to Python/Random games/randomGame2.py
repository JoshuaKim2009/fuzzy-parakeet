print('Welcome to the guessing game!')
a=int(input('Type in any positive number: '))
b=a+1

if(a==b):
    print('CORRECT! You are so good at guessing!')
else:
    print(f'Aw so close! Your guess was {a}. The REAL number was {b}. Try again!')
a=int(input('Type in another number 1 - 100: '))


if(a==b):
    print('CORRECT! You are so good at guessing!')

else:
    print(f'So close again? You are so unlucky. Your guess was {a}. The REAL number was {b}. You have 1 more attempt.')
a=int(input('Type in any number 1 and 100: '))


if(a==b):
    print('CORRECT! You are so good at guessing!')
else:
    print(f'Sorry! Your guess was {a}. The REAL number was {b}. You have run out of attempts.')
print('Thank you for playing the guessing game!')
