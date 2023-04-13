the_file = None
the_tries = 5

while the_tries>0:
    try:
        print("Enter The File Name With Absolote Path To Open")
        print(f"You have {the_tries} Tries Left")
        print("Ex: D:\Python\Files\ file_name.py")
        file_name_path = input("File Name => : ").strip()
        the_file = open(file_name_path,"r")
        print(the_file.read())
        break
    except FileNotFoundError:
        print("The File Not Found Please Try")
        the_tries -=1
    except:
        print("Error Happen")
    finally:
        if the_file is not None:
            the_file.close()
            print("The file Is Closed")
    # print(f"{the_tries} Tries Left")
    # the_tries -=1

else:
    print("All Trie Is Done ")
