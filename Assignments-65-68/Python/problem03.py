import os

path1 = fr"{os.path.dirname(__file__)}"

for i in range(41, 51):
        if os.path.exists(fr"{path1}\text{i}.txt"):
                os.remove(fr"{path1}\text{i}.txt")
        else:
                print(f"The File text{i}.txt Not Exixteing...")
else:
        print("the files has deleted..")

if os.path.exists(fr"{path1}\text10.txt"):
        os.rename(fr"{path1}\text10.txt",fr"{path1}\newtext10.txt")
else:
        print(f"The File text10.txt Not Exixteing...")