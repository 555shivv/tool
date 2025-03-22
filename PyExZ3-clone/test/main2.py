# main2.py

import math

def modulo(a, b):
    if b == 0:
        return "Division by zero error"
    else:
        return a % b

def square_root(a):
    return math.sqrt(a)

def cube_root(a):
    return a ** (1/3)

def percentage(a, b):
    return (a * b) / 100

def main2(a, b):
    result1 = modulo(a, b)
    result2 = square_root(a)
    result3 = cube_root(a)
    result4 = percentage(a, b)
    return result1, result2, result3, result4

if __name__ == "__main__":
    a = 25  # symbolic
    b = 10  # symbolic
    results = main2(a, b)
    print("Modulo of", a, "and", b, "is:", results[0])
    print("Square root of", a, "is:", results[1])
    print("Cube root of", a, "is:", results[2])
    print(b, "percent of", a, "is:", results[3])

