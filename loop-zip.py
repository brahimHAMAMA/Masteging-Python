list1 = [1,2,3,4,5]
list2 = ["A","B","C"]
tuple1 = ("Brahim","Amina", "Khalil", "ali")
dict1 = {"name":"Brahim", "age":40, "country":"alg"}

ultimateList = zip(list1, list2)

print(ultimateList)

# for item in ultimateList:
#     print(item)


for item1, item2, item3, item4 in zip(list1, list2, tuple1, dict1):
    print("Item in List 1  =>", item1)
    print("Item in List 2  =>", item2)
    print("Item in Tuble 1 =>", item3)
    print("Item in Dict 1  =>", item4, "Value => ", dict1[item4])