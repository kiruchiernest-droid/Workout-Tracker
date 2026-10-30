skills = ["welding", "tiling", "upholstery"]
print("Before:", skills)

skills.append("phone repair")
print("After:", skills)

skills.append("graphic design")
print("Final:", skills, )

skills = ["welding", "tiling", "upholstery"]
print("Before:", skills)
# insert copywriting to skills slot 2
skills.insert(1,"copywriting")
print("After:", skills)

#store variables
steps_count = [8800, 6500, 11000, 9200, 7300]

steps_count.append(10500)
steps_count.remove(6500)
steps_count.sort(reverse=True)

print("Final list:", steps_count)

high_days = 0
for s in steps_count:
    if s >= 9000:
        high_days += 1
        print("Days over 9000 steps:", high_days)     
