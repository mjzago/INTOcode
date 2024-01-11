# # Aufgaben 01: 
# class Person: 
#     def __init__(self,name,gewicht,große):
#         self.__name = name
#         self.__gewicht = gewicht # in kilogram
#         self.__große =  große # in metre

#     def __str__(self):
#         return f"Name: {self.__name} , gewicht: {self.__gewicht} , große: {self.__große} , BMI: {self.getBMI()}"

#     def addGewicht(self,gewicht):
#         self.__gewicht += gewicht

#     def setGewicht(self,gewicht):
#         self.__gewicht = gewicht
    
#     def setName(self,name):
#         self.__name = name

#     def setGroße(self, große):
#         self.__große = große
        
#     def getGroße(self):
#         return self.__große

#     def getName(self):
#         return self.__name

#     def getGewicht(self):
#         return self.__gewicht

#     def getBMI(self):
#         if self.__große>0: 
#             return self.__gewicht/self.__große*self.__große
#         else:
#             pass
    
# person1 = Person("Max",80,1.6)
# person1.setName("Mustermann")
# print(person1)
# person2 = Person("Julia",90,1.6)
# print(person2)

# # Aufgaben 02: 
# def vergleich(obj1,obj2):
#     if obj1.getBMI() > obj2.getBMI(): 
#       return obj1.getName()
    
#     if obj1.getBMI() < obj2.getBMI(): 
#       return obj2.getName()

#     if obj1.getBMI() == obj2.getBMI(): 
#       return f"Both {obj1.getName()} {obj2.getName()} have the same BMI"
    

# print(vergleich(person1,person2))

# Aufgaben 03: 

class Auto:
    def __init__(self,marke,preis,model,baujahr):
        self.__marke = marke
        self.__preis = preis
        self.__model = model
        self.__baujahr = baujahr
        self.__rabbatPreis = preis

    def __str__(self):
        return f"Marke: {self.__marke} Preis: {self.__preis} Rabatt Preis: {self.__rabbatPreis} Model: {self.__model} Baujahr: {self.__baujahr}"
    
    def setMarke(self,marke):
        self.__marke = marke
    
    def setPreis(self,preis):
        self.__preis = preis

    def setModel(self,model):
        self.__model = model

    def setBaujahr(self,baujahr):
        self.__baujahr = baujahr

    def getMarke(self):
        return self.__marke
    
    def getPreis(self):
        return self.__preis

    def getModel(self):
        return self.__model

    def getBaujahr(self):
        return self.__baujahr
    
    def setRabatt(self,prozent):
        self.__rabbatPreis = self.__preis - ((prozent/100)*self.__preis)
        return self.__rabbatPreis

vw_tiguan = Auto("VW",7500,"Tiguan",2023)
print(vw_tiguan) 

bmw_x5 = Auto("BMW",70500,"X5",2023)
print(bmw_x5) 

vw_golf = Auto("VW",7500,"Golf",2003)
print(vw_golf) 

vw_tiguan.setPreis(10000)
print(vw_tiguan)
neu_preis = vw_tiguan.setRabatt(50)
print(neu_preis) # 8000


