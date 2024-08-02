x=[
    [3,3],
    [4,5]
    ]

y=[
    [2,7],
    [8,5]
    ]
result=[
    [0,0],
    [0,0]
    ]
for i in range(len(x)):   
    for k in range(len(x[i])):
        result[i][k]=x[i][k]*y[i][k]
print(result)