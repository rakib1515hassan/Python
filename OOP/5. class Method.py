class office:

    def __init__(salf, name, age):
        salf.name = name
        salf.age  = age

    def Display(salf):
        print("Emplaye Name: ", salf.name)
        print("Emplaye Age: ", salf.age)

    @classmethod
    def Maneger(a, m_name):
        print("Maaneger Name: ", m_name)



a = office("Rakib", 26)
r = a.Display()

b = office("Karim", 24)
r2 = b.Display()


office.Maneger("Hassan")
