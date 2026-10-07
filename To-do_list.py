print("Enter tasks to get started")

task_list = [['Task', 'Deadline', 'Status']]

while True:
    task_name = input("Enter a task: ")
    deadline = input("Enter deadline: ")
    status = 'Not_completed'

    task_list.append([task_name, deadline, status])

    while True:
        add_tasks = input("Would you like to add more tasks?: ").strip().lower()

        if add_tasks == 'yes' or add_tasks == 'no':
            break
        else:
            print("Invalid input, enter yes or no")

    if add_tasks == 'no':
                break

for task in task_list:
    print(task)

while True:
    next_step = input("Select next action- add task, delete task, mark complete, exit: ").strip().lower()

    if next_step == 'add task':
        task_name = input("Enter a task: ")
        deadline = input("Enter deadline: ")
        status = 'Not_completed'
        task_list.append([task_name, deadline, status])

        for tasks in task_list:
            print(tasks)

    elif next_step == 'delete task':
        to_delete = input("What task would you like to delete?: ")
        decoy = []
        for row in task_list:
            decoy.append(row[0])

        index_to_delete = decoy.index(to_delete)
        task_list.pop(index_to_delete)
        for task in task_list:
            print(task)

    elif next_step == 'mark complete':
        to_mark = input("Enter a task to mark complete: ")
        decoy = []
        for row in task_list:
            decoy.append(row[0])

        index_to_mark = decoy.index(to_mark)
        task_list[index_to_mark][2] = 'Complete'
        for task in task_list:
            print(task)


    elif next_step == 'exit':
        break

    else:
        print("oops, that's not an option, enter an option from the menu!")       

