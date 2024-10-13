
##? Example 1:-
class Merchant:

    def __init__(self, today_status):
        self.s = today_status

    def status(self):
        print("Today status =", self.s)


    class Order:

        def __init__(self, item_1, item_2):
            self.i1 = item_1
            self.i2 = item_2

        def products(self):
            print("Products 1 =", self.i1)
            print("Products 2 =", self.i2)



obj = Merchant("Open")

# obj = Merchant("Open").products()

obj_2 = obj.Order("Apple", "Banana")

obj_2.products()





##? Example 2:-
class Doctors:
    def __init__(self):
        self.name = 'Doctor'
        self.den = self.Dentist()
        self.car = self.Cardiologist()

    def show(self):
        print('In outer class')
        print('Name:', self.name)

    # create a 1st Inner class
    class Dentist:
        def __init__(self):
            self.name = 'Dr. Savita'
            self.degree = 'BDS'

        def display(self):
            print("Name:", self.name)
            print("Degree:", self.degree)

    # create a 2nd Inner class
    class Cardiologist:
        def __init__(self):
            self.name = 'Dr. Amit'
            self.degree = 'DM'

        def display(self):
            print("Name:", self.name)
            print("Degree:", self.degree)


# create a object
# of outer class
outer = Doctors()
outer.show()

# create a object
# of 1st inner class
d1 = outer.den

# create a object
# of 2nd inner class
d2 = outer.car
print()
d1.display()
print()
d2.display()