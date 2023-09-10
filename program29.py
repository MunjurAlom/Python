print("---print matrix using nested for loop---")
'''
matrix is two dimentional arry or list
'''

matrix = [
    [1,2,3],
    [4,5,6],
    [7,8,9],
]
matrix[2][1] = 10 #Changing the value of the matrix
'''
matrix[2][2] = 10
print(matrix[1][2])
print(matrix[2][2])
'''
for row in matrix:
    for col in row:
        print(col)