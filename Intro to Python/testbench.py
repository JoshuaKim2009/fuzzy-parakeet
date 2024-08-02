list=[]
infile='beans.txt'
outfile='greens.txt'
readerFileThing=open("beans.txt",'r')
for i in readerFileThing:
    print(i)

with open (infile, 'r') as f1:
    for line in f1:
        row=line.split(" ")
        list.append(row)
print(list)

with open (outfile, 'r') as f2:
    for line in f2:
        
        

#list.append(i)
#print(list)

# Read= r
# Write = w
# Append = A

#BASH STUFF
#ls (this prints where we are and what we can move)
#cd (move to place)
#cd..(move back a directory)