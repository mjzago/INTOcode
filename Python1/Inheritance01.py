class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def printinfo(self):
        print(self.name, self.age)


class Student(Person):
    def __init__(self, name, age, id):
        super().__init__(name, age)
        self.student_id = id
    # def printinfo(self):
    #     print(self.name, self.age, self.student_id)


student = Student("John", 25, "1024")
student.printinfo()
