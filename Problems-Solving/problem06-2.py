def add_commas_and_underscore(num):
    num = f"{num:,}"
    return f"{num[:-4]}_{num[-3:]}" if num[-4:-3]=="," else num
    

print(add_commas_and_underscore(120)) # 120
print(add_commas_and_underscore(1530)) # 1_530
print(add_commas_and_underscore(120510650)) # 120,510_650
print(add_commas_and_underscore(510650480910)) # 510,650,780_910
print(add_commas_and_underscore(12069057014032)) # 12,069,057,014_032
