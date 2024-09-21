class office:

    def __init__(salf, name, age):
        salf.name = name
        salf.age  = age



    ##! এটি একটি Instance Methods। এটিকে সব সময় Object Creaate করে call করতে হবে।
    def Display(salf):
        print("Emplaye Name: ", salf.name)
        print("Emplaye Age: ", salf.age)


    ##! এটি একটি Class Methods। এটিকে Object Creaate করে এবং Direct class এর মধ্যমে call করা যাবে। এবং এটি Peramiter accept করতে পারে।
    @classmethod
    def Maneger(a, m_name):
        print("Maaneger Name: ", m_name)



    ##! এটি একটি Static Methods। এটিকে Object Creaate করে এবং Direct class এর মধ্যমে call করা যাবে। তবে এটি কোন Peramiter accept করতে পারে না।
    @staticmethod
    def cash_officer():
        print("Cashofficer is a honest person.")



# a = office("Rakib", 26)
# a.Display()
# # a.cash_officer()


# office.Display()
# office.Maneger("Hassan")
office.cash_officer()