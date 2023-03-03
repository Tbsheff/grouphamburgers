#Group 7: Tyler Sheffield, Brendan Bundy, Camille (Hannah) Cameron, Hannah Johnson, Martin Villar, Savannah Hogan
#Hamburger Group Project 
#This projects creates and stores a dictionary of customers from a list, 
#randomizes orders for each customer, and tracks the total number of hamburgers ordered 

#import random
import random

#create order class 
class Order():
    #create a constructor that defines an instance variable called burger_count
    def __init__(self):
        self.burger_count = self.randomBurger()

    #create a method called randomBurgers that returns a number between 1 and 20
    def randomBurger(self):
        return random.randint(1, 20)

#create person class 
class Person():
    #create a constructor that defines an instance variable called customer_name
    def __init__(self):
        self.customer_name = self.randomName()
   
    #create a method called randomName() that contains a list of 9 names
    def randomName(self):
        lstCustomers = ["Jefe", "El Guapo", "Lucky Day", "Ned Nederlander", "Dusty Bottoms",
                        "Harry Flugleman", "Carmen", "Invisible Swordsman", "Singing Bush"]
        return random.choice(lstCustomers)

#create customer class that inherits from the person class 
class Customer(Person):
    #create a constructor that calls the parent constructor
    def __init__(self):
        super().__init__()
        #create an instance variable called order in the constructor that is assigned an order object
        self.order = Order()


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


iNumCustomers = 100


for iCount in range(0, iNumCustomers):

    lstHamburgerQueue.append(Customer())
    if lstHamburgerQueue[0].customer_name in dictCustomers:
        dictCustomers[lstHamburgerQueue[0].customer_name] += lstHamburgerQueue[0].order.burger_count
    lstHamburgerQueue.pop(0)


listSortedCustomers = sorted(
    dictCustomers.items(), key=lambda x: x[1], reverse=True)

for iCount in range(0, len(listSortedCustomers)):
    print(
        f'{listSortedCustomers[iCount][0].ljust(19)}\t{listSortedCustomers[iCount][1]}')
