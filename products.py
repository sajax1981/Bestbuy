from dataclasses import field


class Car:
    def __init__(self):
        self.odometer = 0

        def drive(self, distance):
            self.odometer += distance


class GasCar(Car):
    def __init__(self, fuel):
        self.odometer = 0
        self.fuel = fuel

    def drive(self, distance):
       fuel_needed = distance +
