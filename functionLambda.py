sayHello = lambda name, age : f"Hello {name} your age {age}"

print(sayHello("brahim", 34))

sayHello1 = lambda name : print(f"Hello {name}")

sayHello1("ali")
print(type(sayHello1))
print(sayHello.__name__)