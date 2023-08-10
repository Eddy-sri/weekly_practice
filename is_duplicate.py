my_list = [4, 5, 6, 'f', 2, 1, 4, 'a', 'a', 'f', 7, 8,
           9, 5, 6, 8, 2, 2, 1, 1, 1, 3, 3, 'b', 'c', 'c', 'c']
my_dict = {}

for item in my_list:
    if item in my_dict:
        my_dict[item] += 1
    else:
        my_dict[item] = 1
# print(my_dict)

duplicate_list = []
for key, val in my_dict.items():
    if val == 2:
        duplicate_list.append(key)
print(f"duplicate item in my list is :{duplicate_list}")
