list=[]
try:
    a=int(input('Type something'))
    if(a<0 or a>4):
        print(f'{a} is not a viable input')
    else:
        list.append(a)
except:
    print(f'Oops something went wrong!!')
try:
    b=int(input('Type another thing'))
    if(b<0 or b>4):
        print(f'{b} is not a viable input')
    else:
        list.append(b)
except:
    print(f'Oops something went wrong!!')
try:
    c=int(input('Type something else'))
    if(c<0 or c>4):
        print(f'{c} is not a viable input')
    else:
        list.append(c)
except:
    print(f'Oops something went wrong!!')
try:
    d=int(input('Type another thing'))
    if(d<0 or d>4):
        print(f'{d} is not a viable input')
    else:
        list.append(d)
except:
    print(f'Oops something went wrong!!')
try:
    e=int(input('Type one more thingy'))
    if(e<0 or e>4):
        print(f'{e} is not a viable input')
    else:
        list.append(e)
except:
    print(f'Oops something went wrong!!')


print(f'These numbers sucessfully passed through the portal: {a}, {b}, {c}, {d} and {e}')