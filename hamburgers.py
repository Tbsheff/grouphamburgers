# Group 7 Hamburger Project

from random import randint as rd


class Order():
    def __init__(self):
        self.burger_count = 0

    def randomBurger():
        return rd(1, 20)


class Person:

    pass


class Customer(Person):
    def _innit__(self, iCustomers):
        super().__innit__()
        self.order = Order()
        self.customerID = iCustomers



lstHamburgerQueue = []

iNumCustomers = 100

while iNumCustomers > 0:

    lstHamburgerQueue.append(Customer(iNumCustomers))
    iNumCustomers -= 1
