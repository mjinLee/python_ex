players = {"name": "Lee", "age": 20, "alive": True, "fav_food": ["🥐", "🧀"]}
# {키 : 값}
print(players.get("age"))  # 20
print(players.get("fav_food"))  # ['🥐', '🧀']
# print(player.get('name'))
print(players["fav_food"])  # ['🥐', '🧀']
# print(player["fav_food"])

print(players)
players.pop("age")  # 삭제
players["xp"] = 1500  # 추가
print(players)

players["fav_food"].append("🍰")
print(players.get("fav_food"))  # ['🥐', '🧀', '🍰']
print(players["fav_food"])  # ['🥐', '🧀', '🍰']


users = {
    "name": "peter",
    "age": 22,
    "alive": True,
    "fav_food": ("🍣", "🍒"),
    "friend": {"name": "parker", "age": 15, "fav_food": ["🍓"]},
}
print(users["friend"]["fav_food"])  # ['🍓']
users["fav_food"] = "🥝"
users.pop("alive")
users["friend"]["fav_food"].append("🍮")
print(users)
