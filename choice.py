from random import randint

user_choice = int(input("Choose number. "))
pc_choice = randint(1, 50)  # imported this

if user_choice == pc_choice:
    print("You won")
elif user_choice > pc_choice:
    print("lower. pc choice is ", pc_choice)
elif user_choice < pc_choice:
    print("higher. pc choice is ", pc_choice)
