def tax_calc(money):
    return money * 0.35


def pay_tax(tax):
    print("thank you for paying", tax)


to_pay = tax_calc(1000000)
pay_tax(to_pay)
pay_tax(tax_calc(10000))


my_name = "Lee"
my_age = 20
my_eyes_color = "brown"

print(f"Hello I'm {my_name}, ")
print(f"I have {my_age} years in the earth, ")
print(f"{my_eyes_color} is my eye color.")
