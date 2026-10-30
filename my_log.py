my_log = {
    "steps": 9400,
    "water_glasses": 7,
    "fasting_protocol": "OMAD",
    "cold_shower": True,
    "sleep_hours": 7.0
}

for key, value in my_log.items():
    print(key, ":", value)

    print()

if my_log["steps"] >= 8000:
    print("steps goal hit")
else:
    print("Off target, more effort needed")
    
