import os


# print(os.path.abspath(__file__))
# print(os.path.dirname(__file__))
# print(os.path.dirname(os.path.abspath(__file__)))
# print(__file__)
# print(fr"{os.path.dirname(__file__)}\bAli.txt")
# print(fr"{os.getcwd()}\bAli.txt")

file = open(fr"{os.getcwd()}\bAli.txt")
# print(file.name)
# print(file.mode)
# print(file.encoding)
# print(file.read(12))
# print(file.readline())
# print(file.readline(7))
# print(file.readlines())
contents = file.readlines()
print(contents)
for line in contents:
    print(line)
    if line.startswith("0"):
        break
file.close()