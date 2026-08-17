import random
import time 


print("WELCOME TO HUNGMAN!")
time.sleep(2)


word_list = ["hack","python","hunt","luffy","zoro"]
secret_word = random.choice(word_list)


display_words = []

for letter in range(len(secret_word)):
    display_words.append("_")
print(display_words)

lives = 6 


while lives > 0 and "_" not in display_words:
    guess = input("Enter the letter that guessed").lower()
    if guess == secret_word:
      for i in range(len(secret_word)):
         
             display_words[i] == guess
             print(display_words)       
    else:
             print("WRONG GUESS : try again")
             lives -= 1
             print (lives)
                 
    if lives == 0:
        print(f"GAME OVER! the secret word was {secret_word}")
        break
    else:
        print("CONGRATULATION YOU WON BY GUESSING THE RIGHT WORD! ")     
   




    



