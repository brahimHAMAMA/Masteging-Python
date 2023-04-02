age = 40
print("Suitable") if age > 20 else print("Not Suitable")

t = 90
x= {True: 'Water is boiling', False: 'Water is not boiling'}[t >= 100]

print(type(x))
print(x)

t = 90
x= ('Water is not boiling', 'Water is boiling')[t >= 100]
print(type(x))
print(x)


t = 90
x= (lambda: 'Water is not boiling', lambda: 'Water is boiling')[t >= 100]()
print(type(x))
print(x)

t = 90
print(('Water is not boiling', 'Water is boiling')[t >= 100])