def convert(num):
    num = str(num)

    myList = list( map(str, str(num)))
    
    myList.reverse()
    print(type(myList[0]))
    number = int("".join(myList))
    print(type(number))

    return number

print(convert(123456))

print("="*20)
def convert1(num):
    list = []
    for n in str(num):
        list.insert(0, n)
    return int("".join(list))

print(convert1(456789))

print("="*20)
def convert2(n):
    list = [num for num in str(n)[::-1]]
    return int("".join(list))

print(convert2(123456))