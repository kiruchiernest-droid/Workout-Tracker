def weekly_report(name, steps_list, goal=8000):
    days_on_target = 0
    for s in steps_list:
        if s >= goal:
            days_on_target += 1
        avg = sum(steps_list) / len(steps_list)
        print(f"--- {name}' s ---")
        print(f"Days tracked : { len(steps_list)}")
        print(f"Days on goal : {days_on_target}")
        print(f"Average steps: {round(avg, 0)}")
        print()

weekly_report("James", [9200, 7500, 10500, 8800, 6900, 11000, 9600])
weekly_report("Sandra", [10000, 10200, 9800, 11000, 10500], goal=10000)        
              