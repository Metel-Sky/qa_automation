class NameClass:
    name = "Taras"
    age = 23

    def say_hallo(self):
        self.age_name = f"{self.age} - річний {self.name}"
        self.hello_string = f"привіт {self.age_name}, як справи?"
        print(self.hello_string)

    def sey_goodbay(self):
        print(f"Гарного дня {self.age_name}")


obj_1 = NameClass()
obj_1.name = {"name": ["Pasha", "Sasha", "Natasha"]}

obj_1.say_hallo()
