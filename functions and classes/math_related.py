class Rational:
    def __init__(self, a, b, c, d):
        self.__a = a
        self.__b = b
        self.__c = c
        self.__d = d
        self.plus = 0
        self.minus = 0
        self.mult = 0
        self.div = 0

    def addition(self):
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

    def comparison(self):
        if self.plus < self.minus and self.plus < self.mult and self.plus < self.div:
            print("Addition is the smallest num")
        elif self.minus < self.plus and self.minus < self.mult and self.minus < self.div:
            print("Subtraction is the smallest num")
        elif self.mult < self.plus and self.mult < self.minus and self.mult < self.div:
            print("Multiplication is the smallest num")
        elif self.div < self.minus and self.div < self.mult and self.div < self.plus:
            print("Division is the smallest num")

        if self.plus > self.minus and self.plus > self.mult and self.plus > self.div:
            print("Addition is the biggest num")
        elif self.minus > self.plus and self.minus > self.mult and self.minus > self.div:
            print("Subtraction is the biggest num")
        elif self.mult > self.plus and self.mult > self.minus and self.mult > self.div:
            print("Multiplication is the biggest num")
        elif self.div > self.minus and self.div > self.mult and self.div > self.plus:
            print("Division is the biggest num")