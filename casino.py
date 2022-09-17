from random import randint

print(">>welcome to python casino<<")
pc_choice = randint(1, 100)

playing = True
while playing:
    user_choice = int(input(">>choose number(1-100): "))
    if user_choice == pc_choice:
        print("You won")
        playing = False
    elif user_choice > pc_choice:
        print("lower")
    elif user_choice < pc_choice:
        print("higher")
