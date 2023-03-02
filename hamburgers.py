# Group 7 Hamburger Project

from random import randint as rd 

class Order():
    def __init__(self):
        self.burger_count = 0
    
    def randomBurger():
        return rd(1,20)




class Customer(Person): 
    def _innit__ (self): 
      super().__innit__()
      self.order = Order()

lstHamburgerQueue = []

iNumCustomers = 100

while iNumCustomers > 0 :
    
    lstHamburgerQueue.append(Customer())
    iNumCustomers -=1

