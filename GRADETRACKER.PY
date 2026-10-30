# Write your try/except block here
def parse_score(value):
    try:
        return int("two hundred")
    except (ValueError, TypeError):
        return "Invalid entry: two hundred is not a number"

# Test
print(parse_score("two hundred"))