from random import uniform

class Turtle: # this generates the stats at the start of a race
    def __init__(self, name):
        if name == 'Inky':
            self.name = name
            self.base = 5
            self.max_speed = uniform(8, 11)
            self.acceleration = uniform(8, 11)
            self.score = (self.max_speed + self.acceleration + self.base) / 2
            self.time = round((self.score / 3), 3)
        elif name == 'Blinky':
            self.name = name
            self.base = 5
            self.max_speed = uniform(7, 12)
            self.acceleration = uniform(7, 12)
            self.score = (self.max_speed + self.acceleration + self.base) / 2
            self.time = round((self.score / 3), 3)
        elif name == 'Pinky':
            self.name = name
            self.base = 5
            self.max_speed = uniform(6, 13)
            self.acceleration = uniform(6, 13)
            self.score = (self.max_speed + self.acceleration + self.base) / 2
            self.time = round((self.score / 3), 3)
        elif name == 'Clyde':
            self.name = name
            self.base = 5
            self.max_speed = uniform(5, 14)
            self.acceleration = uniform(5, 14)
            self.score = (self.max_speed + self.acceleration + self.base) / 2
            self.time = round((self.score / 3), 3)