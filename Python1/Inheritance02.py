class Person:
    def __init__(self, name, age):
        self.__name = name
        self.__age = age
    
    def __str__(self):
        return f"Name: {self.__name}, Age: {self.__age}"
    
    def printinfo(self):
        print(self.__name, self.__age)
    
    def getName(self):
        return self.__name
    
    def getAge(self):
        return self.__age

class Student(Person):
    def __init__(self, name, age, student_id):
        super().__init__(name, age)
        self.__student_id = student_id
    
    def __str__(self):
        return f"Name: {super().getName()}, Age: {super().getAge()}, Id: {self.__student_id}"
    
    def getStudentId(self):
        return self.__student_id

    def printinfo(self):
        super().printinfo()
        print(f"Student ID: {self.__student_id}")

class Teacher(Person):
    def __init__(self, name, age, subject):
        super().__init__(name, age)
        self.__subject = subject

    def __str__(self):
        return f"Name: {super().getName()}, Age: {super().getAge()}, Subject: {self.__subject}"

    def getSubject(self):
        return self.__subject

    def printinfo(self):
        super().printinfo()
        print(f"Teaches: {self.__subject}")

# Demonstration
person1 = Person("John Doe", 30)
print("Person:")
print(person1)

student = Student("Julia", 25, "1478XD")
print("\nStudent:")
print(student)
student.printinfo()

teacher = Teacher("Mr. Smith", 40, "Mathematics")
print("\nTeacher:")
print(teacher)
teacher.printinfo()
