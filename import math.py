def parse_score(value):
    try:
        return int(value)
    except (ValueError, TypeError):
        return None

# Test
print(parse_score("85"))
print(parse_score(""))
print(parse_score("bad data"))
print(parse_score(None))