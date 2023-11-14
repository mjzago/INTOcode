
class Person: 
    def __init__(self,name,gewicht,große):
        self.__name = name
        self.__gewicht = gewicht # in kilogram
        self.__große =  große # in metre

    def __str__(self):
        return f"Name: {self.__name} , gewicht: {self.__gewicht} , große: {self.__große} , BMI: {self.getBMI()}"

    def addGewicht(self,gewicht):
        self.__gewicht += gewicht

    def setGewicht(self,gewicht):
        self.__gewicht = gewicht
    
    def setName(self,name):
        self.__name = name

    def setGroße(self, große):
        self.__große = große
        
    def getGroße(self):
        return self.__große

    def getName(self):
        return self.__name

    def getGewicht(self):
        return self.__gewicht

    def getBMI(self):
        if self.__große>0: 
            return self.__gewicht/self.__große*self.__große
        else:
            pass
    
person1 = Person("Max",80,1.6)
person1.setName("Mustermann")
print(person1)
person2 = Person("Julia",90,1.6)
print(person2)


def vergleich(obj1,obj2):
    if obj1.getBMI() > obj2.getBMI(): 
      return obj1.getName()
    
    if obj1.getBMI() < obj2.getBMI(): 
      return obj2.getName()

    if obj1.getBMI() == obj2.getBMI(): 
      return f"Both {obj1.getName()} {obj2.getName()} have the same BMI"
    

print(vergleich(person1,person2))
