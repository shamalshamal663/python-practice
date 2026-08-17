print("lock screen !")
sec_num = ("1311")

guess = "" 
while guess != sec_num:
    guess = input( "Enter the password")
    if guess == sec_num:
        print("ACCESS GRANTED !")
       
    else :
     
     print("WRONG PASSWORD:TRY AGAIN")
        