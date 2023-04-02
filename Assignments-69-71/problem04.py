# my_all
def my_all(*mydata):
        result = True
        for data in mydata:
                if data == False or data == 0 or data == [] or data == [] or data == "":
                        result = False
                        break
        return result
print(my_all(*[1, 2, 3])) # True
print(my_all(*[1, 2, 3, []])) # False

# my_any
def my_any(*mydataAny):
        result = False
        for data in mydataAny:
                if ((data != False) or (data != 0) or (data != []) or (data != ()) or (data != "")):
                        result = True
                        # break
                        # print(f" test : {(data != False) or (data != 0) or (data != []) or (data != ()) or (data != "")}")
        return result
print(my_any([0, 1, [], False])) # True
print(my_any([(), 0, False])) # False

# # my_min
def my_min(*nums):
        min = 0
        for num in nums:
                if min> num:
                        min = num
        return min
print(my_min(*[10, -100, -20, -150, 50])) # -150
print(my_min(*(10, 100, -20, -100, 50))) # -100

# # my_max
def my_max(*nums):
        max = 0
        for num in nums:
                if max< num:
                        max = num
        return max
print(my_max(*[10, 100, -20, -100, 50, 700])) # 700
print(my_max(*(10, 100, -20, -100, 50, 750))) # 750


print(sum([1,2,3,5],0))

a, b = 20, 30 
print(f"a = {a}", f"b= {b}", sep=" | ")
print("First Line", end=" ")
print("First Second")
print(pow(3,2,4))
