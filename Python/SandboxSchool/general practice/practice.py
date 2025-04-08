import random

class Student:
    def __init__(self, number_of_students):
        self.number_of_students = number_of_students
        self.grades = []

        for i in range(number_of_students):
            self.grades.append(random.randint(0,100))

    def get_grades(self):
        return self.grades

    def set_grades(self, new_grades):
        # check if new_grades is a list
        if isinstance(new_grades, list):
            # check if every grade is an integer and between 0 and 100
            all_valid = True
            for grade in new_grades:
                if not isinstance(grade, int) or grade < 0 or grade > 100:
                    all_valid = False
                    break  
            if all_valid:
                self.grades = new_grades
            else:
                print("Error: Grades must be integers between 0 and 100.")
        else:
            print("Error: Please provide a list of grades.")

    def __str__(self):
        return f"{self.grades}"
    

    # implement get_sorted_grades(self), get highest grade, get avg grade, get median grade, get mode grade, search grade





def main():
    students = Student(5)

    print(students.grades)



if __name__ == '__main__':
    main()