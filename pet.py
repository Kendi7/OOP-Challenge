
class Pet:
    def __init__(self, name):
        self.name = name
        self.hunger = 5
        self.energy = 5
        self.happiness = 5
        self.tricks = []

    def eat(self):
        # Reduce hunger by 3 (but not below 0), increase happiness by 1
        self.hunger = max(0, self.hunger - 3)
        self.happiness += 1
        print(f"{self.name} current has hunger rate of {self.hunger} and happpiness rate of {self.happiness}")
    def sleep(self):
        self.eat()   #call the method

        # Increase energy by 5 (but not above 10)
        self.energy = min(10, self.energy + 5)
        print(f"{self.name} has eaten and has energy rating of {self.energy}")
    def play(self):
        self.sleep()  #call the method

        # Decrease energy by 2, increase happiness by 2, increase hunger by 1
        self.energy -= 2
        self.happiness += 2
        self.hunger += 1
        print(f"After sleeping {self.name} had the energy rating of {self.energy}\n and happiness rating of {self.happiness}\n and hunger got {self.hunger}")
    def train(self, trick):
         # that teaches your pet a new trick and stores it in a list.
        self.tricks.append(trick)
        
        

    def show_tricks(self):
        # prints all learned tricks.
        #self.train()
       
        print(f"This are the tricks: {self.tricks} ")
        
    def get_status(self):
        self.play()
        self.show_tricks()
        
        print(f"Happiness: {self.happiness}\n, Energy: {self.energy},\n Hunger: {self.hunger}\n and my tricks are {self.tricks}")



