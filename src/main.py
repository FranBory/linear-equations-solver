def solve_linear_equations(coefficients, constants):
    """
    Solves a system of linear equations using Gaussian elimination.

    Parameters:
    coefficients (list of list of float): The coefficients of the linear equations.
    constants (list of float): The constants of the linear equations.

    Returns:
    list of float: The solution to the system of equations.
    """
    n = len(constants)
    
    # Forward elimination
    for i in range(n):
        # Make the diagonal contain all non-zero elements
        if coefficients[i][i] == 0:
            raise ValueError("Matrix is singular or nearly singular")
        
        for j in range(i + 1, n):
            ratio = coefficients[j][i] / coefficients[i][i]
            for k in range(i, n):
                coefficients[j][k] -= ratio * coefficients[i][k]
            constants[j] -= ratio * constants[i]

    # Back substitution
    solution = [0] * n
    for i in range(n - 1, -1, -1):
        solution[i] = constants[i]
        for j in range(i + 1, n):
            solution[i] -= coefficients[i][j] * solution[j]
        solution[i] /= coefficients[i][i]

    return solution

if __name__ == "__main__":
    # Example usage
    coeffs = [[2, 1, -1], [3, 3, 9], [3, 2, 1]]
    consts = [8, 0, 4]
    solution = solve_linear_equations(coeffs, consts)
    print("Solution:", solution)