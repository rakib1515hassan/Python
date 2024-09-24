
##! Example 1:-
# class Office:

#     def status(self):
#         print("Today our office status is Open.")

#     def employee(self):
#         print("Total Employee = 10")



# class Menager(Office):

#     def leader(self):
#         print("Mr X lead the office.")



# class CashOfficer(Menager):

#     def cash(self):
#         print("Total Cash = 100000/-")



# a = CashOfficer()
# a.cash()
# a.leader()
# a.status()
# a.employee()



##! Example 2:-
class Person:
  def __init__(self, fname, lname):
    self.firstname = fname
    self.lastname = lname

  def name(self):
    # print(self.firstname, self.lastname)
    return f"{self.firstname} {self.lastname}"



class Student(Person):
    def __init__(self, fname, lname, student_class, student_roll):
        Person.__init__(self, fname, lname)

        self.student_class = student_class
        self.student_roll = student_roll

    def student_info(self):
        print(f"Name: {self.firstname} Class: {self.student_class} Roll: {self.student_roll}")


class Subject(Student):
    def __init__(self, fname, lname, student_class, student_roll, subject, subject_code):
       Student.__init__(self, fname, lname, student_class, student_roll)
       self.subject = subject
       self.subject_code = subject_code

    def info(self):
       name = f"{self.firstname} {self.lastname}"
       return f"Name: {name}, class: {self.student_class}, {self.subject}({self.subject_code})"


sub_1 = Subject("Mr.", "korim", "x", "1001", "Physics", "401")
stu_name = sub_1.name()
print("Student Name: ", stu_name)
print('\n')


sub_1.student_info()
print("\n")


sub_info = sub_1.info()
print(sub_info)