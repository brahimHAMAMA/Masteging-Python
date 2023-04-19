class Member:

    not_allowed_names = ["Hell","Shit","Balot"]
    user_num = 0

    @classmethod
    def show_user_count(cls):
        print(f"We Have {Member.user_num} - {cls.user_num} - Users In Our System.")

    @staticmethod
    def say_how_are_you():
        print("Hello from Static Method")

    def __init__(s, fname, lname,gender) -> str:
        s.fname = fname
        s.lname = lname
        s.gender = gender
        Member.user_num += 1

    def say_hello(s):
        return f"Hello Mr {s.fname}" if s.gender == "male" else f"Hello Mess {s.fname}" 

    def get_full_name(s):
        if s.fname in Member.not_allowed_names:
            raise "This Name Is not Allowed"
        else:      
            return f"{s.fname} {s.lname}"

    def get_info(s):
        return f"{s.say_hello()}, Full Name Is : {s.get_full_name()} "

print(Member.user_num)
member1 = Member("Brahim","hamama","male")
member2 = Member("ali", "Hamama","male")
member3 = Member("amina","hamama","female")
print(Member.user_num)

Member.show_user_count()
Member.say_how_are_you()
# print(member1.fname)
# print(member1.lname)

# print(member2.fname)
# print(member3.fname)


# print(member3.say_hello())
# print(member3.get_full_name())
# print(member3.get_info())
