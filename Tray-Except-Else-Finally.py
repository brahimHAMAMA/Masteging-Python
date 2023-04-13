# try:
#     number = int(input("Enter your Age "))
#     print("Good, This value is Integer From Try")

# except:
#     print("Bad, This value is Not Integer")
# else:
#     print("Good, This value in Integer Form Else")
# finally:
#     print("Print From Finally Whatever Happens")


# Ex 02

try:
    # print(10/0)
    # print(x)
    print(int("Brahim"))
except ZeroDivisionError:
    print("Can't Divide by 0")
except NameError:
    print("Name value not existed")
except ValueError:
    print("Value Error From my Code")

except:
    print("Error Happens")