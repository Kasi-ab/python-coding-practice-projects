import random

print("==== WLECOME NUMBER GUESSING GAME ====")
score = 0
range_ = input(">>Type a number: ")
try:
    range_ = int(range_)
    if range_ <= 0:
        print(">> PLZ type  a number larger than 0 next time")
        quit()
except ValueError:
    print(">> PLZ type a number next time")
    quit()

num = random.randint(0, range_)
while True:
    try:
        guess = int(input(">> Enter your guess: "))
        score += 1
        if guess >= 0:
            if num > guess:
                print(">> Oops!, Try larger number")
            elif num < guess:
                print(">> Oops!, Try lower number")
            else:
                print(f">> Congrats!, You guessed the number in {score} guesses")
                print("==== THANK YOU ====")
                break
        else:
            raise ValueError
    except ValueError:
        print(">> Try vaild number")
        pass
