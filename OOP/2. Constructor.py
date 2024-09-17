class Persone:

    name = "Mr Korim"  ##* `name` is a class variable

    def __init__(self, age, occupation):
        self.age = age
        self.occupation = occupation


obj1 = Persone(25, "Student")
print(obj1.name)
print(obj1.age)
print(obj1.occupation)

print("\n -----------------------------------")
obj2 = Persone(32, "Employee")
print(obj2.name)
print(obj2.age)
print(obj2.occupation)