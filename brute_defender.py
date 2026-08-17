import time


print("THE BRUTE-DEFENDER! ")
time.sleep(2)

real_password = "admin"
word_list = ["guest", "12345678","password","cypher123","admin"]


attempt = 0
max_attempt = 5

for payload in word_list:
    print(f"Testing payload: {payload}")
    if payload == real_password:
        print("BREACHED! : system compromised ")
        break
    else:
        attempt += 1
        if attempt == max_attempt:
         print("FIREWALL ACTIVATED: ip blocked")   
         break     

