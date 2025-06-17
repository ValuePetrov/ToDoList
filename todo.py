
def show_tasks():
    try:
        with open("tasks.txt", "r") as f:
            tasks = f.readlines()
            if not tasks:
                print("No tasks yet.")
            else:
                print("Your tasks:")
                for i, task in enumerate(tasks, 1):
                    print(f"{i}. {task.strip()}")
    except FileNotFoundError:
        print("No tasks yet.")

def add_task():
    task = input("Enter a new task: ")
    with open("tasks.txt", "a") as f:
        f.write(task + "\n")
    print("Task added.")

while True:
    print("\n1) Show tasks\n2) Add task\n3) Quit")
    choice = input("Choose: ")

    if choice == "1":
        show_tasks()
    elif choice == "2":
        add_task()
    elif choice == "3":
        break
    else:
        print("Invalid option.")
