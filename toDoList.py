tasks = []

def addTask(task):
    tasks.append(task)
    print("************Task added successfully!************")

def viewTasks():
    if not tasks:
        print("************No tasks available.************")
    else:
        print("\nTask List:")
        for i, task in enumerate(tasks, start=1):
            print("{}. {}".format(i, task))

def updateTask(index, newTask):
    if 1 <= index <= len(tasks):
        tasks[index - 1] = newTask
        print("************Task updated successfully!************")
    else:
        print("Invalid task index.")

while True:
    print("\nTo-Do List Application")
    print("1. Add Task")
    print("2. View Tasks")
    print("3. Update Task")
    print("4. Exit")

    choice =int( input("Enter your choice (1-4): "))
    if choice == 1:
        task = input("Enter the task: ")
        addTask(task)

    elif choice == 2:
         viewTasks()

    elif choice == 3:
        viewTasks()
        index = int(input("Enter the task index to update: "))
        newTask = input("Enter the new task: ")
        updateTask(index, newTask)

    elif choice == 4:
        print("************Exiting To-Do List Application.************")
        break
    else:
        print("Invalid choice. Please enter a number between 1 and 4.")
