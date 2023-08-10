# approach 1
from collections import Counter

my_list = [2, 2, 3, 6, 5, 6, 8, 5, 7, 8, 9, 9, 9,
           9, 4, 'a', 'a', 'a', 'b', 'c', 'd', 'd', 4, 5, 5, 5, 1]

most_repit = Counter(my_list).most_common(1)[0][0]

print(most_repit)


# approach 2

my_dict = {}

for item in my_list:
    my_dict[item] = my_dict.get(item, 0) + 1
# print(my_dict)

sum = 0
for key, val in my_dict.items():
    if val > sum:
        sum = val
        most = key
print(most)
