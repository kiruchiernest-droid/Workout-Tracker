import math
steps = 10500
target = 10000
Sleep_hours = 6
Water_glasses = 5
Cold_shower = True
Pages_read = 15
# steps evaluation
if steps >= 10000:
    print("Excellent")

elif steps >= 7500:
    print("good")
else:
    print("good, but do more")
# sleep and water evaluation
if Sleep_hours >= 6 and Water_glasses >= 5:
    print("good, target achieved.")
else:
    print("low, target missed.")
#cold shower and reading evaluation
if Cold_shower and Pages_read >= 10:
    print("Good, target achieved.")
else:
    print("Poorly done, own your morning.")
    










