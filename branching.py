# todo_list.py

class TodoList:
    def __init__(self):
        self.tasks = []

    def add_task(self, task):
        self.tasks.append(task)

    def remove_task(self, task):
        if task in self.tasks:
            self.tasks.remove(task)
        else:
            print("Task not found!")

    def display_tasks(self):
        if self.tasks:
            print("Todo List:")
            for index, task in enumerate(self.tasks, start=1):
                print(f"{index}. {task}")
        else:
            print("No tasks in the list.")

if __name__ == "__main__":
    todo_list = TodoList()

    while True:
        print("\n1. Add Task")
        print("2. Remove Task")
        print("3. Display Tasks")
        print("4. Quit")
        
        choice = input("Enter your choice: ")

        if choice == "1":
            task = input("Enter task: ")
            todo_list.add_task(task)
        elif choice == "2":
            task = input("Enter task to remove: ")
            todo_list.remove_task(task)
        elif choice == "3":
            todo_list.display_tasks()
        elif choice == "4":
            print("Quitting...")
            break
        else:
            print("Invalid choice. Please try again.")
