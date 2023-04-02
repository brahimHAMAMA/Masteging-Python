def remove_chars(name):
    return name[1:-1]

friends_map = ["AEmanS", "AAhmedS", "DSamehF", "LOsamaL"]

cleaned_list = map(remove_chars, friends_map)

for name in cleaned_list:
    print(name)

print("="*20)
remove_chars = lambda name: name[1:-1]


cleaned_list = map(remove_chars, friends_map)

for name in cleaned_list:
    print(name)




# Output
"Eman"
"Ahmed"
"Sameh"
"Osama"