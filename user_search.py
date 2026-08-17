import time


print("searching!..")
time.sleep(2)


def user_search(filename, target_user):
    with open(filename,"r") as file:
        for line in file:
            username = line.strip()
            if username == target_user:
                print(f"Target user found: {target_user}")
                return True
        else:
            print("Target user not found in file")
            return False

user_search("user.txt","root")            
user_search("user.txt","hacker")