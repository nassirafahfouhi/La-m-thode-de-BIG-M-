# Big M Method Implementation

This project provides a Python implementation of the **Big M Method**, a popular algorithm in linear programming for solving optimization problems with constraints. The script allows users to input their problem data and solves it step by step, while printing the intermediate iterations of the simplex process.

---

## Features

- User-friendly input for the objective function, constraints, and right-hand side values.
- Automatically handles slack, surplus, and artificial variables.
- Uses the Big M constant to penalize artificial variables in the objective function.
- Provides detailed iteration-by-iteration output of the simplex process.
- Detects unbounded or infeasible problems.

---

## Prerequisites

- Python 3.7 or later
- NumPy library

To install NumPy, run the following command:

```bash
pip install numpy
```

---

## How to Use

1. Clone or download the repository.

2. Open the script file.

3. Run the script:

```bash
python BIG_M.py
```

4. Follow the prompts to enter the problem data:

   - Enter the coefficients of the objective function (separated by spaces).
   - Enter the number of constraints.
   - Specify the types of constraints:
     - 1 for ≤
     - 2 for ≥
     - 3 for =
   - Enter the constraint matrix (one row at a time).
   - Enter the right-hand side values (separated by spaces).

5. The program will solve the problem and display the iterations and the final solution.

---

## Example Input

Suppose we want to maximize:

### Input:

```plaintext
Entrez les coefficients de la fonction objectif séparés par des espaces :
2 3

Entrez le nombre de contraintes :
2

Entrez les types de contraintes (1 pour <=, 2 pour >=, 3 pour =) :
1 2

Entrez la matrice des contraintes (une ligne à la fois, les coefficients séparés par des espaces) :
1 2
2 1

Entrez les termes constants des contraintes séparés par des espaces :
8 6
```

---

## Output

The program provides a step-by-step simplex iteration log, showing the following:

- Current iteration number.
- Entering and leaving variables.
- Reduced costs and direction of movement.
- Final solution values.

### Example Output:

```plaintext
Iteration 1:
Entering variable: x2
Leaving variable: x3

Iteration 2:
Entering variable: x1
Leaving variable: x2

Iteration 3:
Optimal solution found!

Final solution:
x1 = 8.0
x2 = 0.0
Maximum value of z = 16.0
```

---

## Functions

### get\_user\_input()

Prompts the user for all required inputs, including:

- Objective function coefficients.
- Constraint matrix.
- Right-hand side values.
- Constraint types.

### big\_m\_method(c, A, b, constraint\_types)

Solves the linear programming problem using the Big M method.

- Handles slack, surplus, and artificial variables.
- Performs simplex iterations.
- Detects unbounded or infeasible solutions.

---

## Limitations

- The script assumes valid numerical inputs from the user.
- Limited to small-to-medium-sized linear programming problems.
- Does not support integer or mixed-integer programming.

---

## Project Contributors

- Nassira Fahfouhi
- Noura Kazdari
- Bouchra Hanyn

---

