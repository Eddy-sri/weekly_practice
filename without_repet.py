list1 = [1, 2, 5, "apple", "banana"]
list2 = [1, 7, 9, 5, "apple", "pinapple"]


def removeـRepetitious(iter1, iter2):
    for elm in list(iter1):
        if elm in iter2:
            iter2.remove(elm)
        else:
            iter2.append(elm)
    return iter2


print(removeـRepetitious(list1, list2))
