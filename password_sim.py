import random

letters=['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x'
         'y','z','A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']
numbers=['0','1','2','3','4','5','6','7','8','9']
symbols=['!','@','#','$','%','^','&','*','(',')']

print("Welcome to the Password Genaration")
n_letters=int(input("Enter how many Letters You want?\n"))
n_numbers=int(input("Enter how many Numbers You want?\n"))
n_symbolss=int(input("Enter how many Symbols You want?\n"))

password=""

for i in range(1,n_letters+1):
    char=random.choice(letters)
    password+=char
for i in range(1,n_numbers+1):
    char=random.choice(numbers)
    password+=char
for i in range(1,n_letters+1):
    char=random.choice(symbols)
    password+=char

print(password)