def task_manager():
    tasks = []
    print("WELCOME TO TASK MANAGEMENT APP")

    # Input the total number of initial tasks
    total_task = int(input("Enter how many tasks you want to add: "))

    # Add initial tasks
    for i in range(1, total_task + 1):
        task_name = input(f"Enter task {i}: ")
        tasks.append(task_name)

    print(f"\nToday's tasks are: {tasks}")

    # Menu loop
    while True:
        print("\nChoose an operation:")
        print("1 - Add Task")
        print("2 - Update Task")
        print("3 - Delete Task")
        print("4 - View Tasks")
        print("5 - Exit")

        try:
            operation = int(input("Enter your choice: "))
        except ValueError:
            print("Invalid input. Please enter a number between 1 and 5.")
            continue

        if operation == 1:
            add = input("Enter task you want to add: ")
            tasks.append(add)
            print(f"Task '{add}' has been successfully added.")

        elif operation == 2:
            updated_val = input("Enter the task name you want to update: ")
            if updated_val in tasks:
                up = input("Enter the new task: ")
                ind = tasks.index(updated_val)
                tasks[ind] = up
                print(f"Task '{updated_val}' has been updated to '{up}'.")
            else:
                print(f"Task '{updated_val}' not found in the list.")

        elif operation == 3:
            delete_task = input("Enter the task name you want to delete: ")
            if delete_task in tasks:
                tasks.remove(delete_task)
                print(f"Task '{delete_task}' has been successfully deleted.")
            else:
                print(f"Task '{delete_task}' not found in the list.")

        elif operation == 4:
            if tasks:
                print("\nCurrent Tasks:")
                for i, task in enumerate(tasks, 1):
                    print(f"{i}. {task}")
            else:
                print("No tasks available.")

        elif operation == 5:
            print("Exiting the Task Manager. Goodbye!")
            break

        else:
            print("Invalid choice. Please select a valid option.")


# Run the task manager function
task_manager()





