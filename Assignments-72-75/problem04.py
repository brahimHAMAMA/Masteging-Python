skills = ("HTML", "CSS", 10, "PHP", "Python", 20, "JavaScript")

for index, skill in enumerate(reversed( skills), 50):
        if (isinstance(skill, str)) :print(f"{index} - {skill}")


print("="*20)
def checkSkills(skill):
        return isinstance(skill, str)

filterSkills = filter(checkSkills, skills)

for index, skill in enumerate(reversed(list(filterSkills)), 50):
        print(f"{index} - {skill}")

# Output
"50 - JavaScript"
"52 - Python"
"53 - PHP"
"55 - CSS"
"56 - HTML"