
"""
Factorial(0) = 1
Factorial(n) = Factorial(n-1) * n
"""

def factorial(n):
    if n == 0:
        return 1
    else:
        return factorial(n-1) * n
    
print(factorial(5))
