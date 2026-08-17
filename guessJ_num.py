print("NUMBER GUESSING GAME !")
sec_num = 13

guess = 0

while guess != sec_num:
    guess = int(input("Enter your guess"))
    if guess < sec_num:
        print("TOO LOW  : TRY AGAIN ! ")
    elif guess > sec_num:
        print("TOO HIGH : TRY AGAIN ")
print("you guessed it : GREAT JOB ! ")        

        