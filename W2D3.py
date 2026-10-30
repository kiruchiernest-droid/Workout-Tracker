# store variables
exercises = 6
steps_exercise = 4
reps_per_set = 10
average_weight_per_rep = 60
duration = 45
target = 10000 

# calculations
total_sets = exercises * steps_exercise
total_reps = total_sets * reps_per_set
total_volume = average_weight_per_rep * total_reps
reps_minute = total_reps//duration
exceeded_10000_kg = total_volume - target 

#results
print(f"Total sets:{total_sets}")
print(f"Total reps:{total_reps}")
print(f"Total volume:{total_volume}")
print(f"Reps Per minute:{reps_minute}")
print(f"Outcome in kg: {exceeded_10000_kg}")
      