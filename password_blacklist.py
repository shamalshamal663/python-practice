import time 

print("checking...")
time.sleep(2)


def Weak_password_filter(input_fie,output_fie):
    with open(input_fie,"r") as file:
        for line in file:
            password = line.strip().replace(" ","" )
            if len(password) < 8 : 
                with open(output_fie,"a") as out_file:
                    out_file.write(f"{password}\n")


Weak_password_filter("password.txt","blacklisted.txt")                    


