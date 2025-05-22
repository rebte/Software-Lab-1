import sys
import math
import os

def is_valid_number(s):
    try:
        float(s)
        return True
    except ValueError:
        return False

def solve_quadratic(a, b, c):
    print(f"Equation is: ({a}) x^2 + ({b}) x + ({c}) = 0")
    if a == 0:
        print("Error. a cannot be 0")
        sys.exit(1)

    d = b ** 2 - 4 * a * c

    if d < 0:
        print("There are 0 roots")
    elif d == 0:
        x = -b / (2 * a)
        print("There are 1 roots")
        print(f"x1 = {x}")
    else:
        x1 = (-b - math.sqrt(d)) / (2 * a)
        x2 = (-b + math.sqrt(d)) / (2 * a)
        print("There are 2 roots")
        print(f"x1 = {x1}")
        print(f"x2 = {x2}")

def interactive_mode():
    while True:
        a = input("a = ")
        if is_valid_number(a):
            a = float(a)
            break
        print(f"Error. Expected a valid real number, got {a} instead")

    while True:
        b = input("b = ")
        if is_valid_number(b):
            b = float(b)
            break
        print(f"Error. Expected a valid real number, got {b} instead")

    while True:
        c = input("c = ")
        if is_valid_number(c):
            c = float(c)
            break
        print(f"Error. Expected a valid real number, got {c} instead")

    solve_quadratic(a, b, c)

def file_mode(filename):
    if not os.path.exists(filename):
        print(f"file {filename} does not exist")
        sys.exit(1)

    try:
        with open(filename, "r") as f:
            content = f.read().strip()
            parts = content.split()
            if len(parts) != 3:
                print("invalid file format")
                sys.exit(1)

            a, b, c = map(float, parts)
            if a == 0:
                print("Error. a cannot be 0")
                sys.exit(1)

            solve_quadratic(a, b, c)

    except Exception:
        print("invalid file format")
        sys.exit(1)

if __name__ == "__main__":
    if len(sys.argv) == 1:
        interactive_mode()
    elif len(sys.argv) == 2:
        file_mode(sys.argv[1])
    else:
        print("Usage: equation [input_file]")
        sys.exit(1)
