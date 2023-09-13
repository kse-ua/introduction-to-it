def factorial_iterative(n):
    acc = 1
    for i in range (2, n+1):
        acc *= i
    return acc


def factorial_recursive(n):
    if n == 1:
        return 1
    return n * factorial_recursive(n - 1)


print(factorial_iterative(5))
print(factorial_recursive(5))
