import time 

print("checking!...")
time.sleep(2)


def safe_read_log(filename):
     try:
          with open(filename,"r") as file:
               for line in file:
                    line.strip()
                    print(f"LOG ENTRY:{line.strip()}")
     except FileNotFoundError:
          print(f"ERROR:The file {filename} was not found!")
          with open("audit_error.txt","a") as file2:
               file2.write(f"FAILED ATTEMPT: Could not locate {filename}\n")

                         

    
print("---TEST 1 :VALIDATING THE FILE---")
safe_read_log("server.log")

print("-----TEST 2 : VALIDATING THE FILE ")
safe_read_log("missing_vault.log")