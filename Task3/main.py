# 3. A main.py file must import all task modules.
# 4. When main.py runs:
#      - Display a menu showing all tasks with their number & name.
#      - Let the user select which task to execute by entering the task number.
#      - Run only the selected task.
# 5. Use if __name__ == "__main__": script only run in main.py`.

from task4 import transformProducts
from task1 import automateMath
from task2 import validateEmails
from task3 import remind
from task4 import transformProducts
from task5 import manageFile
from task6 import GenerateData

def main():
    while True:
        print("***** Welcome to Day 3 Task *****")
        print("1 -> Math automation.")
        print("2 -> Validate emails.")
        print("3 -> Reminder.")
        print("4 -> Product Transformer.")
        print("5 -> File Manager.")
        print("6 -> Data Generator.")
        choice = input("Enter task number: ")
        match choice:
            case "1":
                automateMath()
            case "2":
                validateEmails()
            case "3":
                remind()
            case "4":
                transformProducts()
            case "5":
                manageFile()
            case "6":
                GenerateData()
            case _:
                print("Enter a valid choice")

if __name__ == "__main__":
    main()