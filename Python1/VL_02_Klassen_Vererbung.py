class Person:
    def __init__(self,name,age):
        self.__name = name
        self.__age = age
    
    def __str__(self):
        return f"Name: {self.__name} Age: {self.__age}"
    
    def printinfo(self):
        print (self.__name, self.__age)
    
    def getName(self):
        return self.__name
    
    def getAge(self):
        return self.__age

# Without inherintance
# class Student ():
#     def __init__(self, name, age, id):
#         self.__name = name
#         self.__age = age
#         self.__id = id
    
#     def __str__(self):
#         return f"Name: {self.__name} Age: {self.__age} Id: {self.__id}"
    
#     def printinfo(self):
#         print (self.__name, self.__age, self.__id)      

# With inherintance
class Student (Person):
    def __init__(self, name, age, student_id):
        super().__init__(name, age)
        self.__student_id = student_id
    
    def __str__(self):
        return f"Name: {super().getName()} Age: {super().getAge()} Id: {self.__student_id}"
    
    def getStudentId(self):
        return self.__student_id

    def printinfo(self):
        #super().printinfo()
        print (super().getName(), super().getAge(), self.__student_id)  


student = Student("Julia",25,"1478XD")
student.printinfo()
print(student)