print("ATM LOGIN")

sec_num = 1311
attempt = 0 
max_attempt = 3

while attempt < max_attempt:
    guess = int(input("ENTER THE PIN "))
    attempt += 1
    if sec_num == guess:
        print("ACCESS GRANTED !")
        break
    else:
        print("WRONG PASSWORD ! ") 
        print(attempt)
if attempt == max_attempt:
    print ("ACCOUNT LOCKED : TOO MANY ATTEMPT ")           
