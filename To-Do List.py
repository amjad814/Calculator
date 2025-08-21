# to_do_list.py
#Simple To_Do_List Application

tasks = []            # it,s a empty list in which we store the task
def show_menu():
    
    print("To-Do list manu")
    print("1. view task")
    print("2. add task")
    print("3. delete task")
    print("4. exit")

while True:
    show_menu()
    choice = input("enter your choice (1-4):")
    if choice == "1":
        if not tasks:
            print("No task yet")

        else:
            print("/n your task:")
            for i, tasks in enumerate(tasks, start=1):
                print(f"{i}. {task}")
            
    elif choice == "2":
        task = str(input("enter new task:"))
        tasks.append(task)
        print(f"Task '{task}' added")

    elif choice == "3":
        if not tasks:
            print("No task for delete")
        else:
            task_num =int(input("enter task num to delete:"))
            if 0< task_num <= len(tasks):
                removed = tasks.pop(task_num - 1)
                print(f"Task '{removed}'' deleted")
            else:
                print("invalid task number")
    elif choice == "4":
        print("Goodbuy")
        break
    else:
        print("invalid choice please enter 1-4")





    


