import datetime


class Goods:
    def __init__(self, name, price):
        self.__name = name
        self.__price = price
        self.__dateOfProduction = datetime.datetime(2020, 2, 10)
        self.__expirationDate = datetime.datetime(2021, 1, 1)

    @property
    def name(self):
        return self.__name

    @property
    def price(self):
        return self.__price

    @property
    def dateOfProduction(self):
        return self.__dateOfProduction

    @property
    def expirationDate(self):
        return self.__expirationDate

    def display_info(self):
        print(f"Info about goods: {self.name, self.price, datetime.datetime.isoformat(self.dateOfProduction)}"
            f"{datetime.datetime.isoformat(self.expirationDate)}")

    def expiration_check(self):
        if self.expirationDate > datetime.datetime.now():
            print("It`s fine")
        elif datetime.datetime.now() == self.expirationDate:
            print("Be careful. It`s last day of usage")
        elif self.expirationDate < datetime.datetime.now():
            print("It`s off.")
        else:
            print("Exception")


class Product(Goods):
    def display_info(self):
        print(self.name, self.price, datetime.datetime.isoformat(self.dateOfProduction),
              datetime.datetime.isoformat(self.expirationDate))


class Batch(Goods):
    __amount = 0

    @property
    def amount(self):
        return self.__amount

    def display_info(self):
        print(self.name, self.price, self.amount, datetime.datetime.isoformat(self.dateOfProduction),
              datetime.datetime.isoformat(self.expirationDate))


class Kit(Goods):
    __product_range = []

    @property
    def product_range(self):
        return self.__product_range

    def display_info(self):
        print(self.name, self.price, self.product_range)

