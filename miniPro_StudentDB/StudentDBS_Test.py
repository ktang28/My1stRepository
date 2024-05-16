
class Student:
    def __init__(self, name, age, grades =None):
        self.name = name
        self.age = age
        self.grades = grades


    def display_info(self):
        print(f"Name: {self.name}")
        print(f"Age: {self.age}")
        print("Grades:")
        for subject, grade in self.grades.items():
            print(f"  {subject}: {grade}")
        average_grade = self.calculate_average_grade()
        if average_grade is not None:
            print(f"Average Grade: {average_grade:.2f}")
        else:
            print("No grades available to calculate average.")

    def calculate_average_grade(self):
        if not self.grades:
            return None
        return sum(self.grades.values()) / len(self.grades)



class StudentDB:

    def __init__(self):
        self.students = []

    def add_student(self, student):
        self.students.append(student)

    def display_all_students(self):
        if not self.students:
            print("No students in the database.")
            return
        for student in self.students:
            student.display_info()
            print("-" * 20)

    def add_student_interactively(self):
        try:
            name = input("Enter student's name: ")
            age = input("Enter student's age: ")
            if not age.isdigit() or int(age) < 0:
                raise ValueError("Age must be a positive integer.")
            age = int(age)

            grades = {}
            while True:
                subject = input("Enter subject name (or 'done' to finish): ")
                if subject.lower() == 'done':
                    break
                grade = input(f"Enter grade for {subject}: ")
                if not grade.isdigit() or int(grade) < 0 or int(grade) > 100:
                    raise ValueError("Grade must be an integer between 0 and 100.")
                grades[subject] = int(grade)

            student = Student(name, age, grades)
            self.add_student(student)

        except ValueError as e:
            print(f"Error: {e}")


def main():
    st_db = StudentDB()

    while True:
        print("\nPlease entry your selection:")
        print("1: Add a new student, 2: Display student information, 0:Exit" )

        choice = input("Choose an option (1/2/0): ")

        if choice == '1':
            st_db.add_student_interactively()

        elif choice == '2':
            st_db.display_all_students()
        elif choice == '0':
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
