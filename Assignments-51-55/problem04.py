# Input
students = {
  "Ahmed": {
    "Math": "A",
    "Science": "D",
    "Draw": "B",
    "Sports": "C",
    "Thinking": "A"
  },
  "Sayed": {
    "Math": "B",
    "Science": "B",
    "Draw": "B",
    "Sports": "D",
    "Thinking": "A"
  },
  "Mahmoud": {
    "Math": "D",
    "Science": "A",
    "Draw": "A",
    "Sports": "B",
    "Thinking": "B"
  }
}
total =0
for key1, value in students.items():
    print("------------------------------")
    print(f"-- Student Name => {key1}")
    print("------------------------------")
    for key, value in value.items():
        if(value =="A"):
            print(f"- {key} => 100 Points")
            total = total + 100
        elif(value == "B"):
            print(f"- {key} => 80 Points")
            total = total + 80
        elif(value =="C") :
            print(f"- {key} => 40 Points")
            total = total + 40
        else :
            print(f"- {key} => 20 Points")
            total = total + 20
    
    print(f"Total Points For {key1} Is {total}")
# Needed Output
"------------------------------"
"-- Student Name => Ahmed"
"------------------------------"
"- Math => 100 Points"
"- Science => 20 Points"
"- Draw => 80 Points"
"- Sports => 40 Points"
"- Thinking => 100 Points"
"Total Points For Ahmed Is 340"
"------------------------------"
"-- Student Name => Sayed"
"------------------------------"
"- Math => 80 Points"
"- Science => 80 Points"
"- Draw => 80 Points"
"- Sports => 20 Points"
"- Thinking => 100 Points"
"Total Points For Sayed Is 360"
"------------------------------"
"-- Student Name => Mahmoud"
"------------------------------"
"- Math => 20 Points"
"- Science => 100 Points"
"- Draw => 100 Points"
"- Sports => 80 Points"
"- Thinking => 80 Points"
"Total Points For Mahmoud Is 380"