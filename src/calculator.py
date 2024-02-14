class Calculator:
    def add(a, b):
        return a + b

    def subtract(a, b):
        return a - b

    def multiply(a, b):
        return a * b

    def divide(a, b):
        if b == 0:
            return "Error! Division by zero"
        else:
            return a / b

    def square(a):
        return a * a

    def square_root(a):
        return a ** 0.5

    def cube(a):
        return a * a * a

    def cube_root(a):
        return a ** (1/3)

    def power(a, b):
        return a ** b