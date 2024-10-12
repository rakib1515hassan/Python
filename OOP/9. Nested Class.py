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
