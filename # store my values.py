# store my values
exercises = 6
sets = 4
reps = 10
average_weight_kg = 60 
duration_minutes = 45 
steps = 10000

total_sets = exercises * sets
total_reps = total_sets * reps
total_volume = average_weight_kg * total_reps
reps_per_minute = total_reps // duration_minutes
steps >= 10,000
print("=== WORKOUT SESSION ===")
print(f"sets : {total_sets}")
print(f"reps : {total_reps}")
print(f"weight : {total_volume}")
print(f"duration : {reps_per_minute}")
print(f"True : {steps > 10,000}")
