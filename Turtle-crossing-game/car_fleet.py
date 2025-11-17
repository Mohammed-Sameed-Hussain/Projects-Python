import cars
import random


class CarFleet:
    def __init__(self, screen_height, screen_width):
        self.screen_height = screen_height
        self.screen_width = screen_width
        self.fleet_of_cars = []
        self.timedelay = 0.1
        self.time_decrement = 0.008

    def create_car(self):
        random_chane = random.randint(1, 25)
        if random_chane == 1:
            new_car = cars.Car(self.screen_height, self.screen_width)
            self.fleet_of_cars.append(new_car)

    def move_car(self):
        for car in self.fleet_of_cars:
            car.move()
