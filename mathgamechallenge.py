import random
import operator
def random_problem():
    operators = {
        "+": operator.add,
        "-": operator.sub,
        "*": operator.mul,
        "/": operator.truediv,
    }
    number1 = random.randint(1, 10)
    number2 = random.randint(1, 10)
    operation = random.choice(list(operators.keys()))
    answer = operators.get(operation)(number1, number2)
    print(f'What is {number1} {operation} {number2}')
    return answer
def allquestions():
    answer = random_problem()
    guess = float(input())
    return guess == answer
def mathgamechallenge():
    print("How well do you know math?\n")
    score = 0
    for i in range(10):
        if allquestions() == True:
            score += 1
            print("Correct!")
        else:
            print("Incorrect!")
    print(f"Your score is {score}")
mathgamechallenge()
