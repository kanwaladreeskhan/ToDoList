# TO-DO LIST

# Initialize Array for storing tasks
my_tasks = []

while True:
    print("\n===== TO-DO LIST MENU =====")
    print("1. Add Task")
    print("2. View Tasks")
    print("3. Exit")

    choice = input("Enter your choice (1-3): ")

    # Add your Task (Append function)
    if choice == "1":
        task = input("Enter a new task: ")
        my_tasks.append(task)
        print("Task added successfully! ✅")

    # View your Tasks  
    elif choice == "2":
        if len(my_tasks) == 0:
            print("No tasks available.")
        else:
            print("\nYour Tasks:")
            for index, task in enumerate(my_tasks, start=1):
                print(f"{index}. {task}")

    # Exiting Program
    elif choice == "3":
        print("Exiting program... Goodbye! ")
        break

    # Handling of Invalid inputs
    else:
        print("Invalid choice! Please select between 1 and 3.")

