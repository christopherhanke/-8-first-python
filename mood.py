#
#
#
#
#

name = input("Hello! Please tell me your name: ")
str_question = "How do you feel today"

if name:
    print("Thank you, "+name+"!")
    str_question = str_question + ", " + name + ": "
else:
    print("That's okay, too.")
    str_question = str_question + ": "

mood = input(str_question)

if mood == "happy":
    str_answer = "It is great to see you happy!"
elif mood == "nervous":
    str_answer = "Take a deep breath 3 times!"
else:
    str_answer = "I don't recognize this mood. Sorry."

print(str_answer)
