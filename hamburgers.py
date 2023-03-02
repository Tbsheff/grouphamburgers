# Group 7 Hamburger Project

import random

class Order():
    def __init__(self):
        self.burger_count = self.randomBurger()
    
    def randomBurger():
        return rd.randint(1,20)
from random import randint as rd


class Person():
    #constructor
    def __init__(self) :
        self.customer_name = self.randomName()    
    #method
    def randomName(self) :
        lstCustomers = ["Jefe", "El Guapo", "Lucky Day", "Ned Nederlander", "Dusty Bottoms", "Harry Flugleman", "Carmen", "Invisible Swordsman", "Singing Bush"] 
        return random.choice(lstCustomers)



class Customer(Person):
    def _init__(self):
        super().__init__() 
        self.order = Order()





lstHamburgerQueue = []

dictCustomers = {
    "Jefe" : 0,
    "El Guapo" : 0,
    "Lucky Day" : 0,
    "Ned Nederlander" : 0,
    "Dusty Bottoms" : 0,
    "Harry Flugleman" : 0,
    "Carmen" : 0,
    "Invisible Swordsman" : 0,
    "Singing Bush" : 0
}

iNumCustomers = 0

while iNumCustomers < 100 :
    lstHamburgerQueue.append(Customer())
    print(lstHamburgerQueue[iNumCustomers].customer_name)
    if lstHamburgerQueue[iNumCustomers].customer_name in dictCustomers:
        dictCustomers[lstHamburgerQueue[iNumCustomers].customer_name] += lstHamburgerQueue[iNumCustomers].order
    iNumCustomers += 1


listSortedCustomers = sorted(dictCustomers.items(), key=lambda x: x[1], reverse=True)

print(listSortedCustomers) 
#print(f"{name} {burgers}")