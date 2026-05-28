#francis
#todolist
#Make an active to-do list
todo_list = []
done_list = []
while True:
    print(f"You have {len(todo_list)} task(s)")
    if len(todo_list) == 0:
        print("No Tasks! Congratulations!")
    else:
        for i in range(len(todo_list)):
            print(f"{i + 1}. {todo_list[i]}")
    print("Done List:")
    if len(done_list) == 0:
        print("No tasks completed yet")
    else:
        for item in done_list:
            print(" - " + item)
    print("Menu:")
    print("1. Add an item to the To-Do list")
    print("2. Mark an item as done")
    print("3. Clear or remove item from the list")
    print("4. Exit the program")
    choice = input("Choose an option(1,2,3,or 4): ")
    if choice == "1":
        task = input("Enter a new task: ").strip()
        if task == "":
            print("Task can not be empty")
        else:
            todo_list.append(task)
            print("Task Added Successfully")
    elif choice == "2":
        if len(todo_list) == 0:
            print("There are no tasks to mark as done")
        else:
            try:
                task_num = int(input("Enter task number to mark as done: "))
                if 1 <= task_num <= len(todo_list):
                    completed = todo_list.pop(task_num - 1)
                    done_list.append(completed)
                    print("Task marked as done")
                else:
                    print("That task does not exist")
            except ValueError:
                print("Please enter a valid number")
    elif choice == "3":
        print("1. Remove one item")
        print("2. Clear entire list")
        sub_choice = input("Choose an option (1-2): ")
        if sub_choice == "1":
            if len(todo_list) == 0:
                print("No tasks to remove.")
            else:
                try:
                    task_num = int(input("Enter task number to remove: "))
                    if 1 <= task_num <= len(todo_list):
                        todo_list.pop(task_num - 1)
                        print("Task removed.")
                    else:
                        print("That task does not exist.")
                except ValueError:
                    print("Please enter a valid number.")
        elif sub_choice == "2":
            todo_list.clear()
            print("All tasks cleared.")
        else:
            print("Invalid choice.")
    elif choice == "4":
        print("Exiting program.")
        break
    else:
        print("Inavlid option. Please choose 1-4.")
