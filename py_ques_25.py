# Ques - 25 Write python script to multiply two matrix
matrix1 = [[1,2,3],[4,5,6],[7,8,9]]
matrix2 = [[8,3,5],[5,4,2],[1,0,1]]

row_matrix1 = len(matrix1)
row_matrix2= len(matrix2)
col_matrix2 = len(matrix2[0])
result = [[ 0 , 0 , 0],[0,0,0],[0,0,0]]

for i in range(0,row_matrix1):
    for j in range(0,col_matrix2):
        for k in range(0,row_matrix2):
            result[i][j] += matrix1[i][k] * matrix2[k][j]

print(f"Multiplication of two matrix is : {result}")