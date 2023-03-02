class Customer(Person): 
    def _innit__ (self): 
      super().__innit__()
      self.order = Order()