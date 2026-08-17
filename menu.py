

running = True

while running:
    print("TERMINAL SETTINGS! ")
    print("1: view system status ")
    print("2: Run security scan ")
    print("3: EXIT")



    choice = input("select your option: ")



    if choice == "1":
        print("All Sessions Operational ")
    elif choice == "2":
        print("Scanning network........No threat found ")
    elif choice == "3":
         print("Exiting utility...Goodbye! ")
         break
    else:
        print("Invalid option!! please pick from 1,2 or 3")         

    