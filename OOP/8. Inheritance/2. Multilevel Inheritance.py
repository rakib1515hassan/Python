class Office:

    def status(self):
        print("Today our office status is Open.")

    def employee(self):
        print("Total Employee = 10")



class Menager(Office):

    def leader(self):
        print("Mr X lead the office.")



class CashOfficer(Menager):

    def cash(self):
        print("Total Cash = 100000/-")



a = CashOfficer()
a.cash()
a.leader()
a.status()
a.employee()



