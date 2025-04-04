import unittest
from src.main import solve_linear_equations  # Adjust the import based on the actual function or class name

class TestLinearEquationsSolver(unittest.TestCase):

    def test_solve_linear_equations(self):
        # Test case 1: Simple equations
        coefficients = [[2, 1], [1, -1]]
        constants = [4, 1]
        expected_solution = [3, 1]
        self.assertEqual(solve_linear_equations(coefficients, constants), expected_solution)

        # Test case 2: No solution
        coefficients = [[1, 2], [2, 4]]
        constants = [5, 10]
        with self.assertRaises(ValueError):
            solve_linear_equations(coefficients, constants)

        # Test case 3: Infinite solutions
        coefficients = [[1, 2], [2, 4]]
        constants = [5, 10]
        with self.assertRaises(ValueError):
            solve_linear_equations(coefficients, constants)

        # Test case 4: More complex equations
        coefficients = [[3, 2], [1, 2]]
        constants = [5, 4]
        expected_solution = [1, 2]
        self.assertEqual(solve_linear_equations(coefficients, constants), expected_solution)

if __name__ == '__main__':
    unittest.main()