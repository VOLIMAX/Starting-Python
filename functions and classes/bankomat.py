class ATM:
    def __init__(self, user_money):
        self.__nomin10 = 200
        self.__nomin20 = 100
        self.__nomin50 = 50
        self.__nomin100 = 35
        self.__nomin200 = 20
        self.__nomin500 = 10
        self.__user_money = user_money
        self.__id = 1
        self.cash_sum = self.__nomin10 * 10 + self.__nomin20 * 20 + self.__nomin50 \
                        * 50 + self.__nomin100 * 100 + self.__nomin200 * 200 + self.__nomin500 * 500
        print(f"The sum of ATM`s money before any operations = {self.cash_sum}")

    @property
    def id(self):
        return self.__id

    @id.setter
    def id(self, value):
        if value in range(1, 100):
            self.__id = value
        else:
            print("Wrong id")

    def cash(self):
        answer = input("To receive money press 'r'. To insert money press 'i'- ")

        if answer == "r":
            receive_money = int(input("Type the amount of money you want to receive. Alert! Only 10 - 500 per day - "))

            while receive_money < 10 or receive_money > 500:
                receive_money = int(input("Type the amount correctly - "))

            nomin_type = input("Big 'b' or small 's' banknotes? - ")
            action_money = receive_money
            self.cash_sum = self.cash_sum - receive_money

            if nomin_type == "s":
                banknotes50 = int(receive_money / 50)
                receive_money -= banknotes50 * 50
                banknotes20 = int(receive_money / 20)
                receive_money -= banknotes20 * 20
                banknotes10 = int(receive_money / 10)
                receive_money -= banknotes10 * 10
                print(f"You received {banknotes50} - 50$, {banknotes20} - 20$, {banknotes10} - 10$."
                      f" Total - {action_money}."
                      f" ATM`s balance - {self.cash_sum}")

            elif nomin_type == "b":
                banknotes500 = int(receive_money / 500)
                receive_money -= banknotes500 * 500
                banknotes200 = int(receive_money / 200)
                receive_money -= banknotes200 * 200
                banknotes100 = int(receive_money / 100)
                receive_money -= banknotes100 * 100
                banknotes50 = int(receive_money / 50)
                receive_money -= banknotes50 * 50
                banknotes20 = int(receive_money / 20)
                receive_money -= banknotes20 * 20
                banknotes10 = int(receive_money / 10)
                receive_money -= banknotes10 * 10
                print(f"You received {banknotes500} - 500$,{banknotes200} - 200$,{banknotes100} - 100$,"
                      f"{banknotes50} - 50$, {banknotes20} - 20$, {banknotes10} - 10$."
                      f" Total - {action_money}. ATM`s balance - {self.cash_sum}")

        elif answer == "i":
            insert_money = int(input("Type the amount of money you want to insert - "))
            self.__user_money -= insert_money
            self.cash_sum += insert_money
            print(f"Your balance - {self.__user_money}. ATM`s balance - {self.cash_sum}")

        else:
            print("You typed the wrong letter")


valera = ATM(5000)
valera.id = 60
print(valera.id)
valera.cash()


