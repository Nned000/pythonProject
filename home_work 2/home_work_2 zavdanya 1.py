import random


class Dog:
    def __init__(self, name):
        self.name = name
        self.lonely = 0  #одинокість
        self.food = 20  #їжа
        self.wash = 20  #чистота
        self.sleep = 0  #на скільки хочеться спати
        self.alive = True

    def to_play(self):
        print("Час грати")
        self.lonely -= 5
        self.wash -= 1
        self.food -= 2
        self.sleep += 3

    def to_sleep(self):
        print("Час спати")
        self.sleep -= 10
        self.food -= 2
        self.lonely += 1

    def to_eat(self):
        print("Час їсти")
        self.food += 10
        self.wash -= 3

    def to_wash(self):
        print("Час митися")
        self.wash += 10
        self.food -= 2
        self.sleep += 1

    def is_alive(self):
        if self.lonely > 30:
            print("Я дуже одинокий...")
            self.alive = False
        elif self.food <= 0:
            print("Я дуже голодний...")
            self.alive = False
        elif self.wash <= 0:
            print("Я дуже бурдний...")
            self.alive = False
        elif self.sleep > 30:
            print("Я дуже хотів спати...")
            self.alive = False

    def end_of_day(self):
        if self.lonely < 0:
            self.lonely = 0
        elif self.sleep < 0:
            self.sleep = 0
        print(f"Одинокість = {self.lonely}")
        print(f"Чситота = {self.wash}")
        print(f"Їжа = {self.food}")
        print(f"Хотіння спати = {self.sleep}")

    def live(self, day):
        day = "День " + str(day) + " із життя " + self.name
        print(f"{day:-^50}")
        live_cube = random.randint(1, 4)
        if live_cube == 1:
            self.to_sleep()
        elif live_cube == 2:
            self.to_play()
        elif live_cube == 3:
            self.to_wash()
        elif live_cube == 4:
            self.to_eat()
        self.end_of_day()
        self.is_alive()


sharik = Dog(name="Шарик")
strelka = Dog(name="Стрілка")
laika = Dog(name="Лайка")
for day in range(365):
    if sharik.alive == False:
        break
    sharik.live(day)
    if strelka.alive == False:
        break
    strelka.live(day)
    if laika.alive == False:
        break
    laika.live(day)
