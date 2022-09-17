age = int(input("how old are you? "))
print("your age is ", age)
print(type(age))

if age < 18:
    print("you can't drink")
elif age >= 18 and age <= 35:
    print("you drink beer")
elif age == 60 or age == 70:
    print("party!")
else:
    print("go ahead")
