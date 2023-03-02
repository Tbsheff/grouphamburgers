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
    if Customer.customer_name in dictCustomer:
        dictCustomers[Customer.customer_name] += Customer.order 

#print(f"{name} {burgers}")