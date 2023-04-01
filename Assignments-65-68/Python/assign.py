import os
for i in range(1, 51):
    if i != 25:
        file = open(fr"{os.path.dirname(__file__)}\text{i}.txt", "w")
        file.write(f"Elzero Web School => {i}\n")
    else:
        file = open(fr"{os.path.dirname(__file__)}\special-text.txt", "w")


print(os.getcwd())
print(os.path.dirname(__file__))
print(os.path.basename(os.getcwd()))
print(os.path.basename(__file__))
print(len(os.listdir(os.getcwd())))

file.close()
file1 = open(fr"{os.path.dirname(__file__)}\text1.txt", "a+")

for i in range(1, 51):
    file1.writelines(f"Appended {i} => Elzero Web School\n")


# count number the lines
file1.seek(0)
file1Lines = file1.readlines()
print(f"Number Of Lines Is => {len(file1Lines)}\n")


# count number the Words
file1.seek(0)
content = file1.read()
print(f"Number Of Words Is => {len(content.split())}\n")

# count Number Of Chars
print(f"Number Of Chars Is => {len(content)}\n")
# count Number Of Chars
print(f"Number Of Chars Is => {content.count('l')}\n")
file1.close()

