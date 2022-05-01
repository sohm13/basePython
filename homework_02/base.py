from abc import ABC
from homework_02 import exceptions



class Vehicle(ABC):

    def __init__(self, weight=100, fuel=100, fuel_consumption=10):
        self.weight = weight
        self.fuel = fuel
        self.fuel_consumption = fuel_consumption
        self.started = False

    def start(self):
        if not self.started and self.fuel > 0:
            self.started = True
        elif self.fuel <= 0:
            raise exceptions.LowFuelError()
    
    def move(self, distance):
        self.fuel = self.fuel - distance*self.fuel_consumption
        if self.fuel < 0:
            raise exceptions.NotEnoughFuel()
