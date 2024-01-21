rows=int(input("Enter the no.of rows: "))
cols=int(input("Enter no.of cols: "))
matrix1=[[0]*cols for k in range(rows)]
for i in range(rows):
    for j in range(cols):
        print("Matrix1 [{}][{}] is ".format(i,j))
        matrix1[i][j]=int(input())

print("transpose of matrix is : ")
#For any matrix
matrix2=[list(row) for row in zip(*matrix1)]

#Method1
matrix3=[[0]*rows for k in range(cols)]
for i in range(rows):
    for j in range(cols):
        matrix3[j][i]=matrix1[i][j]

#For Square_matrix
for i in range(rows,cols):
    for j in range(i+1,cols):
         matrix1[i][j],matrix1[j][i]=matrix1[j][i],matrix1[i][j]


for r in matrix2:
    print(r)