week_steps = [9200, 7400, 10500, 8800, 6900, 11000, 9600]

for steps in week_steps:
    if steps >= 8000:

        print("Goal hit.")
    else:
        print("Goal missed")

print("Days_tracked",  len(week_steps))

print("week_steps", week_steps[-1], week_steps[-4])