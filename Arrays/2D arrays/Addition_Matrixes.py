rows=int(input("Enter no.of rows "))
cols=int(input("Enter no.of cols "))
#intialize matrix with zeroes
matrix1=[[0]*cols for k in range(rows)]
matrix2=[[0]*cols for k in range(rows)]
print("Enter values for matrix1")
for i in range(rows):
    for j in range(cols):
        print("Enter value of [{}][{}]".format(i,j))
        matrix1[i][j]=int(input())
print("Enter values for matrix2")
for i in range(rows):
    for j in range(cols):
        print("Enter value of [{}][{}] ".format(i,j))
        matrix2[i][j]=int(input())

print("Elements of matrix1: ")
for r in matrix1:
    print(r)

print("Elemetns of matrix2: ")
for r in matrix2:
    print(r)
    
#intialize third matrix
matrix3=[[0]*cols for k in range(rows)]
for i in range(rows):
    for j in range(cols):
        matrix3[i][j]=matrix1[i][j]+matrix2[i][j]

print("Addtion of Matrices is")
for r in matrix3:
    print(r)