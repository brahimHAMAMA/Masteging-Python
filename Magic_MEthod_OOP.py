class Skill:
    def __init__(self) -> None:
        self.skills = ["html", "css", "js"]
    def __str__(self) -> str:
        return f"This is My Skills {self.skills}"



profile = Skill()

print(profile)
# print(len(profile))
print(dir(profile))