from src.BasicFunctions import add, subtract, multiply, divide, power
from tests.TestCore import unit_test


# tests if add() works for zero, positive numbers and negative numbers
def add_test():
    unit_test(16, add, 10.4, 5.6)
    unit_test(-5, add, -10, 5)
    unit_test(5, add, 5, 0)
    unit_test(8, add, 6, 2)


# tests if subtract() works for zero, positive numbers and negative numbers
def subtract_test():
    unit_test(5, subtract, 10.4, 5.4)
    unit_test(-15, subtract, -10, 5)
    unit_test(-5, subtract, -5, 0)


# tests if multiply() works for zero, positive numbers and negative numbers
def multiply_test():
    unit_test(0, multiply, 0, 5)
    unit_test(25, multiply, 5, 5)
    unit_test(-25, multiply, -5, 5)
    unit_test(25, multiply, -5, -5)


# tests if multiply() works for zero, positive numbers and negative numbers
def divide_test():
    unit_test(0, divide, 0, 5)
    unit_test(2, divide, 10, 5)
    unit_test(-2, divide, -10, 5)
    unit_test(0.5, divide, -5, -10)
    # unit_test(ZeroDivisionError, divide, 5, 0)

# test if power
def power_test():
    unit_test(4, power, 2, 2)
    unit_test(8, power, 2, 3)
    unit_test(25, power, 5, 2)
    unit_test(-8, power, -2, 3)
    unit_test(0.25, power, 2, -2)


if __name__ == "__main__":
    add_test()
    subtract_test()
    multiply_test()
    divide_test()
    power_test()

