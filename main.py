import random
score = 0
print("Hello dear user, welcome to my math quizz")
while True:
    number = random.randint(0,150)
    number1= random.randint(10,100)
    operation = random.choice(['+', '-', '*', ])
    if operation == '+':
        correct = number + number1
    elif operation == '-':
        correct = number - number1
    elif operation == '*':
        correct = number * number1
    print(f"\n what is {number} {operation} {number1}?")
    while True:
        print("please enter a value")
        user_solution = input().strip()
        try:
            user_solution = int(user_solution)
            break
        except ValueError:
            print("please enter a whole number, no text")
    if user_solution == correct:
        print("good job, Herr Schreiber would be proud")
        score += 1
        print(f"your current score is {score}")
    else:
        print(f"not really you are a disgrace to herr Schreiber the answer is {correct}")
    print("if you want to continue, press 1. To exit press 2")
    choice = input().strip()
    if choice == "2":
        print("have a great day and thank you for playing")
        break
        