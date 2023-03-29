
def get_score(**moduls):
    for key, value in moduls.items():
        print(f"{key} => {value}")
 
# Tests
get_score(Math=90, Science=80, Language=70)
print("="*20)
get_score(Logic=70, Problems=60)
# Output
"Math => 90"
"Science => 80"
"Language => 70"