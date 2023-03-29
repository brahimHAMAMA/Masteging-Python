# Input
def say_hello(name='Unknown', age='Unknown', country='Unknown'):
    return f"Hello {name} Your Age Is {age} And You Live In {country}"
print(say_hello("Osama", 38, "Egypt"))
print(say_hello())
# Output
"Hello Osama Your Age Is 38 And You Live In Egypt"