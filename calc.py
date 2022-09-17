def plus(a=0, b=0):
    print(a + b)


def minus(a=0, b=0):
    print(a - b)


def multiply(a=0, b=0):
    print(a * b)


def divide(a=0, b=0):
    print(a / b)


def power_of(a=0, b=0):
    print(a**b)


def calculator(calc="none", a=0, b=0):
    if calc == "plus":
        plus(a, b)
    elif calc == "minus":
        minus(a, b)
    elif calc == "div":
        divide(a, b)
    elif calc == "mul":
        multiply(a, b)
    elif calc == "pow":
        power_of(a, b)
    else:
        print("wrong data")


calculator("plus", 3, 4)
calculator("mul", 3, 4)
calculator()
