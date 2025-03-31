from random import *

class Shifr:
    def __init__(self):
        self.z = int(input("Введіть числа - "))
    def __shifrator(self):
        x = self.z * randint(1, 50)
        print("Результат обчислень ", x)

run = Shifr()
run._Shifr__shifrator()
