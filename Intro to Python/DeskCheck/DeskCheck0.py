list=[]
list2=[]
a=int(input('Gimme any number you can think of!'))
if(a<=10 and a>=0):
    list.append(a)
else:
    list2.append(a)
b=int(input('Gimme another number!'))
if(b<=10 and b>=0):
    list.append(b)
else:
    list2.append(b)
c=int(input('Gimme another number!'))
if(c<=10 and c>=0):
    list.append(c)
else:
    list2.append(c)
print(f'These numbers passed: {list}')
print(f'These numbers did not pass: {list2}')