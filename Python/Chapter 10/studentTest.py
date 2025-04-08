from student import Student

def main():
    #We are creating a new instance of a Student
    #called stu. The following statement invokes 
    #the __init__ method
    #stu is an instance of the Student class
    stu = Student()
    
    #The following statement will invoke the 
    #__str__ to print the name and age of a student
    print(stu)

    #Set the student name to the user input, then print stu again
    name = input("Enter your name >> ")
    age = int(input("Enter your age >> "))
    stu.setName(name)
    stu.setAge(age)
    print(stu)

    #print each attribute individually
    print("Print each attribute separately")
    print(stu.getName())
    print(stu.getAge())
    print()
    
    #The following will not work because the name and 
    #age attribute are private
    # print(stu.name)
    # print(stu.age)
    # stu.name = 'Sarah'
    # stu.age = 25
    # print(stu.name)
    # print(stu.age)

if __name__ == "__main__":
    main()