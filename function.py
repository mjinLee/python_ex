def say_hi():
    print("hi how r u?")


def say_bye():
    print("bye")
    say_hi()


say_hi()
print("hello world")


def say_hello(user_name, user_age):
    print("hello", user_name, "how r u?")
    print("you are", user_age, "years old")


say_hello("Lee", 20)


def tax_calc(money):
    print(money * 0.35)


tax_calc(1000000)
tax_calc(100)


def say_wow(user_name="anonymous"):
    print("wow", user_name)


say_wow("Lee")
say_wow()


# positional argument
def say_hi(name, age):
    print(f"Hi {name}, you are {age} years old")


say_hi("Lee", 20)
say_hi(name="Lee", age=20)
say_hi(age=20, name="Lee")
