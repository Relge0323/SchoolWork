class Student:
    def __init__(self, name, id_number, department, study_program):
        self.__name = name
        self.__id_number = id_number
        self.__department = department
        self.__study_program = study_program

    def set_name(self, name):
        self.__name = name
    
    def set_id_number(self, id_number):
        self.__id_number = id_number

    def set_department(self, department):
        self.__department = department

    def set_study_program(self, study_program):
        self.__study_program = study_program

    def get_name(self):
        return self.__name

    def get_id_number(self):
        return self.__id_number

    def get_department(self):
        return self.__department

    def get_study_program(self):
        return self.__study_program

students = [
    Student("Lilian Jones", "490242", "Humanities", "Bachelor's in English Literature"),
    Student("Frank Stalfrei", "784921", "Humanities", "Master's in North American History"),
    Student("Zheng Morsey", "012523", "Physics", "Bachelor's in Physics"),
    Student("Antonio Moretta", "472862", "Computer Science", "Master's in Distributed Computing")
]

# I admit I got a little help for this, idk what I was doing here lol
for stu in students:
    print("Name: " + stu.get_name())
    print("ID Number: " + stu.get_id_number())
    print("Department: " + stu.get_department())
    print("Study Program: " + stu.get_study_program())
    print()