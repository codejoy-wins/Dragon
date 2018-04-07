class animal(object):
    def __init__(self, name):
        self.name = name
        self.health = 100
    def walk(self):
        self.health -= 1
        return self
    def run(self):
        self.health -= 5
        return self
    def display_health(self):
        print self.name
        print self.health
        return self

class dog(animal):
    def __init__(self, name):
        super(dog,self).__init__(name)
        self.health = 150
    def pet(self):
        self.health += 5
        return self

class dragon(animal):
    def __init__(self, name):
        super(dragon, self).__init__(name)
        self.health = 170
    def fly(self):
        self.health -= 10
        print "I am flying"
        return self
    def display_health(self):
        super(dragon, self).display_health()
        print "I am a dragon"
        return self
    def breathe_fire(self):
        self.health -= 100
        return self
    def rest(self):
        self.health = 170
        return self
        
cat = animal("Cookie").run().walk().walk().display_health()
chicken = animal("Chic").walk().walk().walk().run().run().display_health()    
    #Create an instance of the Animal, have it walk() three times, run() twice, and finally displayHealth() to confirm that the health attribute has changed.
lab = dog("Chloe").display_health().pet().pet().display_health().run().display_health()
Eragon = dragon("Eragon").fly().display_health().breathe_fire().display_health().fly().rest().display_health().walk().display_health()