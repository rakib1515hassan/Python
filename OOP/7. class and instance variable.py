class Office:

    total_employ = 10  ##! Class Variable

    def __init__(self, name, age):
        self.name = name   ##! Instance Variable
        self.age = age     ##! Instance Variable

    def Display(self):
        print(f"Employ Name:{self.name} Age:{self.age}")
        print("Total Employee =", self.total_employ)

    @classmethod
    def Manager(cls, name):
        print("Manager Name :", name)
        print("From Manager, Total Employee =", cls.total_employ)


a = Office("Mr Rakib", 28)
a.Display()


Office.Manager("Mr Hassan")
    



