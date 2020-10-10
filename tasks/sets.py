from random import randint
# A: Кількість різних чисел
a = [randint(1, 1000000) for i in range(1000000)]
print(len(a))
s = set(a)
print(len(s))