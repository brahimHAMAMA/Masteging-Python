# [A-z0-9\._-]+[A-z0-9]+@[A-z\-_]+[A-z]+\.(com|net|org|co)
import re

# my_search = re.search(r"[A-Z]{2}", "DDsamaEElzero")

# print(my_search)
# print(my_search.span)
# print(my_search.string)
# print(my_search.group())
# print(type(my_search))

# email = "brahum@W@bb.com"

# is_email = re.search(r"[A-z0-9\._-]+[A-z0-9]+@[A-z\-_]+[A-z]+\.(com|net|org|co)",email)

# print(bool(is_email))
# if is_email :
#     print("This is a valid Email")
# else:
#     print("This is not a valid Email")


# email = "brahum@Wbb.com"

# search = re.findall(r"[A-z0-9\._-]+[A-z0-9]+@[A-z\-_]+[A-z]+\.com|net|org|co" ,email)


# print(search)
# print(dir(search))
# print(type(search))


string_one ="I Love Python Programming Language"

search_one = re.split(r"\s", string_one,2)

print(search_one)
print(type(search_one))