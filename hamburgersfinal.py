# Group 7 Hamburger Project

import random


class Order():
    def __init__(self):
        self.burger_count = self.randomBurger()

    def randomBurger(self):
        return random.randint(1, 20)


class Person():
    # constructor
    def __init__(self):
        self.customer_name = self.randomName()
    # method

    def randomName(self):
        lstCustomers = ["Jefe", "El Guapo", "Lucky Day", "Ned Nederlander", "Dusty Bottoms",
                        "Harry Flugleman", "Carmen", "Invisible Swordsman", "Singing Bush"]
        return random.choice(lstCustomers)


class Customer(Person):
    def __init__(self):
        super().__init__()
        self.order = Order()


lstHamburgerQueue = []

dictCustomers = {
    "Jefe": 0,
    "El Guapo": 0,
    "Lucky Day": 0,
    "Ned Nederlander": 0,
    "Dusty Bottoms": 0,
    "Harry Flugleman": 0,
    "Carmen": 0,
    "Invisible Swordsman": 0,
    "Singing Bush": 0
}

iNumCustomers = 100

for iCount in range(0, iNumCustomers):

    lstHamburgerQueue.append(Customer())
    if lstHamburgerQueue[0].customer_name in dictCustomers:
        dictCustomers[lstHamburgerQueue[0].customer_name] += lstHamburgerQueue[0].order.burger_count
    lstHamburgerQueue.pop(0)


listSortedCustomers = sorted(
    dictCustomers.items(), key=lambda x: x[1], reverse=True)

for iCount in range(0, len(listSortedCustomers)):
    print(
        f'{listSortedCustomers[iCount][0].ljust(19)}\t{listSortedCustomers[iCount][1]}')