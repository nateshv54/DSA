rows=int(input("Enter no.of rows"))
cols=int(input("Enter no.of columns"))
#initilize matrix with zeroes
matrix=[[0]*cols for _ in range(rows)]
print("Enter elements into matrxi")
for i in range(rows):
    for j in range(cols):
        print("Enter value for [{}][{}] index".format(i,j))
        matrix[i][j]=int(input())

print("The 2D array is: ")
for r in matrix:
    print(r)
