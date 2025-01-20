import random

target = random.randint(1,100)

while True:
    guess = (input("guess the number or Quit(q):"))
    if (guess == "q"):
        break

    guess = int(guess)
    if (guess == target):
        print("success : Correct guess ")
    elif (guess < target):
        print ("guess the bigger number..")
    else:
        print("guess the smaller number..")
        
print("---GAME OVER---")
