# Python Practice Tasks
# =====================

# Rules:
#     - Everything must be written inside functions.
#     - The file should run as a script.
#     - When the script starts, the user must see a menu of numbered scenarios  (1: List order, 2: Pepole with favorite color , .....).
#     - The user chooses a number, and the program runs the corresponding function.
#     - Each task should only run when chosen from the menu.
#     - At ANY stage: if the user enters invalid input, the program must:
#           * Show an error message
#           * Display what valid input looks like
#           * Let the user try again (do not crash or exit)




# Tasks:
# ------

# 1 - Ask the user to enter 5 numbers.
#     Store them, then display them in ascending order and descending order.
def listOrder():
    nums = [] 
    # accept the numbers
    for i in range(5):
        s = input(f"Enter number {i + 1}: ")
        while not s.isdigit():
            print('Enter a valid integer number "ex => 1, 2"')
            s = input(f"Enter number {i + 1}: ")
        nums.append(int(s)) 
    # print them
    nums.sort()
    print(f"Numbers in asc. order: {nums}")
    nums.reverse()
    print(f"Numbers in asc. order: {nums}")
    
# 2 - Write a function that takes two numbers: (length, start).
#     Generate a sequence of numbers with the given length,
#     starting from the given start number and increasing by one each time.
#     Print the result.
def generateNums(len, st):
    print([st + i for i in range(len)])

# 3 - Keep asking the user for numbers until they type "done".
#     When finished, print:
#         * The total of all numbers entered
#         * The count of valid entries
#         * The average
#     If the user enters something invalid, show an error and continue.
def calcAverage():
    cnt = 0
    total = 0

    while True:
        s = input("Enter a number (or 'done' to exit): ")
        if s == "done":
            break
        else:
            # validate 
            try:
                num = float(s)
                total += num
                cnt += 1
            except:
                print("Enter a valid float number 'ex -> 1, 1.1'")
    print(f"Total of all numbers entered: {total}")
    print(f"Count of valid entries: {cnt}")
    print(f"Average: {total/cnt}")
    
# 4 - Ask the user to enter a list of numbers.
#     Remove any duplicates, sort the result, and display it.
def sortDestinct():
    length = input("Enter length of numbers: ")
    while not length.isdigit():
        print("enter a valid integer number.")
        length = input("Enter length of numbers: ")
    nums = [] 
    for i in range(int(length)):
        s = input("Enter a number: ")
        # validate
        try:
            num = float(s)
            if num not in nums:
                nums.append(num)
        except:
            print("Please Enter a valid number.")
    nums.sort()
    print(f"Sorted distinct numbers {nums}")

# 6 - Ask the user to enter a sentence.
#     Count how many times each word appears in the sentence
#     and display the result.
def wordCounter():
    sen = input("Enter a sentense:")
    words = sen.lower().split()
    cnt = {}
    for word in words:
        if word in cnt:
            cnt[word] += 1
        else:
            cnt[word] = 1
    # print
    for word, count in cnt.items():
        print(f"word: '{word}' => count: {count}")

# 7 - Create a small gradebook system:
#     - The user enters 5 students names and their scores.
#     - At the end, show:
#         * The highest score
#         * The lowest score
#         * The average score.
def gradeBook():
    scores = {}
    min = ""
    max = ""
    total = 0
    for i in range(5):
        # get the name
        name = input(f"Enter student {i + 1} name: ")
        while not name.isalpha() or name in scores:
            print("Enter a valid (unique) Name (numbers and special characters is not allowed)")
            name = input(f"Enter student {i + 1} name:")

        # get the score
        s = input(f"Enter student {i + 1} score: ")
        while not s.isdigit():
            print("Enter a vlid score: ex-> 1, 5, 20")
            s = input(f"Enter student {i + 1} score:")
        
        score = int(s)
        # store the student
        scores[name] = score

        # update min, max, total
        if max == "" or score > scores[max]:
            max = name
        if min == "" or score < scores[min]:
            min = name
        total += score

    print(f"The highest score: {scores[max]} for {max}")
    print(f"The lowest score: {scores[min]} for {min}")
    print(f"The average score: {total/len(scores)}")
        

# 8 - Write a program that simulates a shopping cart:
#     - The user can add items with a name and a price.
#     - The user can remove items by name.
#     - The user can view all items with their prices.
#     - At the end, display the total cost.
def simulateCart():
    items = {}
    cost = 0
    while True:
        print("1: add item")
        print("2: remove item")
        print("3: view all items")
        print("4: exit")
        s = input("Enter a valid Choice: ")
        match s:
            case "1":
                name = input("Enter item name: ")
                priceS = input("Enter price: ")
                try:
                    price = float(priceS)
                    items[name] = price
                    cost += price
                except:
                    print("Invalid Price ex -> 1, 1.1")
            case "2":
                name = input("Enter item name:")
                try:
                    del items[name]
                    cost -= price
                except:
                    print("name doensn't exist")
            case "3":
                print(items)
            case "4":
                print(f"Cost {cost}")
                break
            case _:
                print("Invalid choice.")


# 9 - Create a number guessing game:
#     - The program randomly selects a number between 1 and 20.
#     - The user keeps guessing until they get it right.
#     - After each guess, show if the guess was too high or too low.
#     - When correct, display the number of attempts.
import random
def guessGame():
    num = random.randint(1, 20)
    attempts = 0
    guess = input("Guess: ")
    while str(num) != guess:
        # validate int
        while not guess.isdigit():
            print("Invalid integer. ex=> 1, 10, 20")

        if int(guess) > num:
            print("too high")
        else:
            print("too low")
        
        guess = input("Guess: ")
        attempts += 1
    print(f"True guess. Number of attempts {attempts + 1}")
    
    
    



while True:
    print("***Hello from Day 2 Task*******")
    print("Choose task to run ...")
    print("1: List order.")
    print("2: Generate a sequence of nums.")
    print("3: Print Average / Total for the entred nums.")
    print("4: sort distinct nums")
    print("6: word counter")
    print("7: Gradebook system")
    print("8: Shopping Cart")
    print("9: guess game")
    print("10: exit")
    
    choice = input("Enter a choice: ")
    match choice:
        case "1":
            listOrder()
        case "2":
            lenS = input("Enter a length: ")
            while not lenS.isdigit():
                print("Invalid length ex=> 5, 7")
                lenS = input("Enter a length: ")
            len = int(lenS)
            stS = input("Enter starting point: ")
            while not stS.isdigit():
                print("Invalid start ex=> 5, 7")
                stS = input("Enter a length: ")
            st = int(stS)
            generateNums(len, st)
        case "3":
            calcAverage()
        case "4":
            sortDestinct()
        case "6":
            wordCounter()
        case "7":
            gradeBook()
        case "8":
            simulateCart()
        case "9":
            guessGame()
        case "10":
            break
        case _:
            print("Invalid choice")