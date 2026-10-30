def log_day(steps, water=8, protocol="OMAD"):
    print(f"Steps: {steps}, | Water: {water} | Protocol: {protocol}")

    # call
log_day(2500)
log_day(10500, water=9)
log_day(8000, water=4, protocol="2MAD")

def client_report(name, goal, sessions=4, bench_kg=60):
    print(f"Name : {name} | Goal : {goal} | Session : {sessions} | Bench Press : {bench_kg}kg")
# Positional argument
client_report("James", "fat loss")

# Keyword arguments: order does not matter
client_report(goal="muscle gain", name="Mwangi", bench_kg=100)

# Mix of positional and keyword
client_report("Sandra", "endurance", bench_kg=50)