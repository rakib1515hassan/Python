class Persone:
    name = "Mr Korim"  ##* `name` is a class variable

    def __init__(self, age, email):
        self.age = age
        self.email = email

    def show(self):            ##* `show` is a class method
        print(self.name)
        print(self.age)
        print(self.email)




obj1 = Persone(25, "Student")
obj1.show()

print("\n -----------------------------------")
obj2 = Persone(32, "Employee")
obj2.show()
