#Group 7: Tyler Sheffield, Brendon Bundy, Martin Villar, Camille Cameron, Savannah Hogan, & Hannah
#Hamburger Project

from random import randint as rd
import random



class Order():
    def __init__(self):
        self.burger_count = self.randomBurger()

    def randomBurger(self):
        return rd.randint(1, 20)


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
        self.numBurgers = 0


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

iNumCustomers = 0

lstHamburgerQueue.append(Customer())

print(lstHamburgerQueue[iNumCustomers].customer_name)
if lstHamburgerQueue[iNumCustomers].customer_name in dictCustomers:
    dictCustomers[lstHamburgerQueue[iNumCustomers].customer_name] += lstHamburgerQueue[iNumCustomers].order
    iNumCustomers += 1


listSortedCustomers = sorted(
    dictCustomers.items(), key=lambda x: x[1], reverse=True)

for iCount in range(0, len(listSortedCustomers)):
    print(
        f'{listSortedCustomers[iCount][0].ljust(19)}\t{listSortedCustomers[iCount][1]}')
