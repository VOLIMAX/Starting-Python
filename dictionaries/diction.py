from collections import Counter, defaultdict
# K: Номер появи слова
def n_p_s():
    counter = {}
    text = "She sells sea shells on the sea shore; The shells that she sells are sea shells I`m sure. So if she sells" \
           " sea shells on the sea shore, I`m sure that the shells are sea shore shells."
    for word in text.split():
        counter[word] = counter.get(word, 0) + 1
        print(counter[word] - 1, end=' ')


# n_p_s()

# L: Словник синонімів
def s_s():
    my_file = open("slovn_synon.txt", "r")
    synonym = {}
    last_line = ""
    t = my_file.readline()
    print(f"Number of strings with synonyms: {t}")

    for line in range(int(t)):
        line = my_file.readline()
        key, value = line.split()
        synonym[key] = str(synonym.get(key, "")) + value

    for line in my_file:
        last_line = line

    print(f"We search synonym for the word in the last string: {last_line}")

    for key, value in synonym.items():
        if last_line == value:
            print(f"Searched synonym - {key}")
        if last_line == key:
            print(f"Searched synonym - {value}")
# s_s()

# M: Вибори в США
def elections():
    my_file = open("elections.txt", "r")
    elect = {}

    for line in my_file:
        candidate, votes = line.split()
        elect[candidate] = elect.get(candidate, 0) + int(votes)

    for candidate, votes in sorted(elect.items()):
        print(candidate, votes)

# elections()


# N: Найчастіше слово
def most_often():
    counter = {}
    text = "apple orange banana banana orange"
    line = text.split()
    for word in line:
        counter[word] = counter.get(word, 0) + 1
    max_count = max(counter.values())
    most_frequent = [k for k, v in counter.items() if v == max_count]
    return min(most_frequent)


# print(most_often())

# O: Права доступу
def permission():
    action_permission = {
        'read': 'R',
        'write': 'W',
        'execute': 'X',
    }
    file_permissions = {}
    my_file = open("permis.txt", "r")
    t = my_file.readline()
    print(f"Number of strings to read: {t}")

    for line in range(int(t)):
        line = my_file.readline()
        file, *permissions = line.split()
        file_permissions[file] = set(permissions)

    q = my_file.readline()
    print(f"Number of strings to read: {q}")

    for line in range(int(q)):
        line = my_file.readline()
        action, file = line.split()
        if action_permission[action] in file_permissions[file]:
            print("OK")
        else:
            print("Access denied")


# permission()

# Q: Країни та міста
def country_city():
    my_file = open("coutry_city.txt", "r")
    place = {}
    t = my_file.readline()
    print(f"Number of strings to read: {t}")

    for line in range(int(t)):
        line = my_file.readline()
        country, *cities = line.split()
        for city in cities:
            place[city] = country

    q = my_file.readline()
    print(f"Number of strings to read: {q}")

    for line in range(int(q)):
        line = my_file.readline()
        qq, *qqq = line.split()
        print(place[qq])


# country_city()

# P: Частотний аналіз
def analysis():
    my_file = open("analysis.txt", "r")
    words = {}
    t = my_file.readline()
    print(f"Number of strings to read: {t}")

    for line in range(int(t)):
        line = my_file.readline()
        for i in line.split():
            words[i] = words.get(i, 0) + 1

    for i in sorted(words.items(), key=lambda x: (-x[1], x[0])):
        print(i[0])


#analysis()
# set - забирає повтори і ставить по порядку

# S: Контрольна по наголосам
def nagolos():
    file = open("nagolos.txt", "r")
    accents = {}
    q = file.readline()
    print(f"Number of strings to read: {q}")

    for i in range(int(q)):
        i = file.readline().replace("\n", "")
        base_form = i.lower()
        if base_form not in accents:
            accents[base_form] = set()
        accents[base_form].add(i)

    mistakes = 0
    homework = file.readline().split()
    print(f"{accents}\n")

    for word in homework:
        base_form = word.lower()
        if base_form in accents and word not in accents[base_form] or len([i for i in word if i.isupper()]) != 1:
            print(f"Mistake - {word}")
            mistakes += 1

    print(mistakes)


#nagolos()


# T: Продажі
def sales():
    # collections.Counter - вид словаря, который позволяет нам считать количество неизменяемых объектов
    # (в большинстве случаев, строк)
    # collections.defaultdict ничем не отличается от обычного словаря за исключением того, что по умолчанию всегда
    # вызывается функция, возвращающая значение:

    file = open("sales.txt", "r")
    def_dict = defaultdict(Counter)

    for line in file:
        customer, product, count = line.split()
        def_dict[customer][product] += int(count)

    for customer, sale in sorted(def_dict.items(), key=lambda x: x[0]):
        print(customer, ':', sep='')
        for product, count in sorted(sale.items(), key=lambda x: x[0]):
            print(' {} {}'.format(product, count))


#sales()
