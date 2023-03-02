# Group 7 Hamburger Project

import random

class Order():
    def __init__(self):
        self.burger_count = self.randomBurger()
    
    def randomBurger():
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
    def _innit__(self):
        super().__innit__() 
        self.order = Order()



lstHamburgerQueue = []

dictCustomersOrders = {
    
}

iNumCustomers = 100

while iNumCustomers > 0:

    lstHamburgerQueue.append(Customer())
    iNumCustomers -= 1

