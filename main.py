import math
from random import randint


#4.19
def rectangle(a_x, a_y, b_x, b_y, height_a, width_a, height_b, width_b):
    #a_x, a_y - координати лівого нижнього кутка першого прямокутника
    #b_x, b_y - координати лівого нижнього кутка другого прямокутника
    #c_x, c_y - координати лівого нижнього кутка великого прямокутника
    #d_x, d_y - координати лівого нижнього кутка великого прямокутника

    if height_b == height_a:
        if a_x < b_x and a_y < b_y:
            c_x = a_x
            c_y = a_y
            d_x = b_x + width_b
            d_y = b_y + height_b
        elif a_x < b_x and a_y > b_y:
            c_x = a_x
            c_y = b_y
            d_x = b_x + width_b
            d_y = a_y + height_a
        elif a_x > b_x and a_y < b_y:
            c_x = b_x
            c_y = a_y
            d_x = a_x + width_a
            d_y = b_y + height_b
        else:
            c_x = b_x
            c_y = b_y
            d_x = a_x + width_a
            d_y = a_y + height_a

    elif height_b > height_a:
        if a_x < b_x and a_y < b_y:
            c_x = a_x
            c_y = a_y
            d_x = b_x + width_b
            d_y = b_y + height_b
        elif a_x < b_x and a_y > b_y:
            c_x = a_x
            c_y = b_y
            d_x = b_x + width_b
            d_y = b_y + height_b
        elif a_x > b_x and a_y < b_y:
            c_x = b_x
            c_y = a_y
            d_x = a_x + width_a
            d_y = b_y + height_b
        else:
            c_x = b_x
            c_y = b_y
            d_x = a_x + width_a
            d_y = b_y + height_b

    else:
        if a_x < b_x and a_y < b_y:
            c_x = a_x
            c_y = a_y
            d_x = b_x + width_b
            d_y = a_y + height_a
        elif a_x < b_x and a_y > b_y:
            c_x = a_x
            c_y = b_y
            d_x = b_x + width_b
            d_y = a_y + height_a
        elif a_x > b_x and a_y < b_y:
            c_x = b_x
            c_y = a_y
            d_x = a_x + width_a
            d_y = a_y + height_a
        else:
            c_x = b_x
            c_y = b_y
            d_x = a_x + width_a
            d_y = a_y + height_a

    return f"The coordinates of the big rectangle are:\n left bottom corner - x,y [{c_x},{c_y}] and right top - x,y [{d_x},{d_y}]"


print(rectangle(2,3,4,5,6,6,6,6))
""" ===================================================================================================="""


#4.30
z = randint(100, 999)
first_num = z // 100
second_num = (z // 10) % 10
third_num = z % 10
sum = first_num + second_num + third_num
multip = first_num * second_num * third_num


def if_two_digit():
    if sum > 9 and sum < 100:
        return f"{sum} is a two-digit number!"
    else:
        return f"{sum} isn`t a two-digit number!"


def mult_of_numbers():
    if multip > 99 and multip < 1000:
        return f"Multiplication of {z}`s number = {multip}, and it`s a three-digit number"
    else:
        return f"Multiplication of {z}`s number = {multip}, and it isn`t a three-digit number"


def more_than(a):
    if multip > a:
        return f"{multip} is more than {a}"
    else:
        return f"{multip} is less than {a}"


def multiple_to_5():
    if sum % 5 == 0:
        return f"Sum of the numbers - {sum} is multiple to 5"
    else:
        return f"Sum of the numbers - {sum} isn`t multiple to 5"


def multiple_to_a(a):
    if sum % a == 0:
        return f"Sum of the numbers - {sum} is multiple to {a}"
    else:
        return f"Sum of the numbers - {sum} isn`t multiple to {a}"


print(if_two_digit())
print(mult_of_numbers())
print(more_than(50))
print(multiple_to_5())
print(multiple_to_a(4))
""" ===================================================================================================="""


#4.32
z = randint(1000, 9999)
first_num = z // 1000
second_num = (z // 100) % 10
third_num = (z // 10) % 10
fourth_num = z % 10
first_two = first_num + second_num
second_two = third_num + fourth_num
sum = first_num + second_num + third_num + fourth_num
mult = first_num * second_num * third_num * fourth_num


def sum_of_two():
    if first_two > second_two:
        return f"Sum of first two numbers{first_two} is more than sum of second two numbers {second_two}"
    else:
        return f"Sum of first two numbers{first_two} is less than sum of second two numbers {second_two}"


def divided_by_3():
    if sum % 3 == 0:
        return f"Sum of four numbers = {sum} and they can be divided by 3 evenly"
    else:
        return f"Sum of four numbers = {sum} and they can`t be divided by 3 evenly"


def divided_by_4():
    if mult % 4 == 0:
        return f"Multiplication of 4 numbers {mult} can be divided evenly by 4"
    else:
        return f"Multiplication of 4 numbers {mult} can`t be divided evenly by 4"


def divided_by_a(a):
    if mult % a == 0:
        return f"Multiplication of 4 numbers {mult} can be divided evenly by {a}"
    else:
        return f"Multiplication of 4 numbers {mult} can`t be divided evenly by {a}"


print(sum_of_two())
print(divided_by_3())
print(divided_by_4())
print(divided_by_a(23))
""" ===================================================================================================="""

#4.35
def how_better(a, b, c, d):
    # a,b - parameters of the table
    # c,d - parameters of the rectangles
    if a > b and c > d:
        z1 = (a // c) * (b // d)
        z2 = (a // d) * (b // c)
        print(f"{z1} - horizontally, {z2} - vertically")
        if z1 > z2:
            return f"If you place rectangles horizontally, you`ll place {z1} of them"
        else:
            return f"If you place rectangles vertically, you`ll place {z2} of them"
    else:
        return "Error. a must be bigger than b, c must be bigger than d"


print(how_better(6, 4, 3, 2))
""" ===================================================================================================="""


#4.52
def vasya_fortochka(a, b, d):
    # a,b - window`s parameters, d - diametr of the head, we also need 1 sm from each side
    if a - 1 >= d and b - 1 >= d:
        return "Window has enough space for Vasya to pull his head through."
    else:
        return "Window doesn`t have enough space for Vasya to pull his head through."


print(vasya_fortochka(5, 6, 4))
""" ===================================================================================================="""


# 4.62
def same3():
    z = randint(1000, 9999)
    f1 = z // 1000
    s2 = (z // 100) % 10
    t3 = (z // 10) % 10
    f4 = z % 10
    print(z)
    print(f1,s2,t3,f4)
    if (f1 == s2 and f1 == t3 or f1 == s2 and f1 == f4 or f1 == t3 and f1 == f4) \
    or (s2 == f1 and s2 == t3 or s2 == f1 and s2 == f4 or s2 == t3 and s2 == f4) \
    or (t3 == f1 and t3 == s2 or t3 == f1 and t3 == f4 or t3 == s2 and t3 == f4) \
    or (f4 == f1 and f4 == s2 or f4 == f1 and f4 == t3 or f4 == s2 and f4 == t3):
        return "There are three same digits in this number"
    else:
        return "This number doen`t contain three same numbers"


print(same3())
""" ===================================================================================================="""


#4.96
# a != 0, ax^2 + bx + c = 0
def equation(a, b, c):
    discr = pow(b, 2) - 4 * a * c
    x1 = (-b + pow(discr, 0.5)) / (2 * a)
    x2 = (-b - pow(discr, 0.5)) / (2 * a)
    print(x1, x2)
    if discr == 0:
        return f"Your equation has 1 solution: {x1}"
    elif discr > 0:
        return f"Your equation has 2 solutions: {x1}, {x2}"
    else:
        return "Your equation has no solution"


print(equation(1, 4, -21))
""" ===================================================================================================="""
#4.115
def colored_animal():
    n = int(input("Type a year! - "))
    color = ""
    year = ""
    if n % 5 == 1:
        color = "Green"
    elif n % 5 == 2:
        color = "Red"
    elif n % 5 == 3:
        color = "Yellow"
    elif n % 5 == 4:
        color = "White"
    else:
        color = "Black" \

    if n % 12 == 1:
        year = "Mice"
    elif n % 12 == 2:
        year = "Cow"
    elif n % 12 == 3:
        year = "Tiger"
    elif n % 12 == 4:
        year = "Hare"
    elif n % 12 == 5:
        year = "Dragon"
    elif n % 12 == 6:
        year = "Snake"
    elif n % 12 == 7:
        year = "Horse"
    elif n % 12 == 8:
        year = "Sheep"
    elif n % 12 == 9:
        year = "Monkey"
    elif n % 12 == 10:
        year = "Cock"
    elif n % 12 == 11:
        year = "Dog"
    else:
        year = "Pig"

    return f"This is the year of a {color} {year}!"


print(colored_animal())


def min_average_positive_numbers():
    N = []
    c = 0
    while c < 10:
        q = randint(-50, 50)
        N.append(q)
        c += 1

    print(N)
    min = N[0]
    sum = 0
    above_zero = ""
    for item in N:
        if item < 0:
            if min > item:
                min = item
        if item > 0:
            sum += item
            above_zero += " " + str(item)
    aver = sum / len(N)
    return f"Min = {min}, positive numbers: {above_zero}, average of positive numbers = {aver}"


print(min_average_positive_numbers())
