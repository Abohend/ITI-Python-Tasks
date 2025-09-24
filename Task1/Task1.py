import math

# - write a program that prints hello world
print("Hello World")

print("*************************")
# - application to take a number in binary form from the user, and print it as a decimal
s = input("Enter binary number: ")
validBinary = True
for ch in s:
    if ch not in ['1', '0']:
        validBinary = False
        break
if validBinary:
    print("integer:", int(s, 2))
else:
    print("Invalid Binary")

print("*************************")
# - write a function that takes a number as an argument and if the number
# 	divisible by 3 return "Fizz" and if it is divisible by 5 return "buzz" and if is is
# 	divisible by both return "FizzBuzz"
def divisibleBy(number):
    if number % 3 == 0 and number % 5 == 0:
        return "FizzBuzz"
    elif number % 5 == 0:
        return "buzz"
    elif number % 3 == 0:
        return "Fizz"
    else:
        return "NoFizzNoBuzz"
    
print(divisibleBy(15), divisibleBy(9), divisibleBy(10))

print("*************************")
# - Ask the user to enter the radius of a circle print its calculated area and circumference
try:
    r = float(input("Enter radius of the circle: "))
    print("Circumference:", 2 * math.pi * r)
    print("Area:", math.pi * r * r)
except ValueError:
    print("Invalid Number")



print("*************************")
# - Ask the user for his name then confirm that he has entered his name 
# (not an empty string/integers). 
# then proceed to ask him for his email and print all this data
name = input("Enter your name: ").strip()

while not name.isalpha():
    print("Invalid Name")
    name = input("Enter your name: ").strip()

email = input("Enter your email: ").strip()

while '@' not in email or '.' not in email:
    print("Invalid Email")
    email = input("Enter your email: ").strip()

print(f"Your name is {name} and your email is {email}")


print("*************************")
# - Write a program that prints the number of times the substring 'iti' occurs in a string
s = input("Enter a string:")
print("iti appears", s.lower().count("iti") , "times")
