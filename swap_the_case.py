# approach 1
my_str = input("pleas enter your str ")

print(my_str.swapcase())

# approach 2
new_str = ""
for each_car in my_str:
    if each_car.isupper():
        new_str += each_car.lower()
    else:
        new_str += each_car.upper()
print(new_str)
