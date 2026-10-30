daily_steps = [8200, 5100, 11300, 6800, 9400, 4200, 10100]
target = 8000

for day, steps in enumerate(daily_steps, start=1):
    if steps >= 8000:
        status = "Hit target"
    else:
        status = "Did not hit target"

    print(f"Day {day}: {steps} steps - {status}")

    minimum = 5000

    total = 0
    valid_days = 0
for steps in daily_steps:
    if steps < minimum:
        continue
        print(f"skipping {steps}, (below minimum)")
        
    total += steps
    valid_days += 1
    Average = total// valid_days

    print(f"\nValid_days : {valid_days}")
    print(f"Total steps (valid_days) : {total}")
    print(f"Average :{total// valid_days}")

# using while for consecutive days hitting target before the miss
daily_steps = [8200, 5100, 11300, 6800, 9400, 4200, 10100]

consecutive = 0
valid_days =0
target = 5000


while valid_days < len(daily_steps) and daily_steps [valid_days] >= target:
 consecutive += 1
 valid_days += 1


print(f"Consecutive days hitting the target from the start: {consecutive}")

total_valid_days = 6
average_steps = 8483
consecutive_streak = 5

print(f"{total_valid_days}, {average_steps}, and {consecutive_streak}")