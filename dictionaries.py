# K: Номер появи слова
counter = {}
text = "She sells sea shells on the sea shore; The shells that she sells are sea shells I`m sure. So if she sells sea shells on the sea shore, I`m sure that the shells are sea shore shells."
for word in text.split():
    counter[word] = counter.get(word, 0) + 1
    print(counter[word] - 1, end=' ')                       # dictionary.get(keyname, value)
print(f"\n=====================================")

# L: Словник синонімів
# my_file = open("slovnyk.txt","r")
# my_words = []
# for line in my_file:
#     my_words.extend(line.replace(",","").replace(".","").replace("!","").replace("\n","").split())
# print(my_words)
n = 3
d = {}
for i in range(n):
    first, second = input().split()
    d[first] = second
    d[second] = first
print(d[input()])
print(f"\n=====================================")

# M: Вибори в США
num_votes = {}
for q in range(int(input())):
    candidate, votes = input().split()
    num_votes[candidate] = num_votes.get(candidate, 0) + int(votes)      #!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!

for candidate, votes in sorted(num_votes.items()):
    print(candidate, votes)

# N: Найчастіше слово
counter1 = {}
for i in range(int(input())):
    line = input().split()
    for word in line:
        counter1[word] = counter1.get(word, 0) + 1

max_count = max(counter1.values())                                  # values() method returns a view object that displays a list of all values in a given dictionary.
most_frequent = [k for k, v in counter1.items() if v == max_count]  # items() показує всі елементи словника
print(min(most_frequent))

#O: Права доступу
ACTION_PERMISSION = {
    'read': 'R',
    'write': 'W',
    'execute': 'X',
}

file_permissions = {}
for i in range(int(input())):
    file, *permissions = input().split()
    file_permissions[file] = set(permissions)

for i in range(int(input())):
    action, file = input().split()
    if ACTION_PERMISSION[action] in file_permissions[file]:
        print('OK')
    else:
        print('Access denied')                                  #!Допустим A, *B = (123, 12345, 12345, 12345) тогда A = 123, B = [12345, 12345, 12345] где A приняла первое значение, B - все остальные.

