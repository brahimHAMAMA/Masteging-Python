# Inputs

email = input("Inter Your Email : ").strip().lower()
name = email[:email.index("@")].capitalize()

Domain = email[email.index("@") +1 : email.index(".")]
Top_Level_Domain = email[email.index(".") + 1:]

print(f"Your Name Is {name}")
print(f"Email Service Provider Is {Domain}")
print(f"Top Level Domain Is {Top_Level_Domain}")

# "Osama@Nn.Sa" # Email

# Needed Output

# "Your Name Is Osama"
# "Email Service Provider Is nn"
# "Top Level Domain Is sa"