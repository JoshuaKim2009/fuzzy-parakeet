width=int(input('give width'))

for i in range((width+1)//2):
    string=''
    for x in range((width-(i*2+1))//2):
        string=string+'0'
    for k in range(i*2+1):
        string=string+'.'
    for x in range((width-(i*2+1))//2):
        string=string+'0'
    print(string)


'''
0001000
0011100
0111110
1111111
'''