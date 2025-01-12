import numpy as np

# Define the Big M constant (a very large number)
M = 1_000_000

def get_user_input():
    """
    Get user input for the objective function, constraints, and right-hand side values.
    """
    print("Entrez les coefficients de la fonction objectif séparés par des espaces :")
    c = list(map(float, input().split()))

    print("Entrez le nombre de contraintes :")
    num_constraints = int(input())

    print("Entrez les types de contraintes (1 pour <=, 2 pour >=, 3 pour =) :")
    constraint_types = list(map(int, input().split()))

    print("Entrez la matrice des contraintes (une ligne à la fois, les coefficients séparés par des espaces) :")
    A = []
    for _ in range(num_constraints):
        row = list(map(float, input().split()))
        A.append(row)

    print("Entrez les termes constants des contraintes séparés par des espaces :")
    b = list(map(float, input().split()))

    return np.array(c), np.array(A), np.array(b), constraint_types

def big_m_method(c, A, b, constraint_types):
    """
    Solve the linear programming problem using the Big M method.
    """
    num_vars = len(c)  # Number of decision variables
    num_constraints = len(b)  # Number of constraints

    # Initializing the extended objective function and matrix
    c_extended = np.zeros(num_vars + 2 * num_constraints)
    c_extended[:num_vars] = c

    A_extended = np.zeros((num_constraints, num_vars + 2 * num_constraints))
    
    artificial_var_count = 0  # Counter for artificial variables

    for i in range(num_constraints):
        A_extended[i, :num_vars] = A[i]
        
        if constraint_types[i] == 1:  # <= constraint
            A_extended[i, num_vars + i] = 1  # Add slack variable
        elif constraint_types[i] == 2:  # >= constraint
            A_extended[i, num_vars + i] = -1  # Add surplus variable
            A_extended[i, num_vars + num_constraints + artificial_var_count] = 1  # Add artificial variable
            c_extended[num_vars + num_constraints + artificial_var_count] = -M  # Penalize artificial variable
            artificial_var_count += 1
        elif constraint_types[i] == 3:  # = constraint
            A_extended[i, num_vars + num_constraints + artificial_var_count] = 1  # Add artificial variable
            c_extended[num_vars + num_constraints + artificial_var_count] = -M  # Penalize artificial variable
            artificial_var_count += 1

    total_vars = num_vars + 2 * num_constraints

    # Initial basic feasible solution
    basis = list(range(num_vars, num_vars + num_constraints))  # Slack and artificial variables
    non_basis = [i for i in range(total_vars) if i not in basis]

    # Simplex iterations
    max_iterations = 100
    tolerance = 1e-8

    for iteration in range(max_iterations):
        print(f"\nIteration {iteration + 1}:")

        # Extract the basic and non-basic parts of A and c
        B = A_extended[:, basis]
        N = A_extended[:, non_basis]
        c_B = c_extended[basis]
        c_N = c_extended[non_basis]

        # Compute the inverse of the basis matrix
        try:
            B_inv = np.linalg.inv(B)
        except np.linalg.LinAlgError:
            print("Basis matrix is singular. Stopping.")
            break

        # Compute the current solution
        x_B = B_inv @ b
        x = np.zeros(total_vars)
        x[basis] = x_B

        # Compute the reduced costs
        reduced_costs = c_N - c_B @ B_inv @ N

        # Check for optimality
        if np.all(reduced_costs <= tolerance):
            print("Optimal solution found!")
            break

        # Select the entering variable (most positive reduced cost)
        entering_index = np.argmax(reduced_costs)
        entering_var = non_basis[entering_index]

        # Compute the direction of movement
        d = B_inv @ A_extended[:, entering_var]

        # Check for unboundedness
        if np.all(d <= 0):
            print("Problem is unbounded. Stopping.")
            break

        # Select the leaving variable (minimum ratio test)
        ratios = x_B / d
        ratios[d <= 0] = np.inf  # Ignore non-positive entries
        leaving_index = np.argmin(ratios)
        leaving_var = basis[leaving_index]

        # Update the basis and non-basis
        basis[leaving_index] = entering_var
        non_basis[entering_index] = leaving_var

        print(f"Entering variable: x{entering_var + 1}")
        print(f"Leaving variable: x{leaving_var + 1}")

    # Extract the final solution
    x_B = np.linalg.solve(A_extended[:, basis], b)
    x = np.zeros(total_vars)
    x[basis] = x_B

    # Print the results
    print("\nFinal solution:")
    for i in range(num_vars):
        print(f"x{i + 1} = {x[i]}")

    # Check if artificial variables are zero
    if np.any(x[num_vars + num_constraints:] > tolerance):  # Check artificial variables
        print("Warning: Artificial variables are non-zero. The problem may be infeasible.")
    else:
        print(f"Maximum value of z = {c @ x[:num_vars]}")

# Main program
if __name__ == "__main__":
    c, A, b, constraint_types = get_user_input()
    big_m_method(c, A, b, constraint_types)
