from random import randint


# A: Кількість різних чисел
def dif_num():
    a = [randint(1, 100000) for i in range(randint(1, 100000))]
    print(f"К-сть різних чисел: {len(set(a))}")
# dif_num()


# B: Кількість співпадаючих
def num_of_same():
    a = [randint(1, 100000) for i in range(randint(1, 100000))]
    b = [randint(1, 100000) for i in range(randint(1, 100000))]
    print(f"К-сть співпадаючих: {len(set(a).intersection(set(b)))}")
# num_of_same()


# С: Перетин списків
def inters():
    a = [randint(1, 100000) for i in range(randint(2, 100000))]
    b = [randint(1, 100000) for i in range(randint(1, 100000))]
    print(f"К-сть співпадаючих: {sorted(set(a).intersection(set(b)))}")
# inters()


# D: Чи зустрічалось число раніше
def met_before():
    a = [1, 2, 3, 2, 3, 4]
    b = set()
    for i in a:
        if i not in b:
            print("No")
        else:
            print("Yes")
        b.add(i)
# met_before()


# E: Кубики
def cubes():
    file = open("cubes.txt", "r")
    q, t = file.readline().split()
    iryna = set()
    igor = set()
    for line in range(int(q)):
        line = file.readline().replace("\n", "")
        iryna.add(line)

    for line in range(int(t)):
        line = file.readline().replace("\n", "")
        igor.add(line)

    print(f"Iryna - {iryna}")
    print(f"Igor - {igor}")
    neutral = sorted(iryna.intersection(igor))
    print(f"Є і в Ірини, і в Ігоря - {neutral}")

    rest_of_iryna = iryna.difference(neutral)
    rest_of_igor = igor.difference(neutral)

    print(f"К-сть тих, що залишились в Ірини - {len(rest_of_iryna)}")
    print(f"Ті, що залишились в Ірини у відсортованому порядку: {sorted(rest_of_iryna)}")
    print(f"К-сть тих, що залишились в Ігоря - {len(rest_of_igor)}")
    print(f"Ті, що залишились в Ігоря у відсортованому порядку: {sorted(rest_of_igor)}")
# cubes()


# F: Кількість слів в тексті
def amount_of_words_in_text():
    text = "She sells sea shells on the sea shore; The shells that she sells are sea shells I`m sure. So if she sells" \
           " sea shells on the sea shore, I`m sure that the shells are sea shore shells."
    a = set()

    for word in text.split():
        a.add(word)

    print(f"К-сть різних слів в тексті - {len(a)}")
# amount_of_words_in_text()


# G: Вгадай число
def guess_the_num():
    file = open("guess_the_num.txt", "r")
    commands = ["YES", "NO", "HELP"]
    n = file.readline().replace("\n", "")
    a = set(file.readline().split())
    answer = file.readline().replace("\n", "")

    if answer == commands[0]:
        print("One of this is a searched number")
    else:
        print("None of this is a searched number")

    b = set(file.readline().split())
    next_answer = file.readline().replace("\n", "")

    if next_answer == commands[0]:
        print("One of these is a searched number")
    else:
        print("None of these is a searched number")

    asking = file.readline().replace("\n", "")

    if asking == commands[2]:
        print(f"The answer is one of these: {sorted(a.difference(b))}")
#guess_the_num()


# H: Вгадай число - 2