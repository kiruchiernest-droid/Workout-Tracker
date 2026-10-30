students = [
    {"name": "Eric", "grade": "A"},
    {"name": "James", "grade": "B"},
    {"name": "Amina", "grade": "A"}
]
for s in students:
    print(f"{s['name']}: {s['grade']},")

phonebook = {"Eric": "0712345678", "James": "0798765432", "Amina": "0756123456"}
print("=====PHONE CONTACTS=====")
for name, number in phonebook.items():
    print(f"{name} : {number}")
