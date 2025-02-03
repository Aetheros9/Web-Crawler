from random import randint

class Die:
    def __init__(self, sides, number, value=0):
        self.sides = sides
        self.number = number
        self.value = value
        self.rolls = []
        self.total = 0

    def roll_die(self):
        if self.sides <= 0:
            raise ValueError("Number of sides must be above zero")
        elif self.number <= 0:
            raise ValueError("Number of dice must be above zero")
        else:
            self.rolls = []
            for i in range(self.number):
                self.rolls.append(randint(1, self.sides))
    
    def find_total(self):
        self.total = sum(self.rolls) + self.value
        return self.total
    
    def display(self):
        self.roll_die()
        total = self.find_total()
        print(f"Rolls: {self.rolls} Total: {total}")