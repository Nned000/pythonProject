# '''Ми вже вміємо створювати класи, але в реальності об’єкти
# постійно взаємодіють. Так само можуть комунікувати між собою
# і програмні об’єкти.
# Оголосимо створення двох класів– авто й людини:'''
# class Human:
#     def __init__(self, name="Human"):
#         self.name = name
#
# class Auto:
#     def __init__(self, brand):
#         self.brand = brand
#         self.passengers = []
#
#     def add_passenger(self, human): #Створимо метод, який реєструє пасажирів авто
#         self.passengers.append(human)
#
#     def print_passengers_names(self): #Додамо метод, що виводить імена пасажирів
#         if self.passengers != []:
#             print(f"Names of {self.brand} passengers:")
#             for passenger in self.passengers:
#                 print(passenger.name)
#         else:
#             print(f"There are no passengers in {self.brand}")
#
# '''Створимо об’єкти двох людей та авто, після чого
# викличемо методи реєстрації пасажирів та виведення їхніх імен'''
# nick = Human("Nick")
# kate = Human("Kate")
# bohdan = Human("Bohdan")
# car = Auto("Mercedes")
# car.add_passenger(nick)
# car.add_passenger(kate)
# car.print_passengers_names()

import random
import logging

logging.basicConfig(level=logging.DEBUG,
                    filename="logs.log", filemode="a",
                    format="We have next logging message: "
                           "%(asctime)s:%(levelname)s-%(message)s"
                    )

class Human:
    def __init__(self, name="Human", job=None, home=None, car=None):
        self.name = name
        self.money = 100
        self.gladness = 50
        self.satiety = 50
        self.job = job
        self.car = car
        self.home = home

    def get_home(self):
        self.home = House()
        logging.info("Received House")

    def get_car(self):
        self.car = Auto(brands_of_car)
        logging.info("Received Car")


    def get_job(self):
        if self.car.drive():
            pass  # нічого не робимо (пропуск)
        else:
            self.to_repair()
            logging.warning("Warning car is broken")
            return  # функція get_job завершує свою роботу
        self.job = Job(job_list)
        logging.info("Received Job")

    def eat(self):
        if self.home.food <= 0:
            logging.warning("Warning there are no food")
            self.shopping("food")
        else:
            if self.satiety >= 100:
                self.satiety = 100
                return
            self.satiety += 5
            self.home.food -= 5
            logging.info("Ate food")

    def work(self):
        if self.car.drive():
            pass
        else:
            if self.car.fuel < 20:
                self.shopping("fuel")
                return
            else:
                self.to_repair()
                return
        logging.info("Worked")
        self.money += self.job.salary
        self.gladness -= self.job.gladness_less
        self.satiety -= 4

    def shopping(self, manage):
        if self.car.drive():
            pass
        else:
            if self.car.fuel < 20:
                manage = "fuel"
                logging.warning("Warning car is empty")
            else:
                self.to_repair()
                logging.warning("Warning car is broken")
                return
        if manage == "fuel":
            print("I bought fuel")
            logging.info("Bought Fuel")
            self.money -= 100
            self.car.fuel += 100
        elif manage == "food":
            print("Bought food")
            logging.info("Bought Food")
            self.money -= 50
            self.home.food += 50
        elif manage == "delicacies":
            print("Hooray! Delicious!")
            logging.info("Bought Delicious")
            self.gladness += 10
            self.satiety += 2
            self.money -= 15

    def chill(self):
        logging.info("Chilling")
        self.gladness += 10
        self.home.mess += 5

    def clean_home(self):
        logging.info("Cleaned home")
        self.gladness -= 5
        self.home.mess = 0
    def to_repair(self):
        logging.info("Repaired Car")
        self.car.strength += 100
        self.money -= 50

    def days_indexes(self, day):   #показники дня
        day = f" Today the {day} of {self.name}'s life "
        print(f"{day:=^50}", "\n")   # \n для переносу рядка(enter)
        human_indexes = self.name + "'s indexes"
        print(f"{human_indexes:^50}", "\n")
        print(f"Money – {self.money}")
        print(f"Satiety – {self.satiety}")
        print(f"Gladness – {self.gladness}")
        home_indexes = "Home indexes"
        print(f"{home_indexes:^50}", "\n")
        print(f"Food – {self.home.food}")
        print(f"Mess – {self.home.mess}")
        car_indexes = f"{self.car.brand} car indexes"
        print(f"{car_indexes:^50}", "\n")
        print(f"Fuel – {self.car.fuel}")
        print(f"Strength – {self.car.strength}")
        logging.info("Showing days indexes")

    def is_alive(self):
        if self.gladness < 0:
            print("Depression…")
            return False # повернути значення false. якщо if спрацєю щось отримає значення false
        if self.satiety < 0:
            print("Dead…")
            return False
        if self.money < -500:
            print("Bankrupt…")
            return False

    def live(self, day):
        if self.is_alive() == False:
            return False
        if self.home is None:
            print("Settled in the house")
            self.get_home()
        if self.car is None:
            self.get_car()
            print(f"I bought a car {self.car.brand}")
        if self.job is None:
            self.get_job()
            print(f"I don't have a job, I'm going to get a job "
                  f"{self.job.job} with salary {self.job.salary}")
        self.days_indexes(day)
        dice = random.randint(1, 4)
        if self.satiety < 20:
            print("I'll go eat")
            self.eat()
        elif self.gladness < 20:
            if self.home.mess > 15:
                print("I want to chill, but there is so much mess…")
                print("So I will clean the house")
                self.clean_home()
            else:
                print("Let`s chill!")
                self.chill()
        elif self.money < 0:
            print("Start working")
            self.work()
        elif self.car.strength < 15:
            print("I need to repair my car")
            self.to_repair()
        elif dice == 1:
            print("Let`s chill!")
            self.chill()
        elif dice == 2:
            print("Start working")
            self.work()
        elif dice == 3:
            print("Cleaning time!")
            self.clean_home()
        elif dice == 4:
            print("Time for treats!")
            self.shopping(manage="delicacies")

brands_of_car = {
    "BMW":{"fuel":100, "strength":100, "consumption": 6},  # словник це ключ та значення. в нашому випадку "ключ":{"ключ":значення, "ключ":значення}
    "Lada":{"fuel":50, "strength":40, "consumption": 10},                                                         # ось це словник в словнику
    "Volvo":{"fuel":70, "strength":150, "consumption": 8},
    "Ferrari":{"fuel":80, "strength":120, "consumption": 14} }


class Auto:
    def __init__(self, brand_list):
        logging.info("Random Car choice")
        self.brand=random.choice(list (brand_list))  # якщо з словаря робити список вибираються ключі
        self.fuel=brand_list[self.brand]["fuel"]   # а тут це вже не список, а знову словарь, тому що ми зробили це на 51 рядку
        self.strength = brand_list[self.brand]["strength"]
        self.consumption=brand_list[self.brand]["consumption"]

    def drive(self):
        if self.strength > 0 and self.fuel >= self.consumption:
            self.fuel -= self.consumption
            self.strength -= 1
            return True
        else:
            print("The car cannot move")
            return False

class House:
    def __init__(self):
        self.mess = 0
        self.food = 0

job_list = {
 "Java developer":
                {"salary":50, "gladness_less": 10 },
 "Python developer":
                {"salary":40, "gladness_less": 3 },
 "C++ developer":
                {"salary":45, "gladness_less": 25 },
 "Rust developer":
                {"salary":70, "gladness_less": 1 },
 }


class Job:
    def __init__(self, job_list):
        logging.info("Random Job Choice")
        self.job=random.choice(list(job_list))
        self.salary=job_list[self.job]["salary"]         # [self.job] - це перший ключ, наприклад C++, а ["salary"] це другий ключ
        self.gladness_less=job_list[self.job]["gladness_less"]

nick = Human(name="Nick")
for day in range(1, 800):
    if nick.live(day) == False:
        break   # зупинити цикл

