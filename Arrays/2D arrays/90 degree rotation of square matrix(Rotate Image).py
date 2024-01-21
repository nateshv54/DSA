#90 degree rotation of square matrix
rows=int(input("Enter no.of rows: "))
cols=int(input("Enter no.of cols: "))
matrix1=[[0]*cols for i in range(rows) ]
for i in range(rows):
    for j in range(cols):
        print("Enter value for [{}][{}]".format(i,j))
        matrix1[i][j]=int(input())


def degree90_clock_rotation(matrix1):
    for i in range(rows):
       for j in range(cols):
           matrix1[i][j],matrix1[j][i]=matrix1[j][i],matrix1[i][j]
    for k in range(rows):
       start=0
       end=cols-1
       while(start<end):
           matrix1[k][start],matrix1[k][end]=matrix1[end][k],matrix1[start][k]
           start+=1
           end-=1
        
    return matrix1

degree90_clock_rotation(matrix1)
for k in matrix1:
    print(k)
