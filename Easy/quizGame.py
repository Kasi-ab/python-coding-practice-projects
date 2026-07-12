print("=====Welcome To My Computer Quiz!====")
playing = input(">> Do you want to play?(yes/no) ")
playing = playing.strip().lower()
if playing != "yes":
    quit()
print(">> Okay! Let's play :) ")
score = 0

answer = input(">> What does CPU stand for? ")
answer = answer.lower().strip()
if answer == "central processing unit":
    print(">> Correct!")
    score += 1
else:
    print(">> Incorrect!")

answer = input(">> What does GPU stand for? ")
answer = answer.lower().strip()
if answer == "graphics processing unit":
    print(">> Correct!")
    score += 1
else:
    print(">> Incorrect!")

answer = input(">> What does RAM stand for? ")
answer = answer.lower().strip()
if answer == "random access memory":
    print(">> Correct!")
    score += 1
else:
    print(">> Incorrect!")

answer = input(">> What does PSU stand for? ")
answer = answer.lower().strip()
if answer == "power supply":
    print(">> Correct!")
    score += 1
else:
    print(">> Incorrect!")

print(f"====YOU GOT {score} QUESTIONS CORRECT!====")
print(f"====YOU GOT {(score/4)*100}% ====")