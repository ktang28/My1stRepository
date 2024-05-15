import os

class TaskManager:
    def __init__(self, filename='tasks.txt'):
        self.filename = filename
        self.tasks = []
        self.load_tasks()

    def ensure_file_exists(self):
        if not os.path.exists(self.filename):
            try:
                with open(self.filename, 'w') as file:
                    file.write("Task name :")
            except PermissionError:
                print("Error: Permission denied when creating the grades file.")
                raise

    def load_tasks(self):
        if os.path.exists(self.filename):
            try:
                with open(self.filename, 'r') as file:
                    self.tasks = [line.strip() for line in file.readlines()]
            except (PermissionError, FileNotFoundError) as e:
                print(f"Error loading tasks: {e}")

    def save_tasks(self):
        try:
            with open(self.filename, 'w') as file:
                for task in self.tasks:
                    file.write(task + '\n')
        except PermissionError:
            print("Error: Permission denied when writing to the tasks file.")

    def add_task(self, task):
        if task:
            self.tasks.append(task)
            self.save_tasks()
            print("Task added successfully.")
        else:
            print("Error: Task cannot be empty.")

    def remove_task(self, task_number):
        try:
            task_number = int(task_number)
            if 0 < task_number <= len(self.tasks):
                removed_task = self.tasks.pop(task_number - 1)
                self.save_tasks()
                print(f"Removed task: {removed_task}")
            else:
                print("Error: Invalid task number.")
        except ValueError:
            print("Error: Task number must be an integer.")

    def view_tasks(self):
        if not self.tasks:
            print("No tasks available.")
        else:
            print("\nTask List:")
            for idx, task in enumerate(self.tasks, start=1):
                print(f"{idx}. {task}")

def main():
    manager = TaskManager()

    while True:
        print("\nTask List Manager")
        print("1: Add a new task   2: Remove a task    3: View all tasks    0: Exit  ")

        choice = input("Choose an option (1/2/3/0): ")

        if choice == '1':
            task = input("Enter the task: ")
            manager.add_task(task)
        elif choice == '2':
            manager.view_tasks()
            task_number = input("Enter the task number to remove: ")
            manager.remove_task(task_number)
        elif choice == '3':
            manager.view_tasks()
        elif choice == '0':
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
