# Input
my_ranks = {
  'Math': 'A',
  "Science": 'B',
  'Drawing': 'A',
  'Sports': 'C'
}
total = 0
for key, value in my_ranks.items():
    if(value =="A"):
            print(f"My Rank in {key} Is {value} And This Equal 100 points.")
            total = total + 100
    elif(value == "B"):
            print(f"My Rank in {key} Is {value} And This Equal 80 points.") 
            total = total + 80
    else :
            print(f"My Rank in {key} Is {value} And This Equal 40 points.") 
            total = total + 40
else:
    print(f"Total Points Is {total}")
# Needed Output
"My Rank in Math Is A And This Equal 100 Points"
"My Rank in Science Is B And This Equal 80 Points"
"My Rank in Drawing Is A And This Equal 100 Points"
"My Rank in Sports Is C And This Equal 40 Points"
"Total Points Is 320"