import random
print("welcome to the guessing game! ")

sec_numb = random.randint(1,10)
guess=0

while sec_numb != guess:
    guess=int(input("guesS the number!"))
    if guess > sec_numb:
        print("Enter the number lower ")
    elif guess< sec_numb:
        print("Enter the number greater ")

print("Congragulation! YOU GUESSED THE SECRET NUMBER !")
  

