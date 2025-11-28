tasks = []

while True:
    print("\nTo-Do List Menu")
    print("-----------------")
    print("1. View tasks")
    print("2. Add task")
    print("3. Delete task")
    print("4. Mark task as done")
    print("5. Exit")
    choice = input("Enter your choice(1-5): ")

    if choice == "1":
        if not tasks:
            print("No tasks in the list.")
        else:
            print("\nTasks:")
            for i, task in enumerate(tasks, start=1):
                print(f"{i}. {task}")

    elif choice == "2":
        task = input("Enter new task: ")
        tasks.append(task)
        print(f"Task '{task}' added.")

    elif choice == "3":
        if not tasks:
            print("No tasks to delete.")
        else:
            for i, task in enumerate(tasks, start=1):
                print(f"{i}. {task}")
            index = int(input("Enter task number to delete: "))
            if 1 <= index <= len(tasks):
                removed = tasks.pop(index-1)
                print(f"task '{removed}' deleted.")
            else:
                print("Invalid task number.")

    elif choice == "4":
        if not tasks:
            print("No tasks to mark as done.")
        else:
            for i, task in enumerate(tasks, start=1):
                print(f"{i}. {task}")
            index = int(input("Enter task number to mark as done: "))
            if 1 <= index <= len(tasks):
                tasks[index-1] = tasks[index-1] + "✔"
                print("Task marked as done.")
            else:
                print("Invalid task number.")

    elif choice == "5":
        print("Exiting To-Do List. Goodbye!")
        break

    else:
        print("Invalid choice. Please enter number between 1 to 5.")