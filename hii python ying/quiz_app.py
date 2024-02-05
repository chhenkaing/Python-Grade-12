#file name quiz_app.py
name = input("What is your name? ")
print("Hello", name)

age = input("How old are you? ")
print("Nice")

total_point = 0
print("Let's start!!!")
question = input("A for? ")
if question.lower() == "apple":
    total_point = total_point + 1
    print('Correct')
else:
    print('Incorrect')

question = input("6 - 4? ")
if question == "2":
    total_point = total_point + 1
    print('Correct')
else:
    print('Incorrect')

question = input("4 + 5? ")
if question == "9":
    total_point = total_point + 1
    print('Correct')
else:
    print('Incorrect')

question = input("4 * 5? ")
if question == "20":
    total_point = total_point + 1
    print('Correct')
else:
    print('Incorrect')

question = input("5 / 5? ")
if question == "1":
    total_point = total_point + 1
    print('Correct')
else:
    print('Incorrect')

question = input("15 / 3? ")
if question == "5":
    total_point = total_point + 1
    print('Correct')
else:
    print('Incorrect')

print(f"Your total point is: {int(total_point/6*100)}%")




