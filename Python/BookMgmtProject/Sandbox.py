class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    
    def introduce(self):
        return f"Hi, my name is {self.name} and I am {self.age} years old."
    
class Student(Person):
    def __init__(self, name, age, student_id):
        super().__init__(name, age)
        self.student_id = student_id

    def study(self):
        return f"{self.name} is studying."
    
class Teacher(Person):
    def __init__(self, name, age, subject):
        super().__init__(name, age)
        self.subject = subject

    def teach(self):
        return f"{self.name} is teaching {self.subject}"
    


# Creating objects
student = Student("Mike", 40, "S12345")
teacher = Teacher("Mr. Bupkis", 55, "Math")


print(student.introduce())
print(student.study())
print(teacher.introduce())
print(teacher.teach())