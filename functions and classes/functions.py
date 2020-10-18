from math import sqrt


# 1. Write a function that returns the maximum of two numbers.
def max_of_2(x, y):
    if x > y:
        return x
    else:
        return y


# print(max_of_2(1, 2))


# 2. Write a function called fizz_buzz that takes a number.
# If the number is divisible by 3, it should return “Fizz”.
# If it is divisible by 5, it should return “Buzz”.
# If it is divisible by both 3 and 5, it should return “FizzBuzz”.
# Otherwise, it should return the same number.

def fizz_buzz(num):
    if num % 5 == 0 and num % 3 == 0:
        return "FizzBuzz"
    elif num % 3 == 0:
        return "Fizz"
    elif num % 5 == 0:
        return "Buzz"
    else:
        return num


# print(fizz_buzz(20))

# 3. Write a function for checking the speed of drivers. This function should have one parameter: speed.
# If speed is less than 70, it should print “Ok”.
# Otherwise, for every 5km above the speed limit (70), it should give the driver one demerit point and print
# the total number of demerit points. For example, if the speed is 80, it should print: “Points: 2”.
# If the driver gets more than 12 points, the function should print: “License suspended”
def speed_tracker(speed):
    points = 0
    if speed < 70:
        print("Ok")
    else:
        points = (speed - 70) / 5
        print(f"Points: {int(points)}")
    if points > 12:
        print("License suspended")


# speed_tracker(180)

# 4. Write a function called showNumbers that takes a parameter called limit. It should print all the numbers between 0
# and limit with a label to identify the even and odd numbers. For example, if the limit is 3, it should print:
# 0 EVEN 1 ODD 2 EVEN 3 ODD

def showNumbers(limit):
    i = 0
    while i < limit:
        if i % 2 == 0:
            print(f"{i} EVEN")
        else:
            print(f"{i} ODD")
        i += 1


# showNumbers(4)

# 5. Write a function that returns the sum of multiples of 3 and 5 between 0 and limit (parameter).
# For example, if limit is 20, it should return the sum of 3, 5, 6, 9, 10, 12, 15, 18, 20.

def sum_of_mult(limit):
    sum = 0
    a = []
    for i in range(limit):
        if i % 3 == 0 or i % 5 == 0:
            a.append(i)
            sum += i
    print(f"The sum of {a} = {sum}")


# sum_of_mult(20)

# 6. Write a function called show_stars(rows). If rows is 5, it should print the following:
def show_stars(rows):
    for i in range(1, rows + 1):
        for j in range(i):
            print("*", end=" ")
        print(" ")


# show_stars(5)


# 7. Write a function that prints all the prime numbers between 0 and limit where limit is a parameter.
def prime_num(limit):
    primes = [2, 3, 5, 7]
    for i in range(2, limit):
        if i % 2 == 0 or i % 3 == 0 or i % 5 == 0 or i % 7 == 0:
            continue
        else:
            primes.append(i)
    print(f"Prime numbers are: {primes}")


# prime_num(100)

# Exercise 1
def shut_down(s):
    if s == "yes":
        return "Shutting down"
    elif s == "no":
        return "Shut down aborted"
    else:
        return "Sorry"


# print(shut_down(1))


# Exercise 2
def try_sqrt(num):
    print(int(sqrt(num)))


# try_sqrt(13689)


# Exercise 3
def distance_from_zero(z):
    if type(z) == int or type(z) == float:
        return abs(z)
    else:
        return "Nope"

# print(distance_from_zero(-5.6))
# print(distance_from_zero("what?"))


# Exercise 4
def compute_pay(hours, rate):
    if hours < 40:
        pay = hours * rate
        print(f"You need to pay - {pay}$")
    else:
        pay = 40 * rate + (hours - 40) * 1.5 * rate
        print(f"You need to pay - {pay}$")

# compute_pay(45, 10)


# Exercise 5
def hotel_cost(nights):
    return 140 * nights


def plane_ride_cost(city):
    places = {"Charlotte": 183, "Tampa": 220, "Pittsburgh": 222, "Los Angeles": 475}
    for place in places:
        if str(city) == place:
            price = int(places[place])
        else:
            continue
        return price


def rental_car_cost(days):
    cost = 40 * days
    if days >= 7:
        cost = cost - 50
        return cost
    elif days >= 3:
        cost = cost - 20
        return cost


def trip_cost(city, days, spending_money):
    print(f"Hotel cost: {hotel_cost(days)}$")
    print(f"Plane ride cost: {plane_ride_cost(city)}$")
    print(f"Rental car cost: {rental_car_cost(days)}$")
    print(f"Spending money: {spending_money}$")
    return hotel_cost(days) + plane_ride_cost(city) + rental_car_cost(days) + spending_money


# print(trip_cost("Los Angeles", 3, 200))


# Exercise 6
def cube(number):
    return number * number * number


def by_three(number):
    if number % 3 == 0:
        return cube(number)
    else:
        return False

# print(by_three(6))
