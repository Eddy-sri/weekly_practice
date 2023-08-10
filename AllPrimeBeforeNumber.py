n = int(input("pleas enter your number: "))


def prime(number: int) -> list:
    prime_list = []

    for each_number in range(2, number+1):
        sum = 0
        for each in range(2, each_number):
            if each_number % each == 0:
                sum += 1
        if sum == 0:
            prime_list.append(each_number)
            sum = 0
        else:
            sum = 0
    return prime_list


print(f"all prime number before {n} is {prime(n)}")
