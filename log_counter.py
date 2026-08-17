import time

print("searching....")
time.sleep(2)


def count_log_types(file):
    error_counter = 0
    info_counter = 0
    with open(file,"r") as file:
     for line in file :
        if "ERROR" in line:
            error_counter += 1
        elif "INFO" in line :
            info_counter += 1
     print(f"ERROR count:{error_counter}")
     print(f"INFO count:{info_counter}")



count_log_types("server.log") 