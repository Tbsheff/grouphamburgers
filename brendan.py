import random as rd 

class Order():
    def __init__(self):
        self.burger_count = 0
    
    def randomBurger():
        return rd.random(1,20)
    
class Person():
    #constructor
    def __init__(self) :
        self.customer_name = self.randomName()    
    #method
    def randomName() :
        lstCustomers = ["Jefe", "El Guapo", "Lucky Day", "Ned Nederlander", "Dusty Bottoms", "Harry Flugleman", "Carmen", "Invisible Swordsman", "Singing Bush"] 
        return rd.choice(lstCustomers)
    

    lstHamburgerQueue = []

iNumCustomers = 100

while iNumCustomers > 0:

    lstHamburgerQueue.append(Customer(iNumCustomers))
    iNumCustomers -= 1
    if customer.customer_name in dictCustomer:
        dictCustomers[customer.customer_name] += customer.order 
