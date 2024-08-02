list=[]
counter=0
while(counter<5):
    try:
        a=int(input('Type something'))
        if(a<0 or a>4):
            print(f'{a} is not a viable input')
        else:
            list.append(a)
            counter+=1
    except:
        print(f'Oops something went wrong!!')
print(f'{list} are good inputs.')