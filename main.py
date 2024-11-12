import numpy as np
import sympy as sp

def get_dummy_matrix1():
    return np.array([[2, 1, 0],
                     [1, 2, 1],
                     [0, 1, 2]], dtype=float)

def get_dummy_matrix2():
    return np.array([[2, -1, 0],
                     [-1, 2, -1],
                     [0, -1, 2]], dtype=float)

def get_matrix():
    return np.array([[10, 1, 0, 1],
                     [1, 12, 2, 0],
                     [0, 2, 15, 4],
                     [1, 0, 4, 20]], dtype=float)

def norm(x):
    n = x.size
    sum = 0
    for i in range (n):
        sum += x[i] ** 2
    return np.sqrt(sum)

# перевірити необхідні умови для мошуку мінімального власного значення
# знайти максимальне власне значення
def max_eigenvalue_exp(A, eps = 1e-6): # 
    n = A.shape[0]
    x_prev = np.ones(n).reshape(n, 1)
    x = A @ x_prev

    m = 0 # index of the element to pick
    l_prev = x[m] / x_prev[m]

    while True:
        x_norm = norm(x)
        #x_prev = (x / np.linalg.norm(x)).reshape(n, 1)
        x_prev = (x / x_norm).reshape(n, 1)
        x = A @ x_prev

        l = x[m] / x_prev[m]

        if np.abs(l - l_prev) <= eps:
            return l
        
        l_prev = l

def min_eigenvalue_exp(A, max_eigenvalue):
    n = A.shape[0]
    E = np.eye(n)
    B = max_eigenvalue * E - A

    B_max_eigenvalue = max_eigenvalue_exp(B)
    return max_eigenvalue - B_max_eigenvalue

#A = get_dummy_matrix1()
A = get_dummy_matrix2()
#A = get_matrix()
max_eigenvalue = max_eigenvalue_exp(A)
print(max_eigenvalue)
min_eigenvalue = min_eigenvalue_exp(A, max_eigenvalue)
print(min_eigenvalue)
