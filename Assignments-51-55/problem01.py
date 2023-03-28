# Input
my_nums = [15, 81, 5, 17, 20, 21, 13]
result=[]
for num in my_nums:
    if num % 5 == 0:
        result.append(num)
result.sort(reverse=True)

for i in range(0, len(result)):

    print(f"{i + 1} => {result[i]}")
else:
    print("All Numbers Printed")
# Needed Output
"1 => 20"
"2 => 15"
"3 => 5"
"All Numbers Printed"