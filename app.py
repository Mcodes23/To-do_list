# Main class
class Todo(object):
    def __init__(self):
        self.tasks = []

    def addTask(self):
        taskName = input("Enter task name: ").strip().lower()
        taskDescription = input("Enter task description: ").strip().lower()
        taskStatus = "pending"

        if not taskName:
            print("Task name cannot be empty.")
            return

        newTask = {
            "taskName": taskName,
            "taskDescription": taskDescription,
            "taskStatus": taskStatus
        }

        self.tasks.append(newTask)
        print(f"Task '{taskName}' added successfully!")

    def viewTasks(self):
        if not self.tasks:
            print("No tasks available.")
        else:
            for task in self.tasks:
                print("-" * 30)
                print(f"Task Name: {task['taskName']}")
                print(f"Description: {task['taskDescription']}")
                print(f"Status: {task['taskStatus']}")
                print("-" * 30)

    def updateStatus(self):
        taskName = input("Enter task name to update status: ").lower()
        found = False
        for task in self.tasks:
            if task["taskName"] == taskName:
                newStatus = input("Enter new status (pending/completed): ").lower()
                if newStatus not in ["pending", "completed"]:
                    print("Invalid status. Please enter 'pending' or 'completed'.")
                    return
                task["taskStatus"] = newStatus
                print("Task updated successfully!")
                found = True
                break
        if not found:
            print("Task not found.")

    def deleteTask(self):
        taskName = input("Enter task name to delete: ").lower()
        found = False
        for task in self.tasks:
            if task["taskName"] == taskName:
                self.tasks.remove(task)
                print(f"Task '{taskName}' deleted successfully.")
                found = True
                break
        if not found:
            print("Task not found.")

def main():
    todo = Todo()
    while True:
        print('''
What do you want to do?
1. Add Task(s)
2. View Tasks
3. Update Status
4. Delete Task
5. Exit Program''')

        try:
            userChoice = int(input("Enter a number from (1-5): "))
        except ValueError:
            print("Please enter a valid number.")
            continue

        if userChoice == 1:
            todo.addTask()
        elif userChoice == 2:
            todo.viewTasks()
        elif userChoice == 3:
            todo.updateStatus()
        elif userChoice == 4:
            todo.deleteTask()
        elif userChoice == 5:
            confirm = input("Are you sure you want to exit? (yes/no): ").lower()
            if confirm == "yes":
                print("Exiting program. Goodbye!")
                break
        else:
            print("Invalid input. Please try again.")

if __name__ == "__main__":
    main()
