class car(object):
    def __init__(self, price, speed, fuel, mileage):
        self.price = price
        self.speed = speed
        self.fuel = fuel
        self.mileage = mileage
        self.tax
        self.tax()
        self.display_all()

    def tax(self):
        if self.price >= 10000:
            self.tax = .15
        else:
            self.tax = .12
        return self
    
    def display_all(self):
        print "Car Specs"
        print "Price: " , self.price
        print "Max Speed: " , self.speed
        print "Fuel: " , self.fuel
        print self.mileage
        print "Tax is: " , self.tax
        print "Final Price: ", (self.price + (self.price*self.tax))
        return self

lambo = car(90000, "210mph", "Full", "22mpg")

# ((self.tax*100)*