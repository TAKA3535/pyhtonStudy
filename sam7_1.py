class Animal:
    def getName(self):
        return self.name
    
    def getWeight(self):
        return self.weight
    
dog = Animal()
dog.name = "トイプードル"
dog.weight = 3

name = dog.getName()
weight = dog.getWeight()

print(name,"は",weight,"kgです")