list=[0,15,32,44,1,23,11]
currentMax=list[0]
currentMin=list[0]
if(currentMax<list[1]):
    currentMax=list[1]    
if(currentMax<list[2]):
    currentMax=list[2]   
if(currentMax<list[3]):
    currentMax=list[3]   
if(currentMax<list[4]):
    currentMax=list[4] 
if(currentMax<list[5]):
    currentMax=list[5]   
if(currentMax<list[6]):
    currentMax=list[6]   

if(currentMin>list[1]):
    currentMin=list[1]    
if(currentMin>list[2]):
    currentMin=list[2]   
if(currentMin>list[3]):
    currentMin=list[3]   
if(currentMin>list[4]):
    currentMin=list[4] 
if(currentMin>list[5]):
    currentMin=list[5]   
if(currentMin>list[6]):
    currentMin=list[6]  

print(f'The max is {currentMax} and the min is {currentMin}.')