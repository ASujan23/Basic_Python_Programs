a = [[1,2,3],
[4,5,6],
[7,8,9]]
b = [[9,8,7],
[6,5,4],
[3,2,1]]
c = [[0,0,0],[0,0,0],[0,0,0]]
for i in range(len(a)):
    for j in range(len(b)):
        c[i][j] = a[i][b]+b[i][j]
for i in range(len(c)):
    print(c[i])