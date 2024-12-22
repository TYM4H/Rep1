def is_prime(n):
    div = [int(el) for el in range(1, n+1) if n%el == 0]
    return len(div) == 2

print(is_prime(11))
