days_of_week = ["Mon", "Tue", "Wed", "Thu", "Fri"]  # list
print(days_of_week)  # ['Mon','Tue','Wed','Thu','Fri']
print(days_of_week.count("Wed"))
days_of_week.append("Sat")  # 추가
days_of_week.append("Sun")
print(days_of_week)
days_of_week.remove("Fri")  # 삭제
print(days_of_week)
print(days_of_week[3])  # Thu
days_of_week.reverse()
print(days_of_week)  # ['Sun','Sat','Thu','Wed','Tue','Mon']
days_of_week.clear()
print(days_of_week)  # [] (mutate)

lists = [1, 2, 3, True, False, "hi", [1, 2, [False, True]], "end"]
print(lists[-1])  # end
