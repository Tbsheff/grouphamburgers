# Group 7 Hamburger Project

import random as rd 

class Order():
    def __init__(self):
        self.burger_count = self.randomBurger()
    
    def randomBurger():
        return rd.randint(1,20)


class Customer ():
    
    pass


lstHamburgerQueue = []

iNumCustomers = 100

while iNumCustomers > 0 :
    
    lstHamburgerQueue.append(Customer())
    iNumCustomers -=1

class Customer(Person): 
    def _innit__ (self): 
      super().__innit__()
      self.order = Order()
