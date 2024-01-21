def set_zeroes(matrix1):
    row, col = len(matrix1), len(matrix1[0])
    for i in range(row):
        for j in range(col):
            if matrix1[i][j] == 0:
                #marking ith row elements zero
                for k in range(0,row):
                    if(matrix1[i]):
                        matrix1[i][k]=-1
                #marking j th cols elements zero
                for l in range(0,col):
                    if(matrix1[l][j]):
                        matrix1[l][j]=-1
    
    #Now making marked elements zero
    for i in range(row):
        for j in range(col):
            if matrix1[i][j]==-1:
                matrix1[i][j]=0

    return matrix1


# Example usage:
rows = int(input("Enter the number of rows: "))
cols = int(input("Enter the number of columns: "))
matrix1 = [[0] * cols for _ in range(rows)]

# Input values for the matrix
for i in range(rows):
    for j in range(cols):
        print("Enter value for [{}][{}]".format(i, j))
        matrix1[i][j] = int(input())

set_zeroes(matrix1)

print("Matrix after setting zeroes:")
for r in matrix1:
    print(r)
