def fibonacci_loop(n):
    if n <= 0:
        return []

    a, b = 0, 1
    result = [a]

    for _ in range(1, n):
        result.append(b)
        a, b = b, a + b

    return result
