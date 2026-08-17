#ask input from the user 
#if weak passsword, print "Weak password" 
#moderate password, print "Moderate password consider making it long "
#strong password charecter more than  8 charecteer and check if there is any spacial charecrer, print "Strong password"

password = input("Input a candidate password!: ")


lenght = len(password)
if lenght < 8:
    print("WEAK : PASSWORD IS TOO SHORT ")
elif lenght < 12 :
    print("MODEREATE: CONSIDER MAKING IT LONGER")
elif lenght >= 13:
    print("add spcial charecter to improve the strenght of the passkey ")
    if  '@' or '#' or '$' in password:
        print(" STRONG PASSWORD! ") 


