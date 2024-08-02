list=[]
notList=[]

print('PLEASE READ: This quiz is a quiz in which you will answer questions. PLEASE ANSWER EITHER "A", "B", "C" or "D". As one of your choices.')
print('What is 1 + 1?')
print('A. 3')
print('B. 11')
print('C. 2')
print('D. 0')
a=input('Answer: ')
if(a=='C'):
    list.append(a)
elif(a!='C'):
    notList.append(a)
else:
    notList.append(a)

print('What is the last name of Obama?')
print('A. Obama')
print('B. Barrack')
print('C. Brocoli')
print('D. No clue')
b=input('Answer: ')
if(b=='A'):
    list.append(b)
elif(b!='Obama'):
    notList.append(b)
else:
    notList.append(b)

print('The Earth is a planet. True or false?')
print('A. True')
print('B. False')
c=input('Answer: ')
if(a=='A'):
    list.append(c)
elif(c!='A'):
    notList.append(c)
else:
    notList.append(c)

print('Whice of these choices are correct?')
print('A. The Earth is flat')
print('B. The Earth is a circle')
print('C. The Earth is a soccer ball')
print('D. The Earth is a globe')
d=input('Answer: ')
if(d=='D'):
    list.append(d)
elif(d!='D'):
    notList.append(d)
else:
    notList.append(d)

print('EXTRA CREDIT (not required)')
print('Is this argument logically valid?:')
print('All animals can speak')
print('A dog is an animal')
print('Therefore all dogs can speak')
print('A. Yes because if all animals can speak, all dogs can speak because dogs are animals.')
print('B. Yes because logical validity assumes that all premises are true and they entail the conclusion. This argument is valid but not sound.')
print('C. No because logical validityC assumes that all premises are true, entailing the conclusion AND they MUST be true themselves. Dogs cannot speak human dialect. Therefore this argument is not logically valid.')
print('D. No because dogs are simply incapable of speaking.')
e=input('ANSWER HERE >> (Type "SKIP" if you do not want to answer): ')
if(e=='B'):
    list.append(e)
elif(e=='SKIP'):
    pass
else:
    notList.append(e)


print('You are done!')
j=len(list)
print(f'Your score is {j}/4.')
print(f'Answers you got correct: {list}')
print(f'Answers you got incorrect: {notList}')
if(j==0):
    print('You need to practice. Your IQ is 72.')
else:
    pass

if(j==1):
    print('You are below average but it is okay! Your IQ is 84.')
else:
    pass

if(j==2):
    print('You are average in terms of smarts. Your IQ is 99. If you work hard, you have potential to be like Einstein!')
else:
    pass

if(j==3):
    print('You are almost at a perfect score! Your IQ is 100,003')
else:
    pass

if(j==4):
    print('4/4? Why did you not get extra credit. You are a failure with an IQ of 0!')
else:
    pass

if(j==5):
    print('5/4? Damn! Your IQ is 180!')
else:
    pass