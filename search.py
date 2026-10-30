#store my contacts
contacts = [ {"name": "James Omondi", "phone": "0712345678", "skill": "Welding", "city": "Nairobi"},
    {"name": "Sandra Weru",   "phone": "0723456789", "skill": "tiling",       "city": "Mombasa"},
    {"name": "Patrick Njiru", "phone": "0734567890", "skill": "phone repair", "city": "Nairobi"},
    {"name": "Grace Achieng", "phone": "0745678901", "skill": "copywriting",  "city": "Kisumu"},
    {"name": "Brian Kamau",   "phone": "0756789012", "skill": "upholstery",   "city": "Nairobi"},
]

print("\n=====PHONE CONTACTS=====")
search_name = "James Omondi"
found = False
for contact in contacts:
    if contact ["name"] == search_name:

      print("Contact found:")
      print(f" Name : {contact['name']}")
      print(f" Phone : {contact['phone']}")
      print(f" Skill : {contact['skill']}")
      print(f" City : {contact['city']}")
      found = True
      break
    if not found:
       print("No contact found with name:", search_name)
