from bankomat import ATM
from Cats import Cat
from math_related import Rational


class Program:
    Faraday = Cat("Faraday", "Male")
    for i in range(30):
        Faraday.jump()
    print(Faraday.energy)
    for i in range(1):
        Faraday.sleep()
    print(Faraday.energy)

    Ada = Cat("Ada", "Female")
    for i in range(33):
        Ada.jump()
    print(Ada.energy)
    for i in range(5):
        Ada.sleep()
    print(Ada.energy)

    valera = ATM(5000)
    valera.id = 60
    print(valera.id)
    valera.cash()

    smth = Rational(2, 4, 6, 8)
    smth.addition()
    smth.subtraction()
    smth.mupltiplication()
    smth.division()
    smth.comparison()