#I want to choose a random message when the task was done on time or if it was done after its deadline
import random
#I create the list where I save all my tasks
tasks = []
#these are the lists of messages that I want to show depending of the status of the task (the program chooses one at random)
messages_ontime = ["Very good, you did it on time!", "Excellent!", "You did it!"]
messages_late = ["You did it late, but no worries, it is finally done.", "Mmm late this time. Next time it should be better."]

#I define a function that shows all the tasks
def show_tasks():
    #I define a counter, that way the tasks show as 1, 2, 3 etc.
    task_number = 1
    #the program goes through the list, one task at a time
    for task in tasks:
        #the program checks if the task is done or not
        if task["Completed"] == True:
            status = "done"
        else:
            status = "pending"
        #the program prints the number, name, deadline and status
        print(task_number, task["Name"], "- limit: day", task["Limit"], "-", status)
        task_number = task_number + 1


doing = True

#program main menu
while doing:
    print("\n--- Home tasks ---")
    print("1. Add a task")
    print("2. See tasks list")
    print("3. Complete a task")
    print("4. Exit")
    #the user types the option
    option = input("Choose an option: ")

    #option 1: add a task
    if option == "1":
        task_name = input("Which task do you want to add? ")
        limit = int(input("Until which day of the month do you have time to do it? "))
         #the program creates a dictionary with the deadline day and the status, pendind or done. all this information is added to the list.
        tasks.append({"Name": task_name, "Limit": limit, "Completed": False})
        print("Task was added")

    #option 2: show the tasks
    elif option == "2":
        show_tasks()

    #option 3: complete a task
    elif option == "3":
        #if the list is empty, there is nothing to complete
        if len(tasks) == 0:
            print("you do not have tasks yet")
        else:
            #show the list in a way that the user can choose
            show_tasks()  
            choice = int(input("which task number did you complete? "))

            #check that the number exists (between 1 and the number of tasks)
            if choice < 1 or choice > len(tasks):
                print("this number does not exists")
            else:
                #the list starts at 0, so I subtract 1 to get the right task
                task = tasks[choice - 1]

                #the program checks that the task is not already done
                if task["Completed"] == True:
                    print("this task was already done")
                else:
                    day_done = int(input("when did you complete the task? "))
                    #the program changes the status to done
                    task["Completed"] = True 

                    #if the day I did it is after the deadline, I was late!
                    if day_done > task["Limit"]:
                        #late message
                        print(random.choice(messages_late))   
                    else:
                        #ontime message
                        print(random.choice(messages_ontime))  
                    show_tasks()

    #option 4: exit
    elif option == "4":
        print("Good bye!")
        #this stops the while loop
        doing = False

    #any other option
    else:
        print("the option is not valid")

#please your feedback. after that, i want the make the difference with colour between the 2 status, the done and the pending ones.
