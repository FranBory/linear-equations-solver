import numpy as np

# Size of the matrix 
N = 1272

matrix = np.zeros((N, N), dtype=np.float64)

b = np.zeros((N, 1), dtype=np.float64)

a1 = 6

# Fill the matrix matrix with values
for i in range(N-2):
    matrix[i, i] = a1
    matrix[i, i+1] = -1
    matrix[i, i+2] = -1
    matrix[i+1, i] = -1
    matrix[i+2, i] = -1

# Fill the last two rows of matrix
matrix[N-2, N-2] = a1
matrix[N-2, N-1] = -1
matrix[N-1, N-2] = -1
matrix[N-1, N-1] = a1
matrix[N-1, N-2] = -1
matrix[N-2, N-1] = -1

# Fill vector b
for i in range(N):
    b[i, 0] = np.sin(i*4.0)


# Solve the system of equations
# matrix * x = b
x_jac = np.zeros((N, 1), dtype=np.float64)

# Jacobian iteration
for i in range(N):
    x_jac[i, 0] = b[i, 0] / matrix[i, i]
    for j in range(N):
        if i != j:
            x_jac[i, 0] -= matrix[i, j] * x_jac[j, 0] / matrix[i, i]
    
  