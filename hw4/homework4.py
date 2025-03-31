class Mum:
    def __init__(self):
        self.mum_age = 43
        self.mum_body = "slim"
        self.mum_eyes_col = "green"
        self.mum_height = 167
        self.mum_hair_col = "blond"
        print("Your mum is", self.mum_age, "years old and her height is", self.mum_height, "cm. She is", self.mum_body,
              ", she has", self.mum_eyes_col, "eyes and", self.mum_hair_col, "hair")

class Dad:
    def __init__(self):
        self.dad_age = 46
        self.dad_body = "medium"
        self.dad_eyes_col = "brown"
        self.dad_height = 190
        self.dad_hair_col = "brunet"
        print("Your dad is", self.dad_age, "years old and his height is", self.dad_height, "cm. He is", self.dad_body,
              ", he has", self.dad_eyes_col, "eyes and", self.dad_hair_col, "hair")

class Son(Mum, Dad):
    def __init__(self):
        Mum.__init__(self)
        Dad.__init__(self)
        age = 13
        print("Your son is",age, "years old and his height is", self.mum_height, "cm. He is", self.dad_body,
              ", he has", self.mum_eyes_col, "eyes and", self.dad_hair_col, "hair")

jack = Son()