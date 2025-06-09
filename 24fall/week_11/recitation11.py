def hello():
    print("Hello, World!")
    print("How are you?")
hello()
hello()

gpa = float(input("Enter your GPA: "))
if gpa > 2.0:
    print(f"Your GPA is {str(gpa)}. Your application is accepted.")
elif gpa == 2.0:
    print("Your application is on hold")
else:
    print(f"Your GPA is {str(gpa)}. Your application is denied.")

for int_name in [1, 2, 3, 4, 5]:
    print("Number is", int_name)

for i in range(1, 20, 5):
    print(i)

number = 1
while number < 200:
    number = number * 2
    print(number, end=" ")

def add_numbers(num1, num2):
    sum = num1 + num2
    print("\nSum: ", sum)

add_numbers(5, 4)

def find_square(num):
    result = num * num
    return result
    
sq = find_square(5)
print("\nSquare: ", sq)

name = input("Enter Your Name: ")
print(f"Hello, {name}")

user_choice = input("Do you want to continue? (Yes/No): ")
print(f"You have chosen {user_choice}.")

entered_number = input("Enter a number: ")
print(f"type of number is: {type(entered_number)}, {str(entered_number)}.")
entered_number = int(entered_number)
print(f"type of number is: {type(entered_number)}, {str(entered_number)}.")
entered_number = float(entered_number)
print(f"type of number is: {type(entered_number)}, {str(entered_number)}.")

