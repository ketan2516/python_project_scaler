def task():

    task =[]
    print("--welcome to the task management system app --")

    total_task = int(input("Enter how many task you want to add ="))
    for i in range(1,total_task+1):
        task_name = str(input(f"Enter task{i}="))
        task.append(task_name)
    print(f"Today's task are\n{task}")


    while True:
        oprations = int(input("Enter 1-Add\n2-Update\n3-Delete\n4-View\n5-Stop/"))
        if oprations == 1:
            add_task = str(input("Enter the task you want to add ="))
            task.append(add_task)
            print(f"The task{add_task} has been sucessfully added , Thanks")
         
        elif oprations == 2:
            update_task = str(input("Enter the task name that you want to update = "))
            if update_task in task:
                update_value = str(input("Enter the value that you want to update: "))
                ind = task.index(update_value)
                task[ind] = update_value
                print(f"The value {update_value} has been sucessfully updated in the list")

        elif oprations ==3:
            delete_value= str(input("Enter the task the wants you to delete from the task"))
            if delete_value in task:
                ind = task.index(delete_value)
                del task[ind]
                print(f"Task {delete_value} has been deleted....")
        
        elif oprations == 4:
            print(f"Total tasks ={task}")
        
        elif oprations == 5:
            print("closing the prpgram..")
            break

        else:
            print("Invalid Input")



def main():
    task()

if __name__ == "__main__":
    main()