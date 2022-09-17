"""
days_of_week="Mon,Tue,Wed,Thu,Fri"
print(days_of_week)

days_of_week = ["Mon", "Tue", "Wed", "Thu", "Fri"] # list
print(days_of_week) # ['Mon','Tue','Wed','Thu','Fri']
"""

name = "lee"
print(name.upper())  # LEE
print(name.capitalize())  # Lee
print(name.startswith("l"))  # True
print(name.replace("e", "🥨"))  # l🥨🥨
print(name.endswith("o"))  # False
print(name.endswith("e"))  # True
print(name.isupper())  # False
print("B".isupper())  # True
print("b".isupper())  # False
print(" ".isupper())  # False
