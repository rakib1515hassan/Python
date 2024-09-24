class Person:

    def __init__(self, f_name, l_name, age):
        self.first_name = f_name
        self.last_name = l_name
        self.age = age

    def name(self):
        print(f"{self.first_name} {self.last_name}")

    def person_details(self):
        print(f"Name: {self.first_name} {self.last_name}, Age: {self.age}")





class Student(Person):

    def __init__(self, f_name, l_name, age, std_class, std_roll):
        Person.__init__(self, f_name, l_name, age)

        self.std_class = std_class
        self.std_roll = std_roll

    def student_info(self):
        print(f"Name: {self.first_name} {self.last_name} Class: {self.std_class} Roll: {self.std_roll}")



class Employee(Person):

    def __init__(self, f_name, l_name, age, salary, emp_id):
        # Person.__init__(self, f_name, l_name, age)
        super().__init__(f_name, l_name, age)  ##? Super Method যদি Call করি তবে self লিখা লাগবে না।

        self.salary = salary
        self.employee_id = emp_id


    def emp_info(self):
        print(f"Name: {self.first_name} {self.last_name} Salary: {self.salary} Roll: {self.employee_id}")




std_1 = Student("Mr", "Tanin", 22, "B.Sc", "1001")
std_2 = Student("Mr", "Emon", 25, "M.Sc", "2001")

std_1.name()
std_2.name()
std_1.student_info()
std_2.student_info()
print("\n")



emp_1 = Employee("Mr", "Hassan", 28, 30000, "5001")
emp_2 = Employee("Mr", "Tuhin", 27, 35000, "5002")


emp_1.name()
emp_2.name()
emp_1.emp_info()
emp_2.emp_info()