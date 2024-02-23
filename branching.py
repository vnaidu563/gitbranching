class TodoList:
    def __init__(self):
        self.tasks = []

    def add_task(self, task):
        self.tasks.append({"task": task, "completed": False})

    def remove_task(self, task):
        for t in self.tasks:
            if t["task"] == task:
                self.tasks.remove(t)
                print(f"Task '{task}' removed successfully.")
                return
        print("Task not found!")

    def mark_task_complete(self, task):
        for t in self.tasks:
            if t["task"] == task:
                t["completed"] = True
                print(f"Task '{task}' marked as completed.")
                return
        print("Task not found!")

    def display_tasks(self):
        if self.tasks:
            print("Todo List:")
            for index, task in enumerate(self.tasks, start=1):
                status = "Completed" if task["completed"] else "Pending"
                print(f"{index}. [{status}] {task['task']}")
        else:
            print("No tasks in the list.")

if __name__ == "__main__":
    todo_list = TodoList()

    while True:
        print("\n1. Add Task")
        print("2. Remove Task")
        print("3. Mark Task as Completed")
        print("4. Display Tasks")
        print("5. Quit")
        
        choice = input("Enter your choice: ")

        if choice == "1":
            task = input("Enter task: ")
            todo_list.add_task(task)
        elif choice == "2":
            task = input("Enter task to remove: ")
            todo_list.remove_task(task)
        elif choice == "3":
            task = input("Enter task to mark as completed: ")
            todo_list.mark_task_complete(task)
        elif choice == "4":
            todo_list.display_tasks()
        elif choice == "5":
            print("Quitting...")
            break
        else:
            print("Invalid choice. Please try again.")
