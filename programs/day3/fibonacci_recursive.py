def fib_rec(n):
    if n <= 1:
        return n
    return fib_rec(n - 1) + fib_rec(n - 2)


def fibonacci_recursive(n):
    return [fib_rec(i) for i in range(n)]
