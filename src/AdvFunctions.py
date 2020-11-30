# More complicated functions to implement

# Returns both result of integer division and modulo
def int_division(num1, num2):
    div = num1//num2
    mode = num1%num2
    return [div, mode]

# Returns factorial of given number
def factorial(num):
    fact = 1
    i = 1
    while i <= num:
        fact = i*fact
        i = i+1
    return fact

# Returns all solutions of given quadratic equation
def quadratic_eq(qdr_coef, lin_coef, const):
    disc = (lin_coef**2-4*qdr_coef*const)
    if disc < 0:
        return("There is no real solution")
    elif disc ==0:
        x = -lin_coef/(2*qdr_coef)
        return [x]
    else:
        disc = disc**(1/2)
        x2 = (-lin_coef + disc)/2*qdr_coef
        x1 = (-lin_coef - disc)/2*qdr_coef
        return [x1, x2]




