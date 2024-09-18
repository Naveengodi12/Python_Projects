import random

secret_num=random.randint(1,10)
print(secret_num)
count=0


guess =int(input("Enter a Number between1,10 :"))

if guess==secret_num:
    print("You Guessed It")
    count+=1
else:
    print("Wrong Guess!")

print(f"You Guessed in {count} Attempt")