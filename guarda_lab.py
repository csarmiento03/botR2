import numpy as np

cell = [0, 0, 0, 0]
cell[0] = [0, 0, 0, 0]
cell[1] = [0, 0, 0, 0]
cell[2] = [0, 0, 0, 0]
cell[3] = [0, 0, 0, 0]

cell[0][0] = [1,1,0,0]
cell[0][1] = [0,1,0,1]
cell[0][2] = [0,1,0,1]
cell[0][3] = [0,1,1,0]

cell[1][0] = [1,0,0,1]
cell[1][1] = [0,1,1,0]
cell[1][2] = [1,1,0,1]
cell[1][3] = [0,0,1,1]

cell[2][0] = [1,1,1,0]
cell[2][1] = [1,0,0,0]
cell[2][2] = [0,1,0,0]
cell[2][3] = [0,1,1,0]

cell[3][0] = [1,0,0,1]
cell[3][1] = [0,0,1,1]
cell[3][2] = [1,0,1,1]
cell[3][3] = [1,0,1,1]

matrix = np.zeros((4,4))

for indexrow, row in enumerate(cell):
    for indexcol, col in enumerate(row):
        matrix[indexrow, indexcol] = col[0] + 2*col[1] + 4*col[2] + 8*col[3]

matrix[0,1] = matrix[0,1] + 16
matrix[3,2] = matrix[3,2] + 32

np.save("lab", matrix.astype(int))
