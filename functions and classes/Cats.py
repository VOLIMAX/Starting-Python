class Cat:
    def __init__(self, name, gender):
        self.__name = name
        self.__gender = gender
        self.__energy = 20
        self.MaxEnergy = 20
        self.MinEnergy = 0
        self.SleepEnergyGain = 10
        self.JumpEnergyDrain = 0.5
        self.__energy = self.MaxEnergy
        print(f"Your cat`s name is {self.__name}. It`s gender is {self.__gender} and"
              f" it`s energy is equal to {self.__energy}")

    @property
    def energy(self):
        if self.__energy <= self.MinEnergy:
            self.__energy = self.MinEnergy
        if self.__energy >= self.MaxEnergy:
            self.__energy = self.MaxEnergy
        return self.__energy

    @property
    def gender(self):
        return self.__gender

    @gender.setter
    def gender(self, gender):
        if gender == "Male" or gender == "Female":
            self.__gender = gender
        else:
            print("Wrong gender")

    @property
    def name(self):
        return self.__name

    def jump(self):
        self.__energy -= self.JumpEnergyDrain

    def sleep(self):
        self.__energy += self.SleepEnergyGain


