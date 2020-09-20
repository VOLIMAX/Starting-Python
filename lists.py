from random import randint
from collections import Counter
# A - парні індекси
a = [1, 2, 3, 4, 5]
print(f"{a[2::2]} \n===========================================================")

# B - парні числа
a = [1, 2, 2, 3, 3, 3, 4]
for i in a:
    if i % 2 == 0:
        print(i, end=" ")
print("\n===========================================================")

# C - більше попереднього
a = [1, 5, 2, 4, 3]
q = 100  # щоб не вивело одиничку
for i in a:
    if i > q:
        print(i, end=" ")
    q = i
print("\n===========================================================")

# D - перший додатний
a = [-1, 0, 1]
print(a.index(1))
print("\n===========================================================")

# E - перший позитивний - 2
a = [-1, 0, 1]
first_pos = 1
if first_pos in a:
    print(first_pos)
else:
    print(-1)
print("\n===========================================================")

# F - найбільший елемент
a = [1, 2, 3, 2, 1]
biggest = max(a)
print(f"Index of the biggest number = {a.index(biggest)}")
print(f"The biggest num in the list = {biggest}")
print("\n===========================================================")

# G - більше своїх сусідів
a = [1, 2, 3, 2, 1]
z = 0
for i in range(1, len(a) - 1):
    if a[i - 1] < a[i] > a[i + 1]:
        z += 1
print(f"There are {z} numbers which are bigger than their neighbours")
print("\n===========================================================")

# H - найменший додатний
a = []
for i in range(10):
    a.append(randint(-1000, 1000))
print(a)
min_positive = 1000
for i in a:
    if i > 0:
        if min_positive > i:
            min_positive = i
print(f"The smallest positive number is {min_positive}")
print("\n===========================================================")

# I - найближче число
a = [10, 15, 25, 30, 150, 250]
target = 28
print(f"Найблжче число - {min(enumerate(a), key=lambda x: (abs(x[1] - target), x[0]))[1]}")
print("\n===========================================================")

# J - шеренга
a = [165, 163, 162, 161, 157, 157, 155, 154]
target = 160
a.append(target)
a.sort()
print(f"Номер Андрія в шерензі - {a.index(target)}")
print("\n===========================================================")

# K - кількість різних елементів
a = [1, 5, 7, 2, 5, 7, 4, 10]
unique = []
counter = 0
for i in a:
    if i not in unique:
        unique.append(i)
        counter += 1
print(f"Кількість номерів, які не повторюються - {len(unique)}")
print("\n===========================================================")

# L - найменший непарний
a = [i for i in range(10)]
b = []
z = 0
for i in range(len(a)):
    if i % 2 != 0:
        b.append(i)
print(f"Список непарних елементів {b}")
if len(b) > 0:
    z = min(b)
    print(f"Найменший непарний - {z}")
else:
    print(f"0")
print("\n===========================================================")

# M - переставити в зворотньому напрямку
print(' '.join(input("Введіть числа для списку: ").split()[::-1]))  # на початку ми з'єднуємо пробелом, щоб при виводі
# числа не злиплись, ми вводимо числа, розділяємо і переставляємо в звортньому напрямку
print("\n===========================================================")

# N - переставити сусідні
a = [i for i in range(10)]
for i in range(1, len(a), 2):
    a[i - 1], a[i] = a[i], a[i - 1]
print(' '.join([str(i) for i in a]))
print("\n===========================================================")                 #!!!!!!!!!!!!!!!!!!!!!!!

# O - переставити мін і мах
a = [i for i in range(10)]
q = min(a)
x = max(a)
for i in range(1, len(a)):
    a[q], a[x] = a[x], a[q]
print(f"Перестановка min і max: {' '.join([str(i) for i in a])}")
print("\n===========================================================")                 #!!!!!!!!!!!!!!!!!!!!!!!

# R - кількість співпадаючих пар
array = [randint(1, 9) for i in range(5)]
print(array)
c = Counter(array)
print(c)
# array_d = dict.fromkeys(array, 0)
# for a in array:
#     array_d[a] += 1
# print(array_d)
print("\n===========================================================")                #!!!!!!!!!!!!!!!!!!!!!!!

# T - кількість різних елементів - 2
                                                                                    #зробити
# V - унікальні елементи
array = [randint(1, 9) for i in range(5)]
print(array)
print(f"Unique {list(set(array))}")                #треба вивести в тому вигляді в якому вони зустрічаються