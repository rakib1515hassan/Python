class Manager:

    def __init__(self, m_name):
        self.m_name = m_name

    def manager_name(self):
        return self.m_name


class Customer:

    def __init__(self, account_no, customer_name):
        self.account_no = account_no
        self.customer_name = customer_name

    def customer_info(self):
        return f"Customer Name: {self.customer_name}, Account No: {self.account_no}"


class Office(Manager, Customer):

    def __init__(self, m_name, account_no, customer_name, office_name):
        Manager.__init__(self, m_name)  
        Customer.__init__(self, account_no, customer_name)  
        self.office_name = office_name  

    def office_info(self):
        m_name = self.manager_name()
        return f"Office Name: {self.office_name}, Manager Name: {m_name}"


obj = Office(
    m_name="Mr Korim",
    account_no="AC5001",
    customer_name="Mr Hassan",
    office_name="ABC Bank",
)


print(obj.office_info())
# print(obj.office_info())
# print(obj.manager_name())
