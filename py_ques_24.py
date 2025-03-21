# Ques - 24 Write python script to add two matrices

matrix1 = [[1,2,3],[4,5,6],[7,8,9]]
matrix2 = [[8,3,5],[5,4,2],[1,0,1]]

row = len(matrix1)
col = len(matrix2[0])
result = [[0 for _ in range(row)] for _ in range(col)]

for i in range(0,row):
    for j in range(0,col):
        result[i][j] = matrix1[i][j] + matrix2[i][j]

print(f"Addition of two matrix is {result}")