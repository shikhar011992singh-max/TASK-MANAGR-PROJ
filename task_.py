#CHALLNG:TERMINAL BASED TASK LIST MANAGR

import os

TASK_FILE = "tasks.txt"

def load_tasks():
      tasks = []
      if(os.path.exists(TASK_FILE)):
            with open(TASK_FILE,'r',encoding="utf-8")as f:
                  for line in f:
                     text, status = line.strip().rsplit("||", 1)
                     tasks.append({"text": text, "done": status == "done"})
      return tasks   #.."||"--REFERS TO PIPE SIGN OR SPLITTER/DIVIDER BTW SNTNCES,WORDS..  

def save_tasks(tasks):
      with open (TASK_FILE,"w",encoding="utf-8")as f:
            for task in tasks:
                  status = " done" if task["done"] else "not_done"
                  f.write(f"{task['text']} || {status}\n")

def display_tasks(tasks):
      if not tasks:
            print(f"NO TASKS FOUND")
      else:
            for i, task in enumerate(tasks, 1):
                  checkbox = "✅" if task["done"] else " "
                  print(f"{i}. [{checkbox}] {task['text']}")
      print()

def task_manager():
      tasks = load_tasks()

      while True:
            print("\n------Task List Manager------")
            print("1. Add task")
            print("2. View tasks")
            print("3. Mark task as complete")
            print("4. Delete tasks")
            print("5. Exit")

            choice = input("choose an option (1-5).strip()")

            match choice:

                case "1":
                    text = input("enter your task").strip()
                    if text:
                        tasks.append({"text":text, "done": False})
                        save_tasks(tasks)
                    else:
                        print("task cannot be empty")
            
                case "2":
                   display_tasks(tasks)
                case "3":
                   display_tasks(tasks)
                   try:
                      num = int(input("enter task number"))
                      if 1 <= num <= len(tasks):
                         tasks[num-1] ["done"]= True
                         save_tasks(tasks)
                         print("task marked as DONE ")
                      else:
                          print("invalid task number")
            
                   except ValueError:
                       print("enter a number")
                case"5":
                  print("exiting task manager")
                  break
                case _:
                  print("please choose a valid option")

task_manager()

              
      
