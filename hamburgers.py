# Group 7 Hamburger Project

import random

class Order():
    def __init__(self):
        self.burger_count = self.randomBurger()
    
    def randomBurger(self):
        return random.randint(1,20)



class Person():
    #constructor
    def __init__(self) :
        self.customer_name = self.randomName()    
    #method
    def randomName(self) :
        lstCustomers = ["Jefe", "El Guapo", "Lucky Day", "Ned Nederlander", "Dusty Bottoms", "Harry Flugleman", "Carmen", "Invisible Swordsman", "Singing Bush"] 
        return random.choice(lstCustomers)



class Customer(Person):
    def __init__(self):
        super().__init__() 
        self.order = Order()
        self.numBurgers = 0





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
    if lstHamburgerQueue[iNumCustomers].customer_name in dictCustomers:
        dictCustomers[lstHamburgerQueue[iNumCustomers]].update() #+= lstHamburgerQueue[iNumCustomers].numBurgers
    iNumCustomers += 1


listSortedCustomers = sorted(dictCustomers.items(), key=lambda x: x[1], reverse=True)

print(listSortedCustomers) 
#print(f"{name} {burgers}")