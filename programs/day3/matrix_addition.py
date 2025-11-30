def addmatrix(matrix1,matrix2):
    if len(matrix1)!=len(matrix2) or len(matrix1[0])!=len(matrix2[0]):
        raise ValueError("the matrix must have same dimensions to perform addition")
    rows=len(matrix1)
    cols=len(matrix1[0])
    result =[[0 for _ in range(cols)]for _ in range(rows)]
    for i in range(rows):
        for j in range(cols):
            result[i][j]=matrix1[i][j]+matrix2[i][j]
    return result
matrixa=[[1,4,6],[3,6,8],[1,0,3]]
matrixb=[[6,7,2],[8,5,8],[5,3,2]]
sum=addmatrix(matrixa,matrixb)
print("the sum of matrix is:")
for rows in sum:
    print(rows)
