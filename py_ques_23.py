# Ques - 23 Write python script to transpose a matrix

matrix = [[1,2,3],
          [4,5,6],
          [7,8,9]]

print(f"Matrix is {matrix}")
row = len(matrix)
col = len(matrix[0])

result = [[0 for _ in range(row)] for _ in range(col)]

for i in range(0,row) :
    for j in range(0,col):
        result[j][i] = matrix[i][j]

print(f"Transpose of a matrix is {result}")
