def equation(a, b, c):
    d = b**2 - 4*a*c
    x1 = (-b - d**0.5)/(2*a)
    x2 = (-b + d**0.5)/(2*a)
    return x1, x2

