print("Welcome to the T-20 World-cup Men Quiz Game")
playing=input("Do You Want to Play? ").lower()
if playing !="yes":
    quit()
print("Okay! Let's Play")
score=0

answer=input("Who Scored Most Runs in the Tournament? ")
if answer.lower()=="rahmanullah gurbaz":
    print("Correct!")
    score +=1
else:
    print("Incorrect!")


answer=input("Who Scored Most Sixes in the Tournament? ")
if answer.lower()=="nicholas pooran":
    print("Correct!")
    score +=1
else:
    print("Incorrect!")

answer=input("Who Took Most Wickets in the Tournament? ")
if answer.lower()=="fazal farooqi":
    print("Correct!")
    score +=1
else:
    print("Incorrect!")

answer=input("Who Won the Player of the Match in the Final? ")
if answer.lower()=="virat kohli":
    print("Correct!")
    score +=1
else:
    print("Incorrect!")
     
answer=input("Which Team Won the T-20 Final Match? ")
if answer.lower()=="india":
    print("Correct!")
    score +=1
else:
    print("Incorrect!")

answer=input("Who Won the Player of the tournament.? ")
if answer.lower()=="jasprit bumrah":
    print("Correct!")
    score +=1
else:
    print("Incorrect!")

print("You Got " +str(score)+" Questions Correct")
print("You Got " +str((score/7)*100)+ "%.")
