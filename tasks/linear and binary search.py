from random import randint

a = []
b = 0
while b < 10:
    z = randint(1, 50)
    a.append(z)
    b += 1
print(a)


def linear_unsorted_search(needed_number):
    for item in a:
        if item == needed_number:
            return a.index(item)
    return False


def lin_uns_search_max_min():
    max = a[0]
    min = a[0]
    for item in a:
        if max < item:
            max = item
        if min > item:
            min = item
    return f"Max = {max}, Min = {min}"


def linear_sorted_search(needed_number):
    for item in a:
        if item == needed_number:
            return a.index(item)
        elif item > needed_number:
            return False
    return False


print(lin_uns_search_max_min())


def binary_sorted_search(value):
    a = []

    for i in range(10):
        a.append(randint(1,20))
    a.sort()
    print(a)
    mid = len(a) // 2
    low = 0
    high = len(a) - 1

    while a[mid] != value and low <= high:
        if value > a[mid]:
            low = mid + 1
        else:
            high = mid - 1
        mid = (high + low) // 2

    if low > high:
        return "No value"
    else:
        return f"The value`s index - {mid}"


print(binary_sorted_search(7))



