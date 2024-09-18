print("Welcome to the Quiz game")
playing=input("Do you want to play? ")
if playing.lower() !="yes":
    quit()
score=0

answer=input("what does RAM Stands for? ")
if answer.lower() =="random access memroy":
    print("Correct!")
    score =score+1
else:
    print("InCorrect!")

answer=input("what does CPU Stands for? ")
if answer.lower() =="central processing unit":
    print("Correct!")
    score =score+1
else:
    print("InCorrect")

answer=input("what does PSU Stands for? ")
if answer.lower() =="power supply":
    print("Correct!")
    score =score+1
else:
    print("InCorrect")

answer=input("what does ROM Stands for? ")
if answer.lower() =="read only memroy":
    print("Correct!")
    score =score+1
else:
    print("InCorrect")

print("You Got "+str(score)+" Correct")
print("You Got "+str((score/4)*100)+"%.")