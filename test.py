def newtons_method(f, df, x0, tol=1e-6, max_iter=1000):
    print(f"Starting Newton's Method with initial guess x0 = {x0}")
    x = x0
    for i in range(max_iter):
        fx = f(x)
        dfx = df(x)
        
        print(f"Iteration {i + 1}:")
        print(f"  x = {x}")
        print(f"  f(x) = {fx}")
        print(f"  f'(x) = {dfx}")
        
        if abs(fx) < tol:
            print(f"Converged to solution with f(x) = {fx} (within tolerance).")
            return x
        
        if dfx == 0:
            print("Derivative is zero. No solution found.")
            return None
        
        x = x - fx / dfx 
        print(f"  Updated x = {x}\n")
    
    print("Maximum iterations reached. No solution found.")
    return None

def f(x):
    return x**2 - 2

def df(x):
    return 2*x

root = newtons_method(f, df, x0=1.0)
print(f"\nRoot found using Newton's Method: {root}")


def euler_method(dy_dt, y0, t0, t_end, h):
    print(f"\nStarting Euler's Method with initial condition y({t0}) = {y0} and step size h = {h}")
    t_values = [t0]
    y_values = [y0]
    
    t = t0
    y = y0
    while t < t_end:
        print(f"At t = {t:.2f}, y = {y:.6f}")
        y = y + h * dy_dt(t, y)  
        t += h
        t_values.append(t)
        y_values.append(y)
    
    print(f"Euler's Method completed. Final y({t_end}) = {y_values[-1]:.6f}")
    return t_values, y_values

def dy_dt(t, y):
    return -2 * y + 3

t_values, y_values = euler_method(dy_dt, y0=1, t0=0, t_end=5, h=0.1)

print("\nEuler's Method Solution:")
for t, y in zip(t_values, y_values):
    print(f"t = {t:.2f}, y = {y:.6f}")


def matrix_determinant(matrix):
    """ Calculates the determinant of a 2x2 matrix. """
    det = matrix[0][0] * matrix[1][1] - matrix[0][1] * matrix[1][0]
    print(f"Determinant of matrix {matrix} is {det}")
    return det

def cramer_rule(A, B):
    print(f"\nSolving system of linear equations using Cramer's Rule:")
    print(f"Matrix A = {A}")
    print(f"Matrix B = {B}")
    
    det_A = matrix_determinant(A)
    
    if det_A == 0:
        print("Determinant is zero. No unique solution.")
        return None
    
    A_x = [ [B[0], A[0][1]], [B[1], A[1][1]] ]
    A_y = [ [A[0][0], B[0]], [A[1][0], B[1]] ]
    
    print(f"Matrix A_x = {A_x}")
    print(f"Matrix A_y = {A_y}")
    
    det_A_x = matrix_determinant(A_x)
    det_A_y = matrix_determinant(A_y)
    
    print(f"Determinant of A_x = {det_A_x}")
    print(f"Determinant of A_y = {det_A_y}")
    
    x = det_A_x / det_A
    y = det_A_y / det_A
    
    print(f"Solution: x = {x}, y = {y}")
    return [x, y]

A = [[2, 3], [1, -1]]
B = [5, 1]

solution = cramer_rule(A, B)
print(f"\nSolution using Cramer's Rule: x = {solution[0]}, y = {solution[1]}")
