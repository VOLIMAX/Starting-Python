import csv
# K: Номер появи слова
def n_p_s():
    counter = {}
    text = "She sells sea shells on the sea shore; The shells that she sells are sea shells I`m sure. So if she sells sea shells on the sea shore, I`m sure that the shells are sea shore shells."
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


#country_city()