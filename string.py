myString = "I Live Python"


c = "Brahim"

print(c.rjust(10,"#"))

d = """ I Love Python
and PHP
And JAVA """
print(d.splitlines()) 


name = "brahim"
age = 4000
rank = 1200
print("My Name Is %d " %  age)

print("My Name Is %s and d mY age %d and rank is %.2f" % (name, age, rank))

# New Way

print("My Name Is {} ".format(age))

print("My Name Is {:.2s} and d mY age {:d} and rank is {:.2f}" .format(name, age , rank))


myMony = 12000122012000.232222

print("My Mony {:,.2f}".format(myMony))