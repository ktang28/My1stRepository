import os

class GradeTracker:
    def __init__(self, filename='grades.txt'):
        self.filename = filename
        self.ensure_file_exists()

    def ensure_file_exists(self):
        if not os.path.exists(self.filename):
            try:
                with open(self.filename, 'w') as file:
                    file.write("Subject,Grade\n")
            except PermissionError:
                print("Error: Permission denied when creating the grades file.")
                raise

    def print_grade(self):
        try:
            with open(self.filename, 'r') as file:
                filegrade = file.readlines()
                print(filegrade)
        except PermissionError:
            print("Error: Permission denied when writing to the grades file.")


    def add_grade(self, subject, grade):
        try:
            grade = float(grade)
            if grade < 0 or grade > 100:
                raise ValueError("Grade must be between 0 and 100.")
        except ValueError as e:
            print(f"Invalid input: {e}")
            return

        try:
            with open(self.filename, 'a') as file:
                file.write(f"{subject},{grade}\n")
            print("Grade added successfully.")
        except PermissionError:
            print("Error: Permission denied when writing to the grades file.")

    def calculate_average(self):
        try:
            with open(self.filename, 'r') as file:
                lines = file.readlines()[1:]  # Skip header line
                if not lines:
                    print("No grades found.")
                    return

                total, count = 0, 0
                for line in lines:
                    _, grade = line.strip().split(',')
                    total += float(grade)
                    count += 1

                average = total / count
                print(f"Average grade: {average:.2f}")
        except FileNotFoundError:
            print("Error: The grades file does not exist.")
        except PermissionError:
            print("Error: Permission denied when reading the grades file.")
        except Exception as e:
            print(f"An unexpected error occurred: {e}")

def main():
    tracker = GradeTracker()

    while True:
        print("\nPlease entry your selection:")
        print("1: Add a new grade, 2: Calculate average grade,3: Read Grade, 0:Exit" )

        choice = input("Choose an option (1/2/3/0): ")

        if choice == '1':
            subject = input("Enter the subject: ")
            grade = input("Enter the grade: ")
            tracker.add_grade(subject, grade)
        elif choice == '2':
            tracker.calculate_average()
        elif choice == '3':
            tracker.print_grade()
        elif choice == '0':
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
