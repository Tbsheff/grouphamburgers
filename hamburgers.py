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
        super().__innit__() 
        self.order = Order()



lstHamburgerQueue = []

dictCustomers = {
    "Jefe" : 0,
    "el Guapo" : 0,
    "Lucky Day" : 0,
    "Ned Nederlander" : 0,
    "Dusty Bottoms" : 0,
    "Harry Flugleman" : 0,
    "Carmen" : 0,
    "Invisible Swordsman" : 0,
    "Singing Bush" : 0
}

iNumCustomers = 100

while iNumCustomers > 0:

    lstHamburgerQueue.append(Customer())
    iNumCustomers -= 1
    if Customer.customer_name in dictCustomer:
        dictCustomers[Customer.customer_name] += Customer.order 

#print(f"{name} {burgers}")