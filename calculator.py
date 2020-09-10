#
#
#
#
#

print("Welcome to my little calculator.")
print("Add (+), substract (-), multiply (*), divide (/).")

command = input("What do you want to do?")
num_one = int(input("Your first number: "))
num_two = int(input("Your second number: "))
result = None

if command == "+":
    result = num_one + num_two
elif command == "-":
    result = num_one - num_two
elif command == "*":
    result = num_one * num_two
elif command == "/":
    result = num_one / num_two
else:
    print("Your command was invalid.")
    exit()

print("Your result is: " + str(result))
