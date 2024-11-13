import numpy as np

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

def is_square(A):
    return A.shape[0] == A.shape[1]

def is_symmetric(A):
    return np.array_equal(A, A.T)

def is_positive_definite(A):
    n = A.shape[0]
    for i in range(n):
        if np.linalg.det(A[:i, :i]) <= 0:
            return False
    return True

def max_eigenvalue_exp(A, eps = 1e-6):
    if not is_square(A):
        print("Матриця A не квадратна. Максимальне власне значення не можна знайти")
        return False
    
    i = 1
    print("Ітерація ", i)
    n = A.shape[0]
    x_prev = np.ones(n).reshape(n, 1)
    print("Початкове наближення:\n", x_prev)
    x = A @ x_prev
    print("x:\n", x)

    m = 0 # index of the element to pick
    print ("Обираємо m = ", m + 1)
    l_prev = x[m] / x_prev[m]
    print("λ = ", l_prev)

    while True:
        x_norm = norm(x)
        print("Нормований х:\n", x_norm)
        x_prev = (x / x_norm).reshape(n, 1)
        print("e:\n", x_prev)
        i += 1
        print("Ітерація ", i)
        x = A @ x_prev
        print("x:\n", x)

        l = x[m] / x_prev[m]
        print("λ = ", l)

        print("Перевіримо умову припинення:")
        if np.abs(l - l_prev) <= eps:
            print("Умова виконується")
            return l
        
        print("Умова не виконується")
        l_prev = l

def min_eigenvalue_exp(A, max_eigenvalue):
    if not is_symmetric(A):
        print("Матриця А не симетрична. Мінімальне власне значення не можна знайти")
        return None
    if not is_positive_definite(A):
        print("Матриця А не є додатно визначеною. Мінімальне власне значення не можна знайти")
        return None 
    
    n = A.shape[0]
    E = np.eye(n)
    B = max_eigenvalue * E - A
    print("Матриця B:\n", B)
    B_max_eigenvalue = max_eigenvalue_exp(B)
    print("Максимальне власне значення матриці B:\n", B_max_eigenvalue)
    return max_eigenvalue - B_max_eigenvalue


A = get_matrix()
print("Матриця А:\n", A)

print("Пошук максимального власного значення матриці А")
max_eigenvalue = max_eigenvalue_exp(A)
print("Максимальне власне значення матриці А: ", max_eigenvalue)

print("Пошук мінімального власного значення матриці А")
min_eigenvalue = min_eigenvalue_exp(A, max_eigenvalue)
print("Мінімальне власне значення матриці А: ", min_eigenvalue)
