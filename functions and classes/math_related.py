class Rational:
    def __init__(self, a, b, c, d):
        self.__a = a
        self.__b = b
        self.__c = c
        self.__d = d

    def add(self):
        plus = self.__a + self.__b / self.__c + self.__d
        print(f"Addition - {plus}")

    def subtraction(self):
        minus = self.__a - self.__b / self.__c - self.__d
        print(f"Subtraction - {minus}")

    def mupltiplication(self):
        mult = self.__a * self.__c - (self.__b * self.__d) / (self.__a * self.__d) + self.__b * self.__c
        print(f"Multiplication - {mult}")

    def division(self):
        div = (self.__a * self.__c + (self.__b * self.__d) / (self.__b * self.__c) -
               self.__a * self.__d) / (self.__b * self.__b + self.__d * self.__d)
        print(f"Division - {div}")
