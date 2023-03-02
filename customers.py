# This will create a customer class


class Customer(Person):
    def _innit__(self, iCustomers):
        super().__innit__()
        self.order = Order()
        self.customerID = iCustomers



