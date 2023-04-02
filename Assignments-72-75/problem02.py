def get_names(name):
    return name[len(name) - 1] == "m"
friends_filter = ["Osama", "Wessam", "Amal", "Essam", "Gamal", "Othman"]

names = filter(get_names, friends_filter)

for name in names:
    print(name)

print("="*20)
get_names = lambda name : name[len(name) - 1] == "m"

names = filter(get_names, friends_filter)

for name in names:
    print(name)
# Output
"Wessam"
"Essam"