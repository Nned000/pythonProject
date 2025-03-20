#COMPONENTS      їх я не шукав в інтернеті тому щось може бути не вірним
#VIDEO CARDS
gt730 = "GT 730"
rtx3050 = "RTX 3050"
rtx4070 = "RTX 4070"
rtx4090 = "RTX 4090"
#CPU
intelpen = "INTEL PENTIUM II"
core3 = "INTEL CORE I3 3700"
core5 = "INTEL CORE I5 12400"
core9 = "INTEL CORE I9 14900"
#RAM
gb4 = "4 GB"
gb8 = "8 GB"
gb16 = "16 GB"
gb32 = "32 GB"
#SSD
sgb128 = "128 GB"
sgb256 = "256 GB"
sgb512 = "512 GB"
stb1 = "1 TB"

print(f"{"COMPUTER SHOP":-^50}")
print(f"{"YOU CAN BUY":-^50}")
print(f"{"VIDEO CARDS":^50}")
print("1: GT 730, 2 GB VRAM")
print("2: RTX 3050, 4 GB VRAM")
print("3: RTX 4070, 12 GB VRAM")
print("4: RTX 4090, 24 GB VRAM")
uvideocard = int(input("Your video card (print number) - "))

print("\n")
print(f"{"CPU":^50}")
print("1: INTEL PENTIUM II, 1 CORE 2 THREADS")
print("2: INTEL CORE I3 3700, 2 CORE 4 THEARDS")
print("3: INTEL CORE I5 12400, 6 CORE 8 THEARDS")
print("4: INTEL CORE I9 14900, 12 CORE 24 THEARDS")
ucpu = int(input("Your CPU - "))

print("\n")
print(f"{"RAM":^50}")
print("1: 4 GB OF RAM")
print("2: 8 GB OF RAM")
print("3: 16 GB OF RAM")
print("4: 32 GB OF RAM")
uram = int(input("Your RAM - "))

print("\n")
print(f"{"SSD":^50}")
print("1: 128 GB")
print("2: 256 GB")
print("3: 512 GB")
print("4: 1 TB")
ussd = int(input("Your SSD - "))

class Computer:
    def __init__(self,name = "PC", videocard = None, cpu = None, ram = None, ssd = None):
        self.name = name
        self.videocard = uvideocard
        self.cpu = ucpu
        self.ram = uram
        self.ssd = ussd

    def pc_set(self):
        # показати характеристики ПК
        if self.videocard == 1:
            lvid = 1
            print("Your video card is: ", gt730)
        elif self.videocard == 2:
            lvid = 2
            print("Your video card is: ", rtx3050)
        elif self.videocard == 3:
            lvid = 3
            print("Your video card is: ", rtx4070)
        elif self.videocard == 4:
            lvid = 4
            print("Your video card is: ", rtx4090)
        print("\n")

        if self.cpu == 1:
            lcpu = 1
            print("Your CPU is: ", intelpen)
        elif self.cpu == 2:
            lcpu = 2
            print("Your CPU is: ", core3)
        elif self.cpu == 3:
            lcpu = 3
            print("Your CPU is: ", core5)
        elif self.cpu == 4:
            lcpu = 4
            print("Your CPU is: ", core9)
        print("\n")

        if self.ram == 1:
            lram = 4
            print("Your RAM is: ", gb4)
        elif self.ram == 2:
            lram = 8
            print("Your RAM is: ", gb8)
        elif self.ram == 3:
            lram = 16
            print("Your RAM is: ", gb16)
        elif self.ram == 4:
            lram = 32
            print("Your RAM is: ", gb32)
        print("\n")

        if self.ssd == 1:
            lssd = 128
            print("Your SSD is: ", sgb128)
        elif self.ssd == 2:
            lssd = 256
            print("Your SSD is: ", sgb256)
        elif self.ssd == 3:
            lssd = 512
            print("Your SSD is: ", sgb512)
        elif self.ssd == 4:
            lssd = 1024
            print("Your SSD is: ", stb1)
        print("\n")

        self.comp_list = [lvid, lcpu, lram, lssd]

class Steam:
    def __init__(self, computer):
        self.computer = computer
        self.biblioteka = []
        print(f"{"Welcome to Steam":-^50}")
        print("\n")
        print(f"{"Choose game to play":^50}")
        game_list = {1:{"1: Counter Strike 2":50}, 2:{"2: Dota 2":80}, 3:{"3: GTA 5":130}, 4:{"4: Stardew Valley":2},
                     5:{"5: CyberPunk 2077":200}, 6:{"6: Euro Truck Simulator":70}}

        for i in game_list:
            for game_name in game_list[i]:  # изначально берутся ключи из словаря. тут я беру первый ключ например 1
                print(game_name)       #  а тут второй например кс

        self.chsgm = int(input("You want to install (write number) - "))
        print("\n")
        for game_name in game_list[self.chsgm]:
            print(f"You chose: {game_name.split(': ')[1]}")   # відділяємо двокрапку та цифру
            print("\n")
        for game_name, size in game_list[self.chsgm].items():  #game_name ключ size значение
            if self.computer.comp_list[3] < size:
                print("Not enough memory")
                print("\n")
                pass
            else:
                print(f"{game_name.split(': ')[1]}", "is downloading")
                self.biblioteka.append(f"{game_name.split(': ')[1]}")
                self.computer.comp_list[3] -= size
        print("\n")

        while True:   # цикл повторяется пока условия в нем правда
            self.smthelse = str(input("You want to install somthing else (yes/no) - ")).strip().lower()
            print("\n")
            if self.smthelse == "yes":
                self.chsgm = int(input("You want to install (write number) - "))
                print("\n")
                for game_name in game_list[self.chsgm]:
                    print(f"You chose: {game_name.split(': ')[1]}")  # відділяємо двокрапку та цифру
                    print("\n")
                for game_name, size in game_list[self.chsgm].items():  # game_name ключ size значение
                    if self.computer.comp_list[3] < size:
                        print("Not enough memory")
                        print("\n")
                        break
                    else:
                        print(game_name, "is downloading")
                        print("\n")
                        self.biblioteka.append(f"{game_name.split(': ')[1]}")
                        self.computer.comp_list[3] -= size

            elif self.smthelse == "no":
                print("Okay!")
                print("\n")
                break
            else:
                print("Please enter 'yes' or 'no'.")

        print("Your library:", self.biblioteka)
        print("\n")
        print(f"Remaining SSD space: {self.computer.comp_list[3]} GB")

user_computer = Computer(videocard=uvideocard, cpu=ucpu, ram=uram, ssd=ussd)
user_computer.pc_set()


a = Steam(user_computer)





