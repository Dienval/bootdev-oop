class Soldier:
    def ????????(self, name, armor, num_weapons):
        self.name = name
        self.armor = armor
        self.num_weapons = num_weapons

    def get_speed(self):
        speed = 10
        speed -= self.armor
        speed -= self.num_weapons
        return speed


Question 1: In Python, what is the name of the constructor method? (mult. choice)   

[ ] main   
[ ] init   
[ ] __main__   
[x] __init__   


