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





