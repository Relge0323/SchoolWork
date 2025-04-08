import random

class StudentGrades:
    def __init__(self, number_of_students):
        self.grades = []

        self.number_of_students = number_of_students

        for i in range(number_of_students):
            self.grades.append(random.randint(0,100))


    def get_grades(self):
        return self.grades


    def set_grades(self, new_grades):
        self.grades = new_grades


    def __str__(self):
        return str(self.grades)


    def get_sorted_grades(self):
        grades_copy = list(self.grades)

        for i in range(len(grades_copy)):
            for j in range(len(grades_copy) - i - 1):
                if grades_copy[j] > grades_copy[j + 1]:
                    grades_copy[j], grades_copy[j + 1] = grades_copy[j + 1], grades_copy[j]
        return grades_copy


    def get_highest_grade(self):
        max_grade = self.grades[0]
        for i in range(len(self.grades)):
            if max_grade < self.grades[i]:
                max_grade = self.grades[i]
        return max_grade


    def get_average_grade(self):
        sum = 0
        for i in range(len(self.grades)):
            sum += self.grades[i]
        return sum / len(self.grades)


    def get_median_grade(self):
        sorted_list = self.get_sorted_grades()

        if len(sorted_list) % 2 == 1:
            return sorted_list[len(sorted_list) // 2]
        else:
            mid1 = sorted_list[len(sorted_list) // 2]
            mid2 = sorted_list[(len(sorted_list) // 2 )- 1]
            return (mid1 + mid2) / 2


    def get_mode_grade(self):
        a_dict = {}

        for i in self.grades:
            if i not in a_dict:
                a_dict[i] = 1
            else:
                a_dict[i] += 1

        highest = max(a_dict.values())

        mode = []

        for key, count in a_dict.items():
            if count == highest:
                mode.append(key)

        print("Possible mode candidates: ", mode)
        return mode[0]

        
    def search_grade(self, grade):
        if grade in self.grades:
            return True
        else:
            return False

def main():
    total_student = int(input("Enter number of students: "))
    some_grades = StudentGrades(total_student)

    print("initial list of grades: ", some_grades)

    print("sorted grades: ", some_grades.get_sorted_grades())

    print("highest grade: ", some_grades.get_highest_grade())

    print("average grade: ", some_grades.get_average_grade())

    print("median grade: ", some_grades.get_median_grade())

    print("mode grade: ", some_grades.get_mode_grade())

    user_input = int(input("Enter a number from 0 to 100 to search for a grade: "))
    print("searching for a grade...: ", some_grades.search_grade(user_input))



if __name__ == '__main__':
    main()