
##! Example 1:-
class Office:

    def status(self):
        print("Today our office started at 10 AM")



class Employee(Office):

    def __init__(self, name, email):
        self.name = name
        self.email = email

    def info(self):
        print(f"Employee Name: {self.name} Email: {self.email}")

    @classmethod
    def details(cls, name, email):
        print(f"Employee Name: {name} Email: {email}")



b = Employee("Mr Korim", "karim@gmail.com")
# b.info()
# b.status()

# Employee.details("Mr Korim", "karim@gmail.com")


print(issubclass(Employee, Office))  ## True
print(issubclass(Office, Employee))  ## False

print(isinstance(b, Office))  ## True



##! Example 2:-
class Person:
  def __init__(self, fname, lname):
    self.firstname = fname
    self.lastname = lname

  def person_info(self):
    # print(self.firstname, self.lastname)
    return f"{self.firstname} {self.lastname}"



class Student(Person):
    def __init__(self, fname, lname, student_class, student_roll):
        Person.__init__(self, fname, lname)

        self.student_class = student_class
        self.student_roll = student_roll

    def student_info(self):
        print(f"Name: {self.firstname} Class: {self.student_class} Roll: {self.student_roll}")


std_1 = Student("Md Rakib", "Hassan", "x", 1001)
res_1= std_1.person_info()
print(res_1)
std_1.student_info()





