#store fasting and cold shower variables
fasting = "Autophagy Marathon"
cold_shower = False

# Write your if/elif/else logic below
if fasting:
    print("Autophagy Marathon in progress")
else:
    print("Autophagy not started.")
if cold_shower:
    print("protocol observed")
else:
    print("cold shower skipped")
if fasting == "Autophagy Marathon" and "cold_shower == True":
    print("Peak discipline day.")
else:
    print("protocol not observed, more discipline is required")
