
# Input
def show_skills(name, *skills):
        
        if  skills != ():
                print(f"Hello {name} Your Skills Is : ")
        else:
                print(f"Hello {name} You Have No Skills To Show")
        for skill in skills:
                print(f"- {skill}")

show_skills("Osama", "HTML", "CSS", "JS", "Python")
show_skills("Ahmed")
# Output
"Hello Osama Your Skills Is"
"- HTML"
"- CSS"
"- JS"
"- Python"