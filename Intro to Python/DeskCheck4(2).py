list=[5, 7, 'COW', 11, 'MOOSE', 36, 2.3, 53.0, 22.1, ['E', 'E', False], 34, 44]
listeven=[]
listnoninteger=[]
sum=0

for i in range(0,len(list),1):
    try:
       sum=sum+list[i]
    except:
        pass

for i in range(0,len(list),1):
    try:
        if(list[i]%2==0):
            listeven.append(list[i])
        else:
            pass
    except:
        listnoninteger.append(list[i])

print(f'The sum is {sum}. The even numbers are {listeven}. The non integers are {listnoninteger}')



