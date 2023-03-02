# Group 7 Hamburger Project

import random as rd 

class Order():
    def __init__(self):
        self.burger_count = self.randomBurger()
    
    def randomBurger():
        return rd.randint(1,20)


class Person():
    #constructor
    def __init__(self) :
        self.customer_name = self.randomName()    
    #method
    def randomName() :
        lstCustomers = ["Jefe", "El Guapo", "Lucky Day", "Ned Nederlander", "Dusty Bottoms", "Harry Flugleman", "Carmen", "Invisible Swordsman", "Singing Bush"] 
        return rd.choice(lstCustomers)



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
