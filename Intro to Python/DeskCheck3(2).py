list=[False, 5, 7, 'COW', 11, 'MOOSE', 36, 2.3, 53.0, 22.1, ['E', 'E', False], 34, 44]

sum=0

list2=[]
for i in range(0,len(list),1):
    try:
       sum=sum+list[i]
    except:
        pass
print(sum)