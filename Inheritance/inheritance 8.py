class phoneDirectory:
    notes = {1: "Tom", 2: "Bob", 3: "Bill", 4: "Petro", 5: "Vasya"}

    def __init__(self, adress, phoneNumber):
        self.__adress = adress
        self.__phoneNumber = phoneNumber

    @property
    def adress(self):
        return self.__adress

    @property
    def phoneNumber(self):
        return self.__phoneNumber

    def display_info(self):
        print(f"Those are telephone notes: {self.notes}")

    def searchByKey(self):
        print(f"What u asked for: {self.notes[self.phoneNumber]}")


class Person(phoneDirectory):
    __surname = "someSurname"

    @property
    def surname(self):
        return self.__surname

    def display_info(self):
        print(self.surname, self.adress, self.phoneNumber)


class Organisation(phoneDirectory):
    __naming = "someOrganisation"
    __fax = "someFax"
    __contact_person = "somePerson"

    @property
    def naming(self):
        return self.__naming

    @property
    def fax(self):
        return self.__fax

    @property
    def contact_person(self):
        return self.__contact_person

    def display_info(self):
        print(self.naming, self.adress, self.phoneNumber, self.fax, self.contact_person)


class Friend(Person):
    __birthDate = "someDate"

    @property
    def birhDate(self):
        return self.__birthDate

    def display_info(self):
        print(self.surname, self.adress, self.phoneNumber, self.birhDate)