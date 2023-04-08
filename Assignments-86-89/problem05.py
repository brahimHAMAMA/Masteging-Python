"""sumary_line

Keyword arguments:
argument -- description
Return: return_description
"""

myFriends = ["Ahmed", "Osama", "Sayed"]

def say_hello(some_peoples) -> list:
    """sumary_line
    
    Keyword arguments:
    argument -- description
    Return: return_description
    """
    for someone in some_peoples:
        print(f"Hello {someone}")

say_hello(myFriends)
