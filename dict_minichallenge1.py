#Goal to create modify and print information from a target profile

#1 create a dictionary with two value pair
target = {
    "hostname":"scanme.org","ip":"45.33.32.156"
        }


#print value of ip from the dictionary
print(target["ip"])

target["os"] = "linux"
target["ip"] = "127.0.0.1"


print(target)