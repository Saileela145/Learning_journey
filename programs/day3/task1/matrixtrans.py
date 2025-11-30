matrix=[[1,2,3],[3,4,5],[8,6,9]]
rows=len(matrix)
cols=len(matrix[0])
result=[[0 for _ in range(rows)]for _ in range(cols)]
for i in range(rows):
    for j in range(cols):
        result[j][i]=matrix[i][j]
print(result)        
