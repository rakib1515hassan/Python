class Human:
    def __init__(self, name, age, email=None):
        self.name = name
        self.age = age
        self.email = email

    def show_name(self):
        print(self.name)


    ##! Instance Methods 
    def info(self, birthday):
        print(f"Name: {self.name}, Birthday: {birthday}")



obj = Human("Mr Korim", 25, "korim@gmail.com")

obj.show_name()
obj.info(1995)

