todos = []

while True:
    print("\n1. Add task")
    print("2. View tasks")
    print("3. Quit")
    choice = input("Choose: ")

    if choice == "1":
        task = input("Enter task: ")
        todos.append(task)
        print("Task added!")
    elif choice == "2":
        if len(todos) == 0:
            print("No tasks yet!")
        else:
            for i, task in enumerate(todos, 1):
                print(f"{i}. {task}")
    elif choice == "3":
        break